# -*- coding: utf-8 -*-

# ============================================================================= 
#  Modified version of 1_1_rate of_return:
# ============================================================================= 

#!python2.7

"""
Write a script that computes the annual rate of return and the absolute return
 on an investment of $1,000 at 10% over 30 years
 - lessons in compounding interest
"""
#===================================================================================
#                                params
#===================================================================================

# Get input from user

f_iniInvest = float(raw_input('What are your initial savings? '))
f_interest  = float(raw_input('Specify interest rate: '))
f_income    = float(raw_input('What is your desired monthly income during retiremnt? '))
i_Years     = 30


#===================================================================================
#                                calculation
#===================================================================================

def annual_savings( f_money0, f_int, N, verbose = False):
    """
    - compute annual return on toal savings - f_money0
    :input
        f_money0  - total savings in year 0
        f_int     - interest rate
        N         - total years
    :return float() - savings in year N
    """
    currSave = f_money0
    for i in range( N):
        growth    = currSave*.1
        currSave += growth
        if verbose == True:
            print( 'Year: %i, abs savings: %8.2f, rate of ini.: %4.3f'%( i+1, currSave, (growth)/f_int))
    return currSave

def retirement( f_money0, f_int, f_income, verbose = False):
    """
    - compute annual return on toal savings - f_money0
    :input
        f_money0  - total savings in year 0
        f_int     - interest rate
        f_income  - desired retirement monthly earnings
    :return float() - savings in year N
    """
    N = 1000
    currSave = f_money0
    for i in range( N):
        growth    = currSave*.1
        currSave += growth
        if growth >= (f_income*12):
            retire_year = i
            break
        return retire_year

totSav1 = annual_savings( f_iniInvest, f_interest, i_Years, verbose = False)
 
# Here is the easier formula to get total savings in year n
totSav2 = (1 + f_interest)**i_Years*f_iniInvest
print( 'total savings after {y:.0f} years: {x:.2f}'.format( x=totSav2, y=i_Years), round( totSav1, 2))

# 2. Computation: retirement age 
print('Retirement age: ' + retirement(f_iniInvest,f_interest,f_income))

# =============================================================================


#=============================================================================
#In class assignnment 2
#=============================================================================

"""
While loop, find max height
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 5 #m/s
g = 9.81 # m/s^2
n = 2000 # time steps
a_t = np.linspace(0,1,n) # time (s)

#Computations
y = v0*a_t - 0.5*g*a_t**2

# Find max height in while loop

i = 1

# y[-1] is the last entry in the array, so set i = 1 instead of 0 to avoid this

while y[i] > y[i-1]:
    largest_height = y[i]
    i += 1
    
print('Max height: %10.2f'%(largest_height))

plt.plot(a_t, y)
plt.xlabel('a_t')
plt.ylabel('y')
plt.grid()
plt.show()