# -*- coding: utf-8 -*-
#python2.7

# =============================================================================
#                              Function cross
# =============================================================================

"""

    Determine the crossover point between two functions
    f(t) and g(t)
    (1) - as for loop
    (2) - vectorized problem using numpy

"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                                Parameters
# =============================================================================

tmin, tmax = -10, 10
iN         = 1000
f_dt       = float(tmax-tmin)/(iN-1)

#fct parameters
t0  = 2.5
c   = 1.1
A   = 9
eps = 0.1

# =============================================================================
#                               Function def
# =============================================================================

def f_t(t, c, t0):
    return c*(t-t0)**2

def g_t(t,A):
    return A*t+t0

# =============================================================================
#                          Find cross-over point
# =============================================================================

##A## for loop

f_curr_t = tmin # f refers to float, curr means current, and t is the variable

for i in range( iN):
    f_curr_t += f_dt
    f_curr_f_t = f_t( f_curr_t, c, t0)
    f_curr_g_t = g_t( f_curr_t, A)
    #print f_curr_t, f_curr_f_t, f_curr_g_t
    #Function value comparison
    if abs( f_curr_f_t - f_curr_g_t) < eps:
        print( 'Cross over point at t=%.2f, f(t)=%.2f, g(t)=%.2f'%( f_curr_t, f_curr_f_t, f_curr_g_t))

##B## Vectorized solution

a_t = np.linspace(tmin, tmax, iN)
# Evaluate functions
a_ft = f_t( a_t, c, t0)
a_gt = g_t( a_t, A)
# Find cross over point
sel = abs( a_ft - a_gt) < eps
print 'Cross over points', a_t[sel], a_ft[sel], a_gt[sel]

# =============================================================================
#                               Plot functions
# =============================================================================

plt.plot( a_t, a_ft, 'ro', ms = 2)
plt.plot( a_t, a_gt, 'go', ms = 2)
plt.show()


# =============================================================================
#                               Next thing
# =============================================================================

"""

    1) - Create synthetic well pressure time series
    2) - Compute the mean in each well
    3) - Compute stdev in each well

"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                               Parameters
# =============================================================================

iWell = 10
iMeas = 1000

# =============================================================================
#                           Create synthetic
# =============================================================================

a_mu_syn = np.random.random_integers( 20, 40, iWell)
a_std_syn = np.random.random_integers( 1, 10, iWell)*.1

m_Data = np.array( [])
for i in range( iWell):
    if i == 0:
        m_Data = a_mu_syn[i] + a_std_syn[i]*np.random.randn( iMeas)
    else:
        m_Data = np.vstack( m_Data, a_mu_syn[i] + a_std_syn[i]*np.random.randn( iMeas))

print( m_Data.mean( ))
print( m_Data.mean( ))

# =============================================================================
# print np.ones( iMeas, dtype = float)
# print np.ones( iMeas, dtype = float).reshape( iMeas, 1)
# =============================================================================

# =============================================================================
#                               Statistics
# =============================================================================

a_mean = np.dot( m_Data, np.ones( iMeas, dtype = float).reshape(iMeas, 1))/iMeas
# Test code performance
print( 'Syn results', np.round( a_mu_syn, 2))
print( 'Computed means', np.round( a_mean.flatten(),2))






# =============================================================================
#                           System of Equations
# =============================================================================

import numpy as np

# Coefficient matrix A

mA = np.array( [[3, 1], [1, 2]])

# Solution vector
a_b = np.array([ 9, 8])

# Solve for A^-1 (dot) b

a_x = np.dot( np.linalg.inv(mA), a_b)
print(a_x)
a_x2 = np.linalg.solve( mA, a_b)
print( a_x2)