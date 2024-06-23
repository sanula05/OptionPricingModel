# Binomial Tree model
# Reqirements: Create two underlying functions(one for call and one for put options)
# that calculate the price of the option using the binomial tree model.
# Notes from reaserch: 
# Arbitage - risk free profit(type 1 and 2).
# type 1: zero invesment and chance to gain profit
#   value_0 = 0 , P(value_t >= 0) = 1 , P(value_t > 0) > 0 
# type 2: recive credint and have no risk of loss
#   value_0 < 0 , P(value_t >= 0) = 1 , 
# Law of one price -> for two profolios (A,B), P(V_A = V_B) = 1 Then V_A_0 = V_B_0
# One period binomial model :
#   S_0 = Stock price at T = 0
#   Two probabilites S_up(u) and S_down(d)
#   u & d influence volatility.
#   S_up = u * S_0 & S_down = d * S_0 , The time step i T = 1  


# Monte-Carlo simulation

# Black-Scholes-Merton model
