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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from ssb_rx import ssb_rx  # grc-generated hier_block
import genesis
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
        self.variable_volume_percent_0 = variable_volume_percent_0 = 25
        self.variable_rf_gain_percent0 = variable_rf_gain_percent0 = 100
        self.variable_gui_modulation_0 = variable_gui_modulation_0 = 3
        self.variable_drive_percent_0 = variable_drive_percent_0 = 0
        self.variable_rf_preamp_0 = variable_rf_preamp_0 = 0
        self.variable_rf_atten_0 = variable_rf_atten_0 = 0
        self.variable_qtgui_label_0_1_0 = variable_qtgui_label_0_1_0 = variable_drive_percent_0
        self.variable_qtgui_label_0_1 = variable_qtgui_label_0_1 = variable_rf_gain_percent0
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = variable_volume_percent_0
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = variable_gui_modulation_0
        self.variable_on_lo_freq_0 = variable_on_lo_freq_0 = 10000000
        self.variable_gui_on_vfo_freq_0 = variable_gui_on_vfo_freq_0 = 10001000
        self.variable_gui_on_band_0 = variable_gui_on_band_0 = 0
        self.variable_gui_bandwidth_low_0 = variable_gui_bandwidth_low_0 = 200
        self.variable_gui_bandwidth_high_0 = variable_gui_bandwidth_high_0 = 2700
        self.variable_audio_preamp_0 = variable_audio_preamp_0 = 0
        self.samp_rate = samp_rate = 48000
        self.audio_gain = audio_gain = (variable_volume_percent_0/100.0)*10.0

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_label_0_1_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_1_0_formatter = None
        else:
          self._variable_qtgui_label_0_1_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_1_0_tool_bar.addWidget(Qt.QLabel('Drive'+": "))
        self._variable_qtgui_label_0_1_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_1_0_formatter(self.variable_qtgui_label_0_1_0)))
        self._variable_qtgui_label_0_1_0_tool_bar.addWidget(self._variable_qtgui_label_0_1_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_1_0_tool_bar, 2, 3, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
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
        self.ssb_rx_0 = ssb_rx(
            af_gain=audio_gain,
            agc_decay=.000050,
            freq_offset=variable_on_lo_freq_0 - variable_gui_on_vfo_freq_0,
            low_cut=variable_gui_bandwidth_low_0,
            modulation_mode=variable_gui_modulation_0,
            samp_rate=samp_rate,
            width=variable_gui_bandwidth_high_0,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	4096, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	variable_on_lo_freq_0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	False, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/15)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)


        self.qtgui_sink_x_0.enable_rf_freq(True)



        self.genesis_g59_0 = genesis.g59(
                         freq=variable_on_lo_freq_0,
                         filt=variable_gui_on_band_0,
                         attenuation=variable_rf_atten_0,
                         audiopreamp=variable_audio_preamp_0,
                         rfpreamp=variable_rf_preamp_0,
                         tx=False,
                         transverterver=False,
                         dummy_usb=False)

        self.PyQtSDRGUI_0 = PyQtSDRGUI.PyQtSDRGUI(parent=None,
                              itu_region='itu-region2',
                              band_id=1,
                              bandwidth_low=200,
                              bandwidth_high=2700,
                              volume=5,
                              rf_gain=100,
                              vfo_freq=7001000,
                              lo_freq=7000000,
                              sample_rate=44100,
                              modulation_mode=3)
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

        def PyQtSDRGUI_0_rfatten_callback(onoff):
        	self.set_variable_rf_atten_0(onoff)

        self.PyQtSDRGUI_0.on_rfatten_toggled.connect(PyQtSDRGUI_0_rfatten_callback)

        def PyQtSDRGUI_0_rfpreamp_callback(onoff):
        	self.set_variable_rf_preamp_0(onoff)

        self.PyQtSDRGUI_0.on_rfpreamp_toggled.connect(PyQtSDRGUI_0_rfpreamp_callback)

        def PyQtSDRGUI_0_audiopreamp_callback(onoff):
        	self.set_variable_audio_preamp_0(onoff)

        self.PyQtSDRGUI_0.on_audiopreamp_toggled.connect(PyQtSDRGUI_0_audiopreamp_callback)





        ##################################################
        # Connections
        ##################################################
        self.connect((self.ssb_rx_0, 0), (self.qtgui_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_volume_percent_0(self):
        return self.variable_volume_percent_0

    def set_variable_volume_percent_0(self, variable_volume_percent_0):
        self.variable_volume_percent_0 = variable_volume_percent_0
        self.set_audio_gain((self.variable_volume_percent_0/100.0)*10.0)
        self.set_variable_qtgui_label_0_0(self._variable_qtgui_label_0_0_formatter(self.variable_volume_percent_0))

    def get_variable_rf_gain_percent0(self):
        return self.variable_rf_gain_percent0

    def set_variable_rf_gain_percent0(self, variable_rf_gain_percent0):
        self.variable_rf_gain_percent0 = variable_rf_gain_percent0
        self.set_variable_qtgui_label_0_1(self._variable_qtgui_label_0_1_formatter(self.variable_rf_gain_percent0))

    def get_variable_gui_modulation_0(self):
        return self.variable_gui_modulation_0

    def set_variable_gui_modulation_0(self, variable_gui_modulation_0):
        self.variable_gui_modulation_0 = variable_gui_modulation_0
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.variable_gui_modulation_0))
        self.ssb_rx_0.set_modulation_mode(self.variable_gui_modulation_0)

    def get_variable_drive_percent_0(self):
        return self.variable_drive_percent_0

    def set_variable_drive_percent_0(self, variable_drive_percent_0):
        self.variable_drive_percent_0 = variable_drive_percent_0
        self.set_variable_qtgui_label_0_1_0(self._variable_qtgui_label_0_1_0_formatter(self.variable_drive_percent_0))

    def get_variable_rf_preamp_0(self):
        return self.variable_rf_preamp_0

    def set_variable_rf_preamp_0(self, variable_rf_preamp_0):
        self.variable_rf_preamp_0 = variable_rf_preamp_0
        self.genesis_g59_0.rfpreamp(self.variable_rf_preamp_0)

    def get_variable_rf_atten_0(self):
        return self.variable_rf_atten_0

    def set_variable_rf_atten_0(self, variable_rf_atten_0):
        self.variable_rf_atten_0 = variable_rf_atten_0
        self.genesis_g59_0.attenuator(self.variable_rf_atten_0)

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

    def get_variable_on_lo_freq_0(self):
        return self.variable_on_lo_freq_0

    def set_variable_on_lo_freq_0(self, variable_on_lo_freq_0):
        self.variable_on_lo_freq_0 = variable_on_lo_freq_0
        self.ssb_rx_0.set_freq_offset(self.variable_on_lo_freq_0 - self.variable_gui_on_vfo_freq_0)
        self.qtgui_sink_x_0.set_frequency_range(self.variable_on_lo_freq_0, self.samp_rate)
        self.genesis_g59_0.set_lo_frequency(self.variable_on_lo_freq_0)

    def get_variable_gui_on_vfo_freq_0(self):
        return self.variable_gui_on_vfo_freq_0

    def set_variable_gui_on_vfo_freq_0(self, variable_gui_on_vfo_freq_0):
        self.variable_gui_on_vfo_freq_0 = variable_gui_on_vfo_freq_0
        self.ssb_rx_0.set_freq_offset(self.variable_on_lo_freq_0 - self.variable_gui_on_vfo_freq_0)

    def get_variable_gui_on_band_0(self):
        return self.variable_gui_on_band_0

    def set_variable_gui_on_band_0(self, variable_gui_on_band_0):
        self.variable_gui_on_band_0 = variable_gui_on_band_0
        self.genesis_g59_0.set_band_filter(self.variable_gui_on_band_0)

    def get_variable_gui_bandwidth_low_0(self):
        return self.variable_gui_bandwidth_low_0

    def set_variable_gui_bandwidth_low_0(self, variable_gui_bandwidth_low_0):
        self.variable_gui_bandwidth_low_0 = variable_gui_bandwidth_low_0
        self.ssb_rx_0.set_low_cut(self.variable_gui_bandwidth_low_0)

    def get_variable_gui_bandwidth_high_0(self):
        return self.variable_gui_bandwidth_high_0

    def set_variable_gui_bandwidth_high_0(self, variable_gui_bandwidth_high_0):
        self.variable_gui_bandwidth_high_0 = variable_gui_bandwidth_high_0
        self.ssb_rx_0.set_width(self.variable_gui_bandwidth_high_0)

    def get_variable_audio_preamp_0(self):
        return self.variable_audio_preamp_0

    def set_variable_audio_preamp_0(self, variable_audio_preamp_0):
        self.variable_audio_preamp_0 = variable_audio_preamp_0
        self.genesis_g59_0.audiopreamp(self.variable_audio_preamp_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ssb_rx_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(self.variable_on_lo_freq_0, self.samp_rate)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self.ssb_rx_0.set_af_gain(self.audio_gain)


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
