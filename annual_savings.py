# -*- coding: utf-8 -*-

# anaconda2/python 2.7

"""
Compute annual dollar amount on savings invested at float_Interest over int_Years years
Variables:
        int_Years = durations of investment
        flt_Interest = interest rates
        flt_iniInvest = initial investment
"""

#import numpy

#============================================================================
#                           Define Variables
#============================================================================

int_Years = 30
flt_Interest = 0.1
flt_iniInvest = 1e4

#============================================================================
#                        Do computation - Savings
#============================================================================

def annual_return( flt_iniInvest, flt_Interest, int_Years):
    """
    Computing annual savings
    :input
        Variables:    
        int_Years = durations of investment
        flt_Interest = interest rates
        flt_iniInvest = initial investment
    :output
        Savings in last year ( int_Years)
    """
    currInvest = flt_iniInvest
    for i in range( int_Years-1):
        flt_Growth = currInvest*flt_Interest
        print( 'Year', i+1, 'savings', currInvest, 'interest per year', flt_Growth)
        currInvest += flt_Growth
        return currInvest

# Add a function call
        
print(annual_return( flt_iniInvest, flt_Interest, int_Years))