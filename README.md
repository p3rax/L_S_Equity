# Option Pricing and Delta-Neutral Hedging

## Introduction
This document provides an overview of the theoretical pricing of European call and put options using the Black-Scholes Model and outlines a Delta-Neutral Hedging Strategy for managing these positions.

---

## Theoretical Pricing Using Black-Scholes
Based on the following parameters:
- **Current stock price (S)**: $120
- **Strike price (K)**: $125
- **Time to maturity (T)**: 6 months (0.5 years)
- **Risk-free rate (r)**: 4% annually
- **Volatility (σ)**: 20% annually

The calculated theoretical prices are:
- **Call option price**: $5.65 per option
- **Put option price**: $8.17 per option

For a position of 10 options:
- **Total call position value**: (10 × $5.65) = $56.50
- **Total put position value**: (10 × $8.17) = $81.70

---

## Delta-Neutral Hedging Strategy
Delta-neutral hedging involves adjusting the position in the underlying asset to offset the sensitivity (Δ) of the option position to small price changes in the stock. Next four strategies for different position:

1. **Long Call Position**:
   - **Delta of a single call**: +0.4695
   - **Total delta for 10 calls**: +4.70
   - **Hedging action**: Short 4.70 shares of the underlying asset to neutralize the delta.

2. **Long Put Position**:
   - **Delta of a single put**: -0.5305
   - **Total delta for 10 puts**: -5.305
   - **Hedging action**: Buy 5.305 shares of the underlying asset to neutralize the delta.

3. **Short Call Position**:
   - The total delta is negative. To hedge, buy shares of the underlying asset to offset the negative delta.

4. **Short Put Position**:
   - The total delta is positive. To hedge, short shares of the underlying asset to offset the positive delta.

---

## Conclusions
However, in real-world applications, the following factors must be considered:
- **Transaction costs**
- **Liquidity**
- **Volatility changes**
- **Hedging adjustments**

Understanding these principles is fundamental in order to better manage risk and optimize our positions in the options market.
