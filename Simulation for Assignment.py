# -*- coding: utf-8 -*-
"""
This simualation is based on Python 3, you may have to install a Python 3 
environment to run it. 
"""

import numpy as np
from sympy import *
import matplotlib.pyplot as plt

# Parameters for choosing
t = 12
t_before = 2
t_persistent = 3
y_bar = 100
pi_star = 2
alpha = 1
rho = 2
phi = 0.25
theta_pi = 0.5
theta_y = 0.5
v_t = 0
e_t = 0
data_pi = list(range(t))
data_y = list(range(t))
pi_t = pi_star

# Before the shocks
for i in range(t_before):
    e_t = 0
    pi_1 = pi_t
    pi = Symbol('pi')
    y = Symbol('y')
    f1 = pi-(pi_1+phi*(y-y_bar)+v_t)
    f2 =  y-(y_bar - ((alpha*theta_pi)/(1+alpha*theta_y))*(pi-pi_star)+(1/(1+alpha*theta_y))*e_t)
    pi_t = solve([f1,f2],[pi, y])[pi] 
    y_t = solve([f1,f2],[pi, y])[y]
    data_pi[i] = pi_t
    data_y[i] = y_t
    print(data_pi)

# Two persistent shocks
t_shock = list(range(t))[t_before:t_before+t_persistent]  
for i in t_shock:
    y_bar = 70  # The shocked natural output level
    e_t = -10   # Demand shock
    v_t =  1 # Supply shock
    pi_star = 2 # Inflation target
    theta_pi = 0.5
    pi_1 = pi_t
    pi = Symbol('pi')
    y = Symbol('y')
    f1 = pi-(pi_1+phi*(y-y_bar)+v_t)
    f2 =  y-(y_bar - ((alpha*theta_pi)/(1+alpha*theta_y))*(pi-pi_star)+(1/(1+alpha*theta_y))*e_t)
    pi_t = solve([f1,f2],[pi, y])[pi] 
    y_t = solve([f1,f2],[pi, y])[y] 
    data_pi[i] = pi_t
    data_y[i] = y_t
    print(data_pi)

# Recovery after shocks    
t_after = list(range(t))[t_before+t_persistent:t]
for i in t_after:
    y_bar = 100
    e_t = 0
    v_t = 0
    pi_star = 2
    theta_pi = 0.5
    pi_1 = pi_t
    pi = Symbol('pi')
    y = Symbol('y')
    f1 = pi-(pi_1+phi*(y-y_bar)+v_t)
    f2 =  y-(y_bar - ((alpha*theta_pi)/(1+alpha*theta_y))*(pi-pi_star)+(1/(1+alpha*theta_y))*e_t)
    pi_t = solve([f1,f2],[pi, y])[pi] 
    y_t = solve([f1,f2],[pi, y])[y] 
    data_pi[i] = pi_t
    data_y[i] = y_t
    print(data_pi)
    print(data_y)

# Create an automatic x-axis for the following figure
date = list(range(t))
for i in range(t_before):
    date[i] = "t-"+str(-i+2)
date[t_before] = "t"

t_rest = list(range(t))[t_before:t] 
for i in range(t-t_before-1):
    date[i+t_before+1] = "t+"+str(i+1)

# Turn the list into Numpy arrays
npdata_pi = np.array(data_pi)
npdata_y = np.array(data_y)
npdata_date = np.array(date)

# Plot 2 Figures for Responses
plt.plot(npdata_date,npdata_y,color="red",linestyle="-")
plt.ylim(30, 108)
plt.ylabel("Output yt")
plt.show()

plt.plot(npdata_date,npdata_pi,color="#800080",linestyle="-")
plt.ylim(0,25)
plt.ylabel("Infaltion Pi_t")
plt.show()


