# heatmap_pnl.py

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bs_model import black_scholes

def generate_pnl_heatmaps(S_min, S_max, sigma_min, sigma_max, K, r, T, purchase_price_call, purchase_price_put, steps=50):
    """
    Generate and display PnL heatmaps for Call and Put options.
    
    S_min, S_max       : Range for spot prices
    sigma_min, sigma_max : Range for volatilities
    K, r, T            : Strike price, risk-free rate, time to expiry
    purchase_price_call: Price paid to buy the call option
    purchase_price_put : Price paid to buy the put option
    steps              : Resolution of the heatmap grid
    """
    
    spot_prices = np.linspace(S_min, S_max, steps)
    volatilities = np.linspace(sigma_min, sigma_max, steps)

    pnl_call = np.zeros((steps, steps))
    pnl_put = np.zeros((steps, steps))

    for i, S in enumerate(spot_prices):
        for j, sigma in enumerate(volatilities):
            call_price, put_price = black_scholes(S, K, r, sigma, T)
            pnl_call[j, i] = call_price - purchase_price_call
            pnl_put[j, i] = put_price - purchase_price_put

    # Plot Call PnL heatmap
    plt.figure(figsize=(12, 5))
    sns.heatmap(pnl_call, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2), cmap="RdYlGn", center=0)
    plt.title("Call Option PnL Heatmap")
    plt.xlabel("Spot Price")
    plt.ylabel("Volatility")
    plt.show()

    # Plot Put PnL heatmap
    plt.figure(figsize=(12, 5))
    sns.heatmap(pnl_put, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2), cmap="RdYlGn", center=0)
    plt.title("Put Option PnL Heatmap")
    plt.xlabel("Spot Price")
    plt.ylabel("Volatility")
    plt.show()


if __name__ == "__main__":
    # Example inputs
    S_min = 80
    S_max = 120
    sigma_min = 0.1
    sigma_max = 0.5
    K = float(input("Enter strike price:"))
    r = float(input("Enter risk free rate of return:"))
    T = float(input("ENTER time to maturity:"))
    S = float(input("Enter Spot price: "))
    vol = float(input("Enter volatility: "))

    purchase_price_call = float(input("Enter current market value of call:"))
    purchase_price_put = float(input("Enter current market value of put:"))
    call_p, put_p = black_scholes(S,K,r,vol, T)

    print("Call Price ", call_p)
    print("Put Price: ", put_p)


    generate_pnl_heatmaps(S_min, S_max, sigma_min, sigma_max, K, r, T, purchase_price_call, purchase_price_put)
