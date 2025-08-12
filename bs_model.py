# bs_model.py

"""
Simple Black-Scholes function that returns (call_price, put_price).

Usage:
    from bs_model import black_scholes
    call, put = black_scholes(S=100, K=100, r=0.05, sigma=0.2, T=1.0, q=0.0)

Notes:
- S: spot price
- K: strike price
- r: risk-free rate (annual, decimal)
- sigma: volatility (annual, decimal)
- T: time to maturity (in years)
- q: continuous dividend yield (default 0)
"""
import math
from typing import Tuple


def _phi(x: float) -> float:
    """Standard normal PDF"""
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def _Phi(x: float) -> float:
    """Standard normal CDF using math.erf (no external deps)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _d1(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    return (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))


def _d2(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    return _d1(S, K, r, sigma, T, q) - sigma * math.sqrt(T)


def black_scholes(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> Tuple[float, float]:
    """
    Return (call_price, put_price) for a European option using Black-Scholes.

    Handles edge-cases:
      - If T <= 0: returns intrinsic payoffs (option at expiry).
      - If sigma <= 0: treats volatility as zero and returns discounted intrinsic
        (deterministic forward payoff).
    """
    # validate
    if S <= 0 or K <= 0:
        raise ValueError("S and K must be positive numbers")

    # At expiry: option value equals payoff
    if T <= 0:
        call = max(S - K, 0.0)
        put = max(K - S, 0.0)
        return call, put

    # Zero volatility -> deterministic forward payoff (discounted)
    if sigma <= 0:
        forward_spot = S * math.exp(-q * T)
        discounted_strike = K * math.exp(-r * T)
        call = max(forward_spot - discounted_strike, 0.0)
        put = max(discounted_strike - forward_spot, 0.0)
        return call, put

    D1 = _d1(S, K, r, sigma, T, q)
    D2 = D1 - sigma * math.sqrt(T)

    call = S * math.exp(-q * T) * _Phi(D1) - K * math.exp(-r * T) * _Phi(D2)
    put = K * math.exp(-r * T) * _Phi(-D2) - S * math.exp(-q * T) * _Phi(-D1)

    return call, put


# quick demo when run directly
if __name__ == "__main__":
    S = 100.0
    K = 100.0
    r = 0.05
    sigma = 0.2
    T = 1.0
    call_price, put_price = black_scholes(S, K, r, sigma, T)
    print(f"Call: {call_price:.6f}, Put: {put_price:.6f}")
