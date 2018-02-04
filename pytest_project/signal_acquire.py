# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:17:24 2018

@author: Synapticon
"""
import math
import numpy as np
import matplotlib.pyplot as plt


# it could be analog or digital input
#channel = ["AIN0"]
channel = ["FIO7"]


numScans=6000  # number of samples to acquire 
scanRate=100e3  # this is maximum Sampling frequency of LabJack


numChannels = len(channel)
aScanList = ljm.namesToAddresses(numChannels, channel)[0]   #returns (aAddresses, aDataTypes)
aData=ljm.streamBurst(handle, numChannels, aScanList, scanRate, numScans)[1]

A=aData
A = A-np.mean(A)
n=len(A)

sampling_freq_of_DAC = 100e3 #max smapling freq=100kHz
#f = (-n/2:n/2-1)./(n/2)*sampling_freq_of_DAC/2

A_f = np.abs(np.real(np.fft.fft(A)))  # performing FFT on the data acquired, saving only real-absolute values
A_f_trunk = A_f[1: int(n/2)] # truncating the mirrored data fromt FFT

threshold = np.max(A_f_trunk)-5  # threshold of where to search for the frequency peaks 

freq_peak_index = np.where(A_f_trunk>threshold)[0]  # boolean comparison, finding indices
freq_of_sig = freq_peak_index[0]/n*sampling_freq_of_DAC 

print('Frequency of the signal: %.2f kHz\n' %(freq_of_sig/1000))
#print('Frequency of the signal=', freq_of_sig/1000, 'kHz') 

plt.plot(A_f_trunk,'r-')
plt.axhline(y=threshold, xmin=0, xmax=n, color='c') #horizontal axis line
plt.show()



