# 3_4_KTB_rates.py

# # -*- coding: utf-8 -*-
# # python2.7
# 
# """
#     Compute temporal earathquake rate change for KTB fluid injection experiment 
# """
# 
# import numpy as np
# import matplotlib.pyplot as plt
# 
# # =============================================================================
# #                                   Fct. def
# # =============================================================================
# 
# def comp_rate(a_t, k):
#     """
#     - Compute rate change for time vector a_t
#     :input
#         a_t - time vector
#         k - sample window - controls smoothness
#     
#     :output a_bin, a_rate
#     
#     """
#     
#     aS = np.arange(0, a_t.shape[0]-k, 1)
#     a_bin = np.zeros(aS.shape[0])
#     a_rate = np.zeros(aS.shape[0])
#     iS = 0
#     for s_step in aS:
#         i1, i2 = s_step, s_step+k
#         a_rate[iS] = k/(a_t[i2] - a_t[i1])
#         a_bin[iS] = 0.5*(a_t[i1] + a_t[i2])
#         iS += 1
#     return a_bin, a_rate
# 
# 
# # =============================================================================
# #                             Params and files
# # =============================================================================
# 
# file_inj = 'E:/ASTR_119/Week_3/KTB_inject.txt'
# file_eq = 'E:/ASTR_119/Week_3/KTB_mag.txt'
# 
# # Sample window
# k_win = 10
# 
# t0 = float() # Starting time for plotting
# aT_eq = np.array([]) # Timing of the earthquakes
# aMag = np.array([])
# 
# aT_inj = np.array([])
# aV = np.array([])
# 
# # =============================================================================
# #                       Load data and comp rates
# # =============================================================================
# 
# mData = np.loadtxt(file_eq).T
# aT_eq = mData[0]
# aMag = mData[1]
# 
# mData = np.loadtxt(file_inj).T
# aT_inj = mData[3]
# aV = mData[4]
# 
# sel = aV > 0
# aV = aV[sel]
# aT_inj = aT_inj[sel]
# 
# # Shift time vectors and change ot hr
# 
# t0 =  aT_inj[0]
# aT_inj -= t0
# aT_eq -= t0
# aT_inj = aT_inj/3600
# aT_eq = aT_eq/3600
# 
# # Test plot of magnitudes
# 
# plt.figure()
# ax1 = plt.subplot(211)
# ax1.plot(aT_inj, aV, 'b-')
# ax1.set_ylabel('Cumul. Inj. Rate [m3]')
# ax2 = plt.subplot(212)
# ax2.plot(aT_eq, aMag, 'r-')
# twinx2.plot(sorted(aT_eq), np.cumsum(np.ones(aT_eq.shape[0])))
# ax2.set_xlim(ax1.get_xlim())
# ax2.set_xlabel('Time [hr]')
# ax2.set_ylabel('Eq. Rate [eV/hr]')
# plt.plot(aT_eq, aMag, 'ko')
# plt.show()
# 
# # Compute eq rates
# 
# a_tbin, a_rate = comp_rate(aT_eq, k_win)
# 
# # =============================================================================
# #                                  Plots
# # =============================================================================
# 
# =============================================================================


# 3_5_gloabl_earthquakes.py

