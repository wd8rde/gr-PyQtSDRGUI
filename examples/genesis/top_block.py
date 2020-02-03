#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.13.5
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from genesis_g59_xcvr import genesis_g59_xcvr  # grc-generated hier_block
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_PyQtSDRGUI as PyQtSDRGUI
import sip
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.variable_on_lo_freq_0 = variable_on_lo_freq_0 = 10000000
        self.variable_gui_on_vfo_freq_0 = variable_gui_on_vfo_freq_0 = 10001000
        self.variable_volume_percent_0 = variable_volume_percent_0 = 25
        self.variable_rf_gain_percent0 = variable_rf_gain_percent0 = 100
        self.variable_gui_modulation_0 = variable_gui_modulation_0 = "LSB"
        self.freq_offset_0 = freq_offset_0 = variable_gui_on_vfo_freq_0 - variable_on_lo_freq_0
        self.variable_vox_0 = variable_vox_0 = 0
        self.variable_rf_preamp_0 = variable_rf_preamp_0 = False
        self.variable_rf_atten_0 = variable_rf_atten_0 = False
        self.variable_qtgui_label_0_1_1 = variable_qtgui_label_0_1_1 = variable_rf_gain_percent0
        self.variable_qtgui_label_0_1_0 = variable_qtgui_label_0_1_0 = freq_offset_0
        self.variable_qtgui_label_0_1 = variable_qtgui_label_0_1 = variable_rf_gain_percent0
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = variable_volume_percent_0
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = variable_gui_modulation_0
        self.variable_mute_0 = variable_mute_0 = 0
        self.variable_mic_percent_0 = variable_mic_percent_0 = 60
        self.variable_gui_on_band_0 = variable_gui_on_band_0 = 0
        self.variable_gui_bandwidth_low_0 = variable_gui_bandwidth_low_0 = 200
        self.variable_gui_bandwidth_high_0 = variable_gui_bandwidth_high_0 = 2700
        self.variable_drive_percent_0 = variable_drive_percent_0 = 0
        self.variable_audio_preamp_0 = variable_audio_preamp_0 = 0
        self.samp_rate = samp_rate = 19200
        self.rf_gain_0 = rf_gain_0 = (variable_rf_gain_percent0/100.0)
        self.iq_samp_rate = iq_samp_rate = 48000
        self.iq_input_device = iq_input_device = "plughw:SB,0"
        self.audio_samp_rate = audio_samp_rate = 48000
        self.audio_output_device = audio_output_device = "hw:Pro,0"
        self.audio_gain = audio_gain = (variable_volume_percent_0/100.0)

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_label_0_1_1_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_1_1_formatter = None
        else:
          self._variable_qtgui_label_0_1_1_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_1_1_tool_bar.addWidget(Qt.QLabel('LO Freq'+": "))
        self._variable_qtgui_label_0_1_1_label = Qt.QLabel(str(self._variable_qtgui_label_0_1_1_formatter(self.variable_qtgui_label_0_1_1)))
        self._variable_qtgui_label_0_1_1_tool_bar.addWidget(self._variable_qtgui_label_0_1_1_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_1_1_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_1_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_1_0_formatter = None
        else:
          self._variable_qtgui_label_0_1_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_1_0_tool_bar.addWidget(Qt.QLabel('Freq offset'+": "))
        self._variable_qtgui_label_0_1_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_1_0_formatter(self.variable_qtgui_label_0_1_0)))
        self._variable_qtgui_label_0_1_0_tool_bar.addWidget(self._variable_qtgui_label_0_1_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_1_0_tool_bar, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_1_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_1_formatter = None
        else:
          self._variable_qtgui_label_0_1_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_1_tool_bar.addWidget(Qt.QLabel('RF Percent'+": "))
        self._variable_qtgui_label_0_1_label = Qt.QLabel(str(self._variable_qtgui_label_0_1_formatter(self.variable_qtgui_label_0_1)))
        self._variable_qtgui_label_0_1_tool_bar.addWidget(self._variable_qtgui_label_0_1_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_1_tool_bar, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_0_formatter = None
        else:
          self._variable_qtgui_label_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_tool_bar.addWidget(Qt.QLabel('Volume percent'+": "))
        self._variable_qtgui_label_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_formatter(self.variable_qtgui_label_0_0)))
        self._variable_qtgui_label_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_0_tool_bar, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Modulation'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	4096, #fftsize
        	firdes.WIN_BLACKMAN, #wintype
        	variable_on_lo_freq_0, #fc
        	iq_samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/15)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)


        self.qtgui_sink_x_0.enable_rf_freq(True)



        self.genesis_g59_xcvr_0 = genesis_g59_xcvr(
            audio_out_device_param=audio_output_device,
            audio_output_gain=audio_gain,
            audio_preamp_param=variable_audio_preamp_0,
            audio_samp_rate_param=audio_samp_rate,
            band_param=variable_gui_on_band_0,
            bandwidth_hi_param=variable_gui_bandwidth_high_0,
            bandwidth_low_param=variable_gui_bandwidth_low_0,
            freq_offset_param=freq_offset_0,
            input_iq_audio_device_param=iq_input_device,
            iq_sample_rate_param=iq_samp_rate,
            lo_freq_param=variable_on_lo_freq_0,
            mod_mode_param=variable_gui_modulation_0,
            rf_atten_param=variable_rf_atten_0,
            rf_gain_param=rf_gain_0,
            rf_preamp_param=variable_rf_preamp_0,
        )
        self.PyQtSDRGUI_0 = PyQtSDRGUI.PyQtSDRGUI(parent=None,
                              itu_region='itu-region2',
                              band_id=1,
                              bandwidth_low=200,
                              bandwidth_high=2700,
                              volume=5,
                              rf_gain=100,
                              drive=0,
                              mic=60,
                              vfo_freq=7001000,
                              lo_freq=7000000,
                              sample_rate=iq_samp_rate,
                              modulation_mode='3')
        self.top_grid_layout.addWidget(self.PyQtSDRGUI_0, 0, 0, 1, 4)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)


        def PyQtSDRGUI_0_band_callback(band):
        	self.set_variable_gui_on_band_0(band)

        self.PyQtSDRGUI_0.on_band.connect( PyQtSDRGUI_0_band_callback)

        def PyQtSDRGUI_0_bandwidth_high_callback(bandwidth):
        	self.set_variable_gui_bandwidth_high_0(bandwidth)

        self.PyQtSDRGUI_0.on_bandwidth_high.connect(PyQtSDRGUI_0_bandwidth_high_callback)

        def PyQtSDRGUI_0_bandwidth_low_callback(bandwidth):
        	self.set_variable_gui_bandwidth_low_0(bandwidth)

        self.PyQtSDRGUI_0.on_bandwidth_low.connect(PyQtSDRGUI_0_bandwidth_low_callback)

        def PyQtSDRGUI_0_vfo_callback(freq):
        	self.set_variable_gui_on_vfo_freq_0(freq)

        self.PyQtSDRGUI_0.on_vfo_frequency.connect( PyQtSDRGUI_0_vfo_callback)

        def PyQtSDRGUI_0_lo_callback(freq):
        	self.set_variable_on_lo_freq_0(freq)

        self.PyQtSDRGUI_0.on_lo_frequency.connect( PyQtSDRGUI_0_lo_callback)

        def PyQtSDRGUI_0_modulation_callback(modulation):
        	self.set_variable_gui_modulation_0(modulation)

        self.PyQtSDRGUI_0.on_modulation_mode.connect(PyQtSDRGUI_0_modulation_callback)

        def PyQtSDRGUI_0_volume_callback(volume):
        	self.set_variable_volume_percent_0(volume)

        self.PyQtSDRGUI_0.on_volume_changed.connect(PyQtSDRGUI_0_volume_callback)

        def PyQtSDRGUI_0_rf_gain_callback(percent):
        	self.set_variable_rf_gain_percent0(percent)

        self.PyQtSDRGUI_0.on_rf_gain_changed.connect(PyQtSDRGUI_0_rf_gain_callback)

        def PyQtSDRGUI_0_drive_callback(percent):
        	self.set_variable_drive_percent_0(percent)

        self.PyQtSDRGUI_0.on_drive_changed.connect(PyQtSDRGUI_0_drive_callback)

        def PyQtSDRGUI_0_mic_callback(percent):
        	self.set_variable_mic_percent_0(percent)

        self.PyQtSDRGUI_0.on_mic_changed.connect(PyQtSDRGUI_0_mic_callback)

        def PyQtSDRGUI_0_rfatten_callback(onoff):
        	self.set_variable_rf_atten_0(onoff)

        self.PyQtSDRGUI_0.on_rfatten_toggled.connect(PyQtSDRGUI_0_rfatten_callback)

        def PyQtSDRGUI_0_rfpreamp_callback(onoff):
        	self.set_variable_rf_preamp_0(onoff)

        self.PyQtSDRGUI_0.on_rfpreamp_toggled.connect(PyQtSDRGUI_0_rfpreamp_callback)

        def PyQtSDRGUI_0_vox_callback(onoff):
        	self.set_variable_vox_0(onoff)

        self.PyQtSDRGUI_0.on_vox_toggled.connect(PyQtSDRGUI_0_vox_callback)

        def PyQtSDRGUI_0_mute_callback(onoff):
        	self.set_variable_mute_0(onoff)

        self.PyQtSDRGUI_0.on_mute_toggled.connect(PyQtSDRGUI_0_mute_callback)

        def PyQtSDRGUI_0_audiopreamp_callback(onoff):
        	self.set_variable_audio_preamp_0(onoff)

        self.PyQtSDRGUI_0.on_audiopreamp_toggled.connect(PyQtSDRGUI_0_audiopreamp_callback)





        ##################################################
        # Connections
        ##################################################
        self.connect((self.genesis_g59_xcvr_0, 0), (self.qtgui_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_on_lo_freq_0(self):
        return self.variable_on_lo_freq_0

    def set_variable_on_lo_freq_0(self, variable_on_lo_freq_0):
        self.variable_on_lo_freq_0 = variable_on_lo_freq_0
        self.set_freq_offset_0(self.variable_gui_on_vfo_freq_0 - self.variable_on_lo_freq_0)
        self.qtgui_sink_x_0.set_frequency_range(self.variable_on_lo_freq_0, self.iq_samp_rate)
        self.genesis_g59_xcvr_0.set_lo_freq_param(self.variable_on_lo_freq_0)

    def get_variable_gui_on_vfo_freq_0(self):
        return self.variable_gui_on_vfo_freq_0

    def set_variable_gui_on_vfo_freq_0(self, variable_gui_on_vfo_freq_0):
        self.variable_gui_on_vfo_freq_0 = variable_gui_on_vfo_freq_0
        self.set_freq_offset_0(self.variable_gui_on_vfo_freq_0 - self.variable_on_lo_freq_0)

    def get_variable_volume_percent_0(self):
        return self.variable_volume_percent_0

    def set_variable_volume_percent_0(self, variable_volume_percent_0):
        self.variable_volume_percent_0 = variable_volume_percent_0
        self.set_audio_gain((self.variable_volume_percent_0/100.0))
        self.set_variable_qtgui_label_0_0(self._variable_qtgui_label_0_0_formatter(self.variable_volume_percent_0))

    def get_variable_rf_gain_percent0(self):
        return self.variable_rf_gain_percent0

    def set_variable_rf_gain_percent0(self, variable_rf_gain_percent0):
        self.variable_rf_gain_percent0 = variable_rf_gain_percent0
        self.set_rf_gain_0((self.variable_rf_gain_percent0/100.0))
        self.set_variable_qtgui_label_0_1_1(self._variable_qtgui_label_0_1_1_formatter(self.variable_rf_gain_percent0))
        self.set_variable_qtgui_label_0_1(self._variable_qtgui_label_0_1_formatter(self.variable_rf_gain_percent0))

    def get_variable_gui_modulation_0(self):
        return self.variable_gui_modulation_0

    def set_variable_gui_modulation_0(self, variable_gui_modulation_0):
        self.variable_gui_modulation_0 = variable_gui_modulation_0
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.variable_gui_modulation_0))
        self.genesis_g59_xcvr_0.set_mod_mode_param(self.variable_gui_modulation_0)

    def get_freq_offset_0(self):
        return self.freq_offset_0

    def set_freq_offset_0(self, freq_offset_0):
        self.freq_offset_0 = freq_offset_0
        self.set_variable_qtgui_label_0_1_0(self._variable_qtgui_label_0_1_0_formatter(self.freq_offset_0))
        self.genesis_g59_xcvr_0.set_freq_offset_param(self.freq_offset_0)

    def get_variable_vox_0(self):
        return self.variable_vox_0

    def set_variable_vox_0(self, variable_vox_0):
        self.variable_vox_0 = variable_vox_0

    def get_variable_rf_preamp_0(self):
        return self.variable_rf_preamp_0

    def set_variable_rf_preamp_0(self, variable_rf_preamp_0):
        self.variable_rf_preamp_0 = variable_rf_preamp_0
        self.genesis_g59_xcvr_0.set_rf_preamp_param(self.variable_rf_preamp_0)

    def get_variable_rf_atten_0(self):
        return self.variable_rf_atten_0

    def set_variable_rf_atten_0(self, variable_rf_atten_0):
        self.variable_rf_atten_0 = variable_rf_atten_0
        self.genesis_g59_xcvr_0.set_rf_atten_param(self.variable_rf_atten_0)

    def get_variable_qtgui_label_0_1_1(self):
        return self.variable_qtgui_label_0_1_1

    def set_variable_qtgui_label_0_1_1(self, variable_qtgui_label_0_1_1):
        self.variable_qtgui_label_0_1_1 = variable_qtgui_label_0_1_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_1_1_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_1_1))

    def get_variable_qtgui_label_0_1_0(self):
        return self.variable_qtgui_label_0_1_0

    def set_variable_qtgui_label_0_1_0(self, variable_qtgui_label_0_1_0):
        self.variable_qtgui_label_0_1_0 = variable_qtgui_label_0_1_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_1_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_1_0))

    def get_variable_qtgui_label_0_1(self):
        return self.variable_qtgui_label_0_1

    def set_variable_qtgui_label_0_1(self, variable_qtgui_label_0_1):
        self.variable_qtgui_label_0_1 = variable_qtgui_label_0_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_1_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_1))

    def get_variable_qtgui_label_0_0(self):
        return self.variable_qtgui_label_0_0

    def set_variable_qtgui_label_0_0(self, variable_qtgui_label_0_0):
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_variable_mute_0(self):
        return self.variable_mute_0

    def set_variable_mute_0(self, variable_mute_0):
        self.variable_mute_0 = variable_mute_0

    def get_variable_mic_percent_0(self):
        return self.variable_mic_percent_0

    def set_variable_mic_percent_0(self, variable_mic_percent_0):
        self.variable_mic_percent_0 = variable_mic_percent_0

    def get_variable_gui_on_band_0(self):
        return self.variable_gui_on_band_0

    def set_variable_gui_on_band_0(self, variable_gui_on_band_0):
        self.variable_gui_on_band_0 = variable_gui_on_band_0
        self.genesis_g59_xcvr_0.set_band_param(self.variable_gui_on_band_0)

    def get_variable_gui_bandwidth_low_0(self):
        return self.variable_gui_bandwidth_low_0

    def set_variable_gui_bandwidth_low_0(self, variable_gui_bandwidth_low_0):
        self.variable_gui_bandwidth_low_0 = variable_gui_bandwidth_low_0
        self.genesis_g59_xcvr_0.set_bandwidth_low_param(self.variable_gui_bandwidth_low_0)

    def get_variable_gui_bandwidth_high_0(self):
        return self.variable_gui_bandwidth_high_0

    def set_variable_gui_bandwidth_high_0(self, variable_gui_bandwidth_high_0):
        self.variable_gui_bandwidth_high_0 = variable_gui_bandwidth_high_0
        self.genesis_g59_xcvr_0.set_bandwidth_hi_param(self.variable_gui_bandwidth_high_0)

    def get_variable_drive_percent_0(self):
        return self.variable_drive_percent_0

    def set_variable_drive_percent_0(self, variable_drive_percent_0):
        self.variable_drive_percent_0 = variable_drive_percent_0

    def get_variable_audio_preamp_0(self):
        return self.variable_audio_preamp_0

    def set_variable_audio_preamp_0(self, variable_audio_preamp_0):
        self.variable_audio_preamp_0 = variable_audio_preamp_0
        self.genesis_g59_xcvr_0.set_audio_preamp_param(self.variable_audio_preamp_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rf_gain_0(self):
        return self.rf_gain_0

    def set_rf_gain_0(self, rf_gain_0):
        self.rf_gain_0 = rf_gain_0
        self.genesis_g59_xcvr_0.set_rf_gain_param(self.rf_gain_0)

    def get_iq_samp_rate(self):
        return self.iq_samp_rate

    def set_iq_samp_rate(self, iq_samp_rate):
        self.iq_samp_rate = iq_samp_rate
        self.qtgui_sink_x_0.set_frequency_range(self.variable_on_lo_freq_0, self.iq_samp_rate)
        self.genesis_g59_xcvr_0.set_iq_sample_rate_param(self.iq_samp_rate)
        self.PyQtSDRGUI_0.set_sample_rate_cb(self.iq_samp_rate)

    def get_iq_input_device(self):
        return self.iq_input_device

    def set_iq_input_device(self, iq_input_device):
        self.iq_input_device = iq_input_device
        self.genesis_g59_xcvr_0.set_input_iq_audio_device_param(self.iq_input_device)

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate
        self.genesis_g59_xcvr_0.set_audio_samp_rate_param(self.audio_samp_rate)

    def get_audio_output_device(self):
        return self.audio_output_device

    def set_audio_output_device(self, audio_output_device):
        self.audio_output_device = audio_output_device
        self.genesis_g59_xcvr_0.set_audio_out_device_param(self.audio_output_device)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self.genesis_g59_xcvr_0.set_audio_output_gain(self.audio_gain)


def main(top_block_cls=top_block, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
