# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:57:08 2017

@author: Synapticon
"""

from labjack import ljm
import numpy as np

ANALOG_INPUT_3 = 'AIN3'
#ANALOG_SIGNAL_OUT_0 = 'DAC0'
#ANALOG_SIGNAL_OUT_1 = 'DAC1'

class Daq:
    def __init__(self):
        self.handle = ljm.openS("T7", "USB", "470015671")
#		self.handle = ljm.openS("T7", "ETHERNET", "470015671")
        self.info = ljm.getHandleInfo(self.handle);
    
    def close(self):
        ljm.close(self.handle)
        
    def measure_average_voltage_from_stream(self, channel):
        aScanList = ljm.namesToAddresses(1, [channel])[0]   #returns (aAddresses, aDataTypes)
        numScans=20
        scanRate=float(2000)
        
        aData=ljm.streamBurst(self.handle, 1, aScanList, scanRate, numScans)[1]
        return np.mean(aData)
    
""" not tested
    def generate_dc_waveform(self, channel, output_voltage):
        ljm.eWriteName(self.handle, channel, output_voltage)
        output = ljm.eReadName(self.handle, channel)
        print(\n %s set to: %.3f V" % (channel, output))
        
#    def generate_analog_waveform(self, channel):
"""