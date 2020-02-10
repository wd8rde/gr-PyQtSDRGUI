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
except ImportError:
    sys.stderr.write("Error: Program requires gr-qtgui.\n")
    sys.exit(1)

if('PyQt5' in sys.modules.keys()):
    print('using PyQt5')
    from PyQt5 import QtCore, QtGui, QtWidgets, uic
    from PyQt5.QtWidgets import QWidget
    from PyQt5.QtWidgets import QApplication
elif('PyQt4' in sys.modules.keys()):
    print('using PyQt5')
    from PyQt4 import Qt, QtCore, QtGui, uic
    from PyQt4.Qt import QWidget
    from PyQt4.Qt import QApplication
else:
    sys.stderr.write("Error: Program requires PyQt5, or PyQt4.\n")
    sys.exit(1)

from OpenSdrGuiLogic import OpenSdrGuiLogic

print('huh?',QWidget,OpenSdrGuiLogic)
class PyQtSDRGUI(QWidget,OpenSdrGuiLogic):
    """
    docstring for block PyQtSdrGui
    """
    on_band = QtCore.pyqtSignal(int)
    on_bandwidth_high = QtCore.pyqtSignal(int)
    on_bandwidth_low = QtCore.pyqtSignal(int)
    on_vfo_frequency = QtCore.pyqtSignal(int)
    on_lo_frequency = QtCore.pyqtSignal(int)
    on_modulation_mode = QtCore.pyqtSignal(str)
    on_volume_changed = QtCore.pyqtSignal(int)
    on_rf_gain_changed = QtCore.pyqtSignal(int)
    on_drive_changed = QtCore.pyqtSignal(int)
    on_mic_changed = QtCore.pyqtSignal(int)
    on_rfatten_toggled = QtCore.pyqtSignal(bool)
    on_rfpreamp_toggled = QtCore.pyqtSignal(bool)
    on_audiopreamp_toggled = QtCore.pyqtSignal(bool)
    on_vox_toggled = QtCore.pyqtSignal(bool)
    on_mute_toggled = QtCore.pyqtSignal(bool)

    def __init__(self,
                 parent=None,
                 itu_region='itu-region2',
                 band_id=1,
                 bandwidth_low=200,
                 bandwidth_high=2700,
                 volume=25,
                 rf_gain=100,
                 drive=0,
                 mic=60,
                 vfo_freq=7001000,
                 lo_freq=7000000,
                 sample_rate=44100,
                 modulation_mode=3):

        QWidget.__init__(self, parent)
        OpenSdrGuiLogic.__init__(self,
                                 itu_region=itu_region,
                                 band_id=band_id,
                                 bandwidth_low=bandwidth_low,
                                 bandwidth_high=bandwidth_high,
                                 volume=volume,
                                 rf_gain=rf_gain,
                                 drive=drive,
                                 mic=mic,
                                 vfo_freq=vfo_freq,
                                 lo_freq=lo_freq,
                                 sample_rate=sample_rate,
                                 modulation_mode=modulation_mode)

        OpenSdrGuiLogic.setupUi(self,self)

    def set_itu_region_cb(self, itu_region):
        self.itu_region = itu_region; #defined in OpenSdrGuiLogic.py

    def set_band_id_cb(self, band_id):
        self.set_band(band_id) #defined in OpenSdrGuiLogic.py

    def set_bandwidth_low_cb(self, bandwidth_low):
        self.current_bandwidth_low = bandwidth_low #defined in OpenSdrGuiLogic.py

    def set_bandwidth_high_cb(self, bandwidth_high):
        self.set_bandwidth_high(bandwidth_high) #defined in OpenSdrGuiLogic.py

    def set_volume_cb(self, volume):
        self.set_volume(volume) #defined in OpenSdrGuiLogic.py

    def set_rf_gain_cb(self, rf_gain):
        self.set_rf_gain(rf_gain) #defined in OpenSdrGuiLogic.py

    def set_drive_cb(self, rf_gain):
        self.set_drive(drive) #defined in OpenSdrGuiLogic.py

    def set_mic_cb(self, rf_gain):
        self.set_mic(mic) #defined in OpenSdrGuiLogic.py

    def set_sample_rate_cb(self, sample_rate):
        self.sample_rate = sample_rate #defined in OpenSdrGuiLogic.py

    def set_modulation_mode_cb(self, mode):
        print("Setting Modulation mode to ", mode)
        self.set_modulation_mode(mode)

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
        print("PyQtSdrGui 'on_modulation_mode_event' %s"%(str(mode)))
        self.on_modulation_mode.emit(mode)

    def on_volume_changed_event(self,percent):
        print('on_volume_changed',percent)
        self.on_volume_changed.emit(int(percent))

    def on_rf_gain_changed_event(self,percent):
        print('on_rf_gain_changed',percent)
        self.on_rf_gain_changed.emit(int(percent))

    def on_drive_changed_event(self,percent):
        print('on_drive_changed',percent)
        self.on_drive_changed.emit(int(percent))

    def on_mic_changed_event(self,percent):
        print('on_mic_changed',percent)
        self.on_mic_changed.emit(int(percent))

    def on_rfatten_toggled_event(self, toggled):
        print('on_rfatten_toggled',toggled)
        self.on_rfatten_toggled.emit((toggled))

    def on_rfpreamp_toggled_event(self, toggled):
        print('on_rfpreamp_toggled',toggled)
        self.on_rfpreamp_toggled.emit((toggled))

    def on_audiopreamp_toggled_event(self, toggled):
        print('on_audiopreamp_toggled',toggled)
        self.on_audiopreamp_toggled.emit((toggled))

    def on_vox_toggled_event(self, toggled):
        print('on_vox_toggled',toggled)
        self.on_vox_toggled.emit((toggled))

    def on_mute_toggled_event(self, toggled):
        print('on_mute_toggled',toggled)
        self.on_mute_toggled.emit((toggled))

class my_top_block(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
        self.main_box = PyQtSDRGUI()
        self.main_box.show()

def main():
    qapp = QApplication(sys.argv)
    tb = my_top_block()
    tb.start()
    qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
