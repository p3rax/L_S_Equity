import math
from scipy.stats import norm

# S (float) = current stock price
# K (float) = strike price
# T (float) = time to maturity
# r (float) = risk-free rate
# sigma (float) = volatility
# option_type (str) = "call" o "put"
# option_count (int): number of options in the position

# Black-Scholes Model
def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    if option_type == "call":
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return option_price

# Delta-Neutral Hedging Strategy
def option_delta(S, K, T, r, sigma, option_type="call"):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    
    if option_type == "call":
        return norm.cdf(d1)
    elif option_type == "put":
        return norm.cdf(d1) - 1

# Parameters
S = 120 # current stock price ($120)
K = 125 # strike price ($125)
T = 0.5 # time to maturity (6 months = 0.5 years)
r = 0.04 # risk-free rate (4%)
sigma = 0.2 # volatility (20%)
num_options = 10 # number of option in the position (assumed)

# Price Calculation
call_price = black_scholes(S, K, T, r, sigma, option_type="call")
put_price = black_scholes(S, K, T, r, sigma, option_type="put")

# Delta Calculation
call_delta = option_delta(S, K, T, r, sigma, option_type="call")
put_delta = option_delta(S, K, T, r, sigma, option_type="put")

# Delta Coverage Calculation
hedge_call = -call_delta * num_options
hedge_put = -put_delta * num_options  

# Results
print(f"Theorical call option price: {call_price:.2f} USD")
print(f"Theorical put option price: {put_price:.2f} USD")
print(f"Delta-neutral hedging strategy for call options:: Short {hedge_call:.2f} shares of stock")
print(f"Delta-neutral hedging strategy for put options:: Long {hedge_put:.2f} shares of stock")