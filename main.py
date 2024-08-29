import numpy as np
import scipy as sp

class option_pricing_model:
  def __init__(self, S_0, K, T, r,N, sigma, type):
    self.S_0 = 100            #Inital stock price
    self.K = 100              #Strike price
    self.T = 1                #Time to maturity
    self.r = 0.05             #Risk-free rate
    self.N = 100              #Number of time steps
    self.sigma = 0.2          #Volatility
    self.type = "Call"        #Call or put
  
# Binomial Tree Model:
  def binomial_asset_pricing(S_0,K,T,r,N,sigma,type):
    dt = T/N
    
    pass
  
# Black-Scholes Merton Model:
  def black_scholes_pricing(S_0,K,T,r,N,sigma,type):
    d1 = (np.log(S_0 / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S_0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    price_0 = 0
    if type == "Call":
       price_0 = S_0 * sp.stats.norm.cdf(d1) - K * np.exp(-r * T) * sp.stats.norm.cdf(d2)  
    elif type == "Put" :
       price_0 = K * np.exp(-r * T) * sp.stats.norm.cdf(-d2) - S_0 * sp.stats.norm.cdf(-d1)
    
    return(price_0)
  


# Monte-Carlo simulation:
def Monte_Carlo(S_0, K, T, r, N, sigma, type, no):
   np.ranon.seed(42)
   dt = T/N
   S_t = S_0*np.exp((r-o.5*sigma**2)*dt+sigma*np.sqrt(dt)*np.random.randn(no))

   if type == "Call":
      payoff = np.maximum(S_t - K, 0)
   elif type == "Put":
      payoff = np.maximum(K - S_t, 0)
   price = np.exp(-r *T) *  np.mean(payoff)
   return(price)

#Cox-Ross-Rubinstein Model:


def black_scholes_pricing(S_0,K,T,r,N,sigma,type):
  d1 = (np.log(S_0 / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
  d2 = (np.log(S_0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))
  price_0 = 0
  if type == "Call":
     price_0 = S_0 * sp.stats.norm.cdf(d1) - K * np.exp(-r * T) * sp.stats.norm.cdf(d2)  
  elif type == "Put" :
     price_0 = K * np.exp(-r * T) * sp.stats.norm.cdf(-d2) - S_0 * sp.stats.norm.cdf(-d1)

  return(price_0)

print(black_scholes_pricing(100,100,1,0.05,100,0.2,"Put"))