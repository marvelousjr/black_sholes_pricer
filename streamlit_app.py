import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bs_model import black_scholes

st.set_page_config(page_title="Black-Scholes Option PnL Heatmap", layout="wide")

st.title("📈 Black-Scholes Option PnL Heatmaps & Valuation")

# ---- Sidebar Inputs ----
st.sidebar.header("Option Parameters")

S0 = st.sidebar.number_input("Current Spot Price (S₀)", min_value=1.0, value=100.0, step=1.0)
K = st.sidebar.number_input("Strike Price (K)", min_value=1.0, value=100.0, step=1.0)
r = st.sidebar.number_input("Risk-free Rate (r) in %", min_value=0.0, value=5.0, step=0.1) / 100
T = st.sidebar.number_input("Time to Maturity (years)", min_value=0.01, value=1.0, step=0.01)
purchase_price_call = st.sidebar.number_input("Purchase Price for Call Option", min_value=0.0, value=10.0, step=0.1)
purchase_price_put = st.sidebar.number_input("Purchase Price for Put Option", min_value=0.0, value=10.0, step=0.1)

st.sidebar.header("Heatmap Ranges")
S_min = st.sidebar.number_input("Min Spot Price", min_value=1.0, value=80.0, step=1.0)
S_max = st.sidebar.number_input("Max Spot Price", min_value=1.0, value=120.0, step=1.0)
sigma_min = st.sidebar.number_input("Min Volatility (%)", min_value=1.0, value=10.0, step=1.0) / 100
sigma_max = st.sidebar.number_input("Max Volatility (%)", min_value=1.0, value=50.0, step=1.0) / 100

S_steps = st.sidebar.slider("Spot Steps", min_value=5, max_value=50, value=20)
sigma_steps = st.sidebar.slider("Volatility Steps", min_value=5, max_value=50, value=20)

# ---- Current Option Pricing ----
current_call_price, current_put_price = black_scholes(S0, K, r, (sigma_min + sigma_max) / 2, T)

# Determine undervalued/overvalued
call_status = "Undervalued ✅ (usually BUY)" if current_call_price > purchase_price_call else "Overvalued ❌ (usually SELL)"
put_status = "Undervalued ✅ (usually BUY)" if current_put_price > purchase_price_put else "Overvalued ❌ (usually SELL)"

# Display option prices at the top
col_price1, col_price2 = st.columns(2)
with col_price1:
    st.metric(label="Current Call Option Price", value=f"${current_call_price:.2f}", delta=call_status)
with col_price2:
    st.metric(label="Current Put Option Price", value=f"${current_put_price:.2f}", delta=put_status)

st.markdown("---")

# ---- Generate Ranges for Heatmap ----
spot_range = np.linspace(S_min, S_max, S_steps)
sigma_range = np.linspace(sigma_min, sigma_max, sigma_steps)

call_pnl = np.zeros((len(sigma_range), len(spot_range)))
put_pnl = np.zeros((len(sigma_range), len(spot_range)))

for i, sigma in enumerate(sigma_range):
    for j, spot in enumerate(spot_range):
        call_price, put_price = black_scholes(spot, K, r, sigma, T)
        call_pnl[i, j] = call_price - purchase_price_call
        put_pnl[i, j] = put_price - purchase_price_put

# ---- Plot Call Heatmap ----
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.heatmap(call_pnl, xticklabels=np.round(spot_range, 2), yticklabels=np.round(sigma_range * 100, 1),
            cmap="RdYlGn", center=0, ax=ax1)
ax1.set_xlabel("Spot Price")
ax1.set_ylabel("Volatility (%)")
ax1.set_title("Call Option PnL Heatmap")

# ---- Plot Put Heatmap ----
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.heatmap(put_pnl, xticklabels=np.round(spot_range, 2), yticklabels=np.round(sigma_range * 100, 1),
            cmap="RdYlGn", center=0, ax=ax2)
ax2.set_xlabel("Spot Price")
ax2.set_ylabel("Volatility (%)")
ax2.set_title("Put Option PnL Heatmap")

# ---- Display Heatmaps Side-by-Side ----
col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig1)
with col2:
    st.pyplot(fig2)

st.caption("Green = Profit, Red = Loss. PnL = Option Price - Purchase Price.")
