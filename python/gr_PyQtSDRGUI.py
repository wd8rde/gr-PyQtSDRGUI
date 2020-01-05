#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, filter
from gnuradio import blocks
import sys
import numpy

try:
    from gnuradio import qtgui
    #from PyQt5 import Qt, QtGui, QtCore, QtWidgets
    from PyQt5 import Qt
except ImportError:
    sys.stderr.write("Error: Program requires PyQt4 and gr-qtgui.\n")
    sys.exit(1)

from OpenSdrGuiLogic import *

class PyQtSDRGUI(Qt.QWidget,OpenSdrGuiLogic):
    """
    docstring for block PyQtSdrGui
    """
    on_band = Qt.pyqtSignal(int)
    on_bandwidth_high = Qt.pyqtSignal(int)
    on_bandwidth_low = Qt.pyqtSignal(int)
    on_vfo_frequency = Qt.pyqtSignal(int)
    on_lo_frequency = Qt.pyqtSignal(int)
    on_modulation_mode = Qt.pyqtSignal(int)
    on_volume_changed = Qt.pyqtSignal(int)
    on_rfatten_toggled = Qt.pyqtSignal(bool)
    on_rfpreamp_toggled = Qt.pyqtSignal(bool)
    on_audiopreamp_toggled = Qt.pyqtSignal(bool)

    def __init__(self,
                 parent=None,
                 itu_region='itu-region2',
                 band_id=1,
                 bandwidth_low=200,
                 bandwidth_high=2700,
                 volume=25,
                 vfo_freq=7001000,
                 lo_freq=7000000,
                 sample_rate=44100):

        Qt.QWidget.__init__(self, parent)
        OpenSdrGuiLogic.__init__(self,
                                 itu_region=itu_region,
                                 band_id=band_id,
                                 bandwidth_low=bandwidth_low,
                                 bandwidth_high=bandwidth_high,
                                 vfo_freq=vfo_freq,
                                 lo_freq=lo_freq,
                                 sample_rate=sample_rate)

        OpenSdrGuiLogic.setupUi(self,self)

    def set_itu_region(self, itu_region):
        pass

    def set_band_id(self, band_id):
        pass

    def set_bandwidth_low(self, bandwidth_low):
        pass

    def set_bandwidth_high(self, bandwidth_high):
        pass

    def set_volume(self, volume):
        pass

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate #defined in OpenSdrGuiLogic.py

    def on_band_event(self, band_id):
        print("PyQtSdrGui 'on_band' %d"%band_id)
        self.on_band.emit(int(band_id))

    def on_bandwidth_high_event(self, bandwidth):
        print("PyQtSdrGui 'on_band_high' %d"%bandwidth)
        self.on_bandwidth_high.emit(int(bandwidth))

    def on_bandwidth_low_event(self, bandwidth):
        print("PyQtSdrGui 'on_band_low' %d"%bandwidth)
        self.on_bandwidth_low.emit(int(bandwidth))

    def on_vfo_frequency_event(self, freq):
        print("PyQtSdrGui 'on_vfo_frequency' %d"%(int(freq)))
        self.on_vfo_frequency.emit(int(freq))

    def on_lo_frequency_event(self, freq):
        print("PyQtSdrGui 'on_lo_frequency' %d"%(int(freq)))
        self.on_lo_frequency.emit(int(freq))

    def on_modulation_mode_event(self,mode):
        mode_map = {'AM':0,'SAM':1,'DSB':2,'LSB':3,'USB':4,'CWL':5,'CWU':6,'FMN':7,'SPEC':8,'DIGL':9,'DIGL':10,'DIGU':11,'DRM':12 }
        if(mode in mode_map):
            mode_idx = mode_map[mode]
            print("PyQtSdrGui 'on_modulation_mode_event' %s, emitting %d"%(str(mode),int(mode_idx)))
            self.on_modulation_mode.emit(int(mode_idx))
        else:
            print("PyQtSdrGui 'on_modulation_mode_event' %s not in mode_map"%(str(mode)))

    def on_volume_changed_event(self,percent):
        print('on_volume_changed',percent)
        self.on_volume_changed.emit(int(percent))
        pass

    def on_rfatten_toggled_event(self, toggled):
        print('on_rfatten_toggled',toggled)
        self.on_rfatten_toggled.emit((toggled))

    def on_rfpreamp_toggled_event(self, toggled):
        print('on_rfpreamp_toggled',toggled)
        self.on_rfpreamp_toggled.emit((toggled))

    def on_audiopreamp_toggled_event(self, toggled):
        print('on_audiopreamp_toggled',toggled)
        self.on_audiopreamp_toggled.emit((toggled))

class my_top_block(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
        self.main_box = PyQtSDRGUI()
        self.main_box.show()

def main():
    qapp = Qt.QApplication(sys.argv)
    tb = my_top_block()
    tb.start()
    qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
