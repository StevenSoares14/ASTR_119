# -*- coding: utf-8 -*-

# =============================================================================
# """
# 
#         - Detect planet size and brightness depth
# 
# """
# 
# import numpy as np
# import matplotlib.pyplot as plt
# 
# # =============================================================================
# #                           files and variables
# # =============================================================================
# 
# file_in = 'exoplanet_transit.csv'
# 
# r_earth = 6371  # [km]
# r_s = 8e4 # [km]
# Np = 3
# 
# # =============================================================================
# #                               Load data
# # =============================================================================
# 
# mData = np.loadtxt(file_in, delimiter = ',', skiprows = 1).T
# N = len(mData[0])
# lenPer = int(float(N)/Np)
# # Compute difference between subsequent samples
# aDiff = mData[1][1::] - mData[1][0::-1]
# 
# # =============================================================================
# #                       Compute depth of transit
# # =============================================================================
# 
# aDepth = np.zeros(Np)
# for i in range(Np):
#     # Create an index vector
#     aID = np.arange(lenPer) + lenPer*i
#     print(aID)
#     selMin = aDiff[aID] == aDiff[aID].min()
#     selMax = aDiff[aID] == aDiff[aID].max()
#     
#     iID_min = aID[selMin][0]
#     iID_max = aID[selMax][0]
#     
#     # Compute mean depth of transit (for each period)
#     aDepth[1] = 1 - mData[1, iID_min:iID_max].mean()
# 
#     plt.figure(1)
#     plt.subplot(111)
#     plt.plot(mData[0],mData[1], 'ko', ms = 10)
#     plt.plot(mData[0][aID],mData[1][aID], 'ro', ms = 10)
#     #plt.xlabel('Transit Time [hr]')
#     plt.ylabel('Brightness')
#     plt.show()
#     plt.pause(1)
# 
# # Compute size of planet
# aR_p = np.sqrt(aDepth)*r_s
# print(aR_p)
# print('Size relative to Earth', aR_p/r_earth)
# 
# # =============================================================================
# #                               Plotting
# # =============================================================================
# 
# plt.figure(2)
# plt.subplot(211)
# plt.plot(mData[0],mData[1], 'ko', ms = 10)
# #plt.xlabel('Transit Time [hr]')
# plt.ylabel('Brightness')
# 
# plt.subplot(212)
# plt.plot(mData[0][0:-1], aDiff, 'ro', ms = 10)
# plt.xlabel('Transit time [hr]')
# plt.ylabel('Brightness difference')
# plt.show()
# =============================================================================



import numpy as np
import os

# =============================================================================
#                           Creating ex data
# =============================================================================

file_out = 'dataIO_ex.txt'
N = 10
aX = np.arange(N)
aY = aX**2

# =============================================================================
#                     Methods to load and save data
# =============================================================================

print(os.getcwd())
np.savetxt(file_out, np.array([aX, aY]).T, #fmt = '%4.0f%4.0f', 
           header = 'X  X^2')

mData = np.loadtxt(file_out).T
print(mData)

# Read file line by line
with open(file_out, 'r') as file_obj:
    file_obj.next()
    for line in file_obj:
        lStr = line.split(' ')
        print(lStr)
        for my_str in lStr:
            print (int( float( my_str)))
            
# Read and write binary
            
import scipy.io
print(file_out)
print (file_out.replace('txt', 'mat'))
scipy.io.savemat(file_out.replace('txt', 'mat'), { 'X' : aX, 'Y': aY}, do_compression = True)

dicData = scipy.io.loadmat(file_out.replace('txt','mat'))
print(dicData['X'])
print(dicData['Y'])