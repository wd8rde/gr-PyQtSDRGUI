# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from OpenGrSdrGui import *

class OpenSdrGuiLogic(Ui_OpenGRSDR):
    def __init__(self,
                 itu_region='itu-region2',
                 band_id=0,
                 bandwidth_low=200,
                 bandwidth_high=2700,
                 volume=25,
                 vfo_freq=7001000,
                 lo_freq=7000000,
                 sample_rate=44100):

        Ui_OpenGRSDR.__init__(self)
        self.current_band = band_id
        self.itu_region = itu_region
        self.band_plans = {'itu-region1':{0:[0,9999999999],
                                          1:[1810000,2000000],
                                          2:[3500000,3800000],
                                          3:[7000000,7200000],
                                          4:[10100000,10150000],
                                          5:[14000000,14350000],
                                          6:[18068000,18168000],
                                          7:[21000000,21450000],
                                          8:[24890000,24990000],
                                          9:[28000000,29700000],
                                          10:[50000000,52000000]},
                           'itu-region2':{0:[0,9999999999],
                                          1:[1800000,2000000],
                                          2:[3500000,4000000],
                                          3:[7000000,7300000],
                                          4:[10100000,10150000],
                                          5:[14000000,14350000],
                                          6:[18068000,18168000],
                                          7:[21000000,21450000],
                                          8:[24890000,24990000],
                                          9:[28000000,29700000],
                                          10:[50000000,54000000]},
                           'itu-region3':{0:[0,9999999999],
                                          1:[1800000,2000000],
                                          2:[3500000,3900000],
                                          3:[7000000,7300000],
                                          4:[10100000,10150000],
                                          5:[14000000,14350000],
                                          6:[18068000,18168000],
                                          7:[21000000,21450000],
                                          8:[24890000,24990000],
                                          9:[28000000,29700000],
                                          10:[50000000,54000000]},
                            }

        self.band_freq_mem = {0:10000000,
                              1:self.band_plans[self.itu_region][1][0],
                              2:self.band_plans[self.itu_region][2][0],
                              3:self.band_plans[self.itu_region][3][0],
                              4:self.band_plans[self.itu_region][4][0],
                              5:self.band_plans[self.itu_region][5][0],
                              6:self.band_plans[self.itu_region][6][0],
                              7:self.band_plans[self.itu_region][7][0],
                              8:self.band_plans[self.itu_region][8][0],
                              9:self.band_plans[self.itu_region][9][0],
                              10:self.band_plans[self.itu_region][10][0],}

        self.vfo_frequency = self.band_freq_mem[self.current_band]
        self.lo_frequency = self.vfo_frequency + 1000
        self.current_bandwidth_high = bandwidth_high
        self.current_bandwidth_low = bandwidth_low
        self.current_volume = volume
        self.modulation_mode = 'AM'
        self.sample_rate = sample_rate

    def setupUi(self, object):
        Ui_OpenGRSDR.setupUi(self, object)
        self.set_vfo_frequency(self.vfo_frequency)

        #VFO Display
        self.pbDg9.clicked.connect(lambda: self.on_vfo_digit(9))
        self.pbDg8.clicked.connect(lambda: self.on_vfo_digit(8))
        self.pbDg7.clicked.connect(lambda: self.on_vfo_digit(7))
        self.pbDg6.clicked.connect(lambda: self.on_vfo_digit(6))
        self.pbDg5.clicked.connect(lambda: self.on_vfo_digit(5))
        self.pbDg4.clicked.connect(lambda: self.on_vfo_digit(4))
        self.pbDg3.clicked.connect(lambda: self.on_vfo_digit(3))
        self.pbDg2.clicked.connect(lambda: self.on_vfo_digit(2))
        self.pbDg1.clicked.connect(lambda: self.on_vfo_digit(1))
        self.pbDg0.clicked.connect(lambda: self.on_vfo_digit(0))

        self.installEventFilter(self)
        def eventFilter(self, obj, event):
            print('eventFilter ',obj,event)
            if event.type() == QtCore.QEvent.Wheel:
                if obj == self.pbDg9:
                    on_vfo_wheel(9,event)
            return True

        #Band Selection
        #return yaesu band constants, bypass:0, 160m:1, 80m:2, 40m:3, 30m:4, 20m:5, 17m:6, 15m:7, 12m:8, 10m:9, 6m:10.
        self.band_objs = {0:self.pbGEN,
                          1:self.pb160M,
                          2:self.pb80M,
                          3:self.pb40M,
                          4:self.pb30M,
                          5:self.pb20M,
                          6:self.pb17M,
                          7:self.pb15M,
                          8:self.pb12M,
                          9:self.pb10M,
                          10:self.pb6M,}

        #Band buttons
        self.pb160M.clicked.connect(lambda: self._on_band(1))
        self.pb80M.clicked.connect(lambda: self._on_band(2))
        self.pb40M.clicked.connect(lambda: self._on_band(3))
        self.pb30M.clicked.connect(lambda: self._on_band(4))
        self.pb20M.clicked.connect(lambda: self._on_band(5))
        self.pb17M.clicked.connect(lambda: self._on_band(6))
        self.pb15M.clicked.connect(lambda: self._on_band(7))
        self.pb12M.clicked.connect(lambda: self._on_band(8))
        self.pb10M.clicked.connect(lambda: self._on_band(9))
        self.pb6M.clicked.connect(lambda: self._on_band(10))
        self.pbGEN.clicked.connect(lambda: self._on_band(0))

        self.set_band(self.current_band)

        #Bandwidth
        self.bandwidth_objs = {0:self.pbF0,
                               1:self.pbF1,
                               2:self.pbF2,
                               3:self.pbF3,
                               4:self.pbF4,
                               5:self.pbF5,
                               6:self.pbF6,
                               7:self.pbF7,
                               8:self.pbF8,}

        #bandwidth buttons
        self.pbF0.clicked.connect(lambda: self._on_bandwidth_high(0))
        self.pbF1.clicked.connect(lambda: self._on_bandwidth_high(1))
        self.pbF2.clicked.connect(lambda: self._on_bandwidth_high(2))
        self.pbF3.clicked.connect(lambda: self._on_bandwidth_high(3))
        self.pbF4.clicked.connect(lambda: self._on_bandwidth_high(4))
        self.pbF5.clicked.connect(lambda: self._on_bandwidth_high(5))
        self.pbF6.clicked.connect(lambda: self._on_bandwidth_high(6))
        self.pbF7.clicked.connect(lambda: self._on_bandwidth_high(7))
        self.pbF8.clicked.connect(lambda: self._on_bandwidth_high(8))
        self.set_bandwidth_high(self.current_bandwidth_high)

        #Mode
        self.pbAM.clicked.connect(lambda: self._on_modulation_mode('AM'))
        self.pbSAM.clicked.connect(lambda: self._on_modulation_mode('SAM'))
        self.pbDSB.clicked.connect(lambda: self._on_modulation_mode('DSB'))
        self.pbLSB.clicked.connect(lambda: self._on_modulation_mode('LSB'))
        self.pbUSB.clicked.connect(lambda: self._on_modulation_mode('USB'))
        self.pbCWL.clicked.connect(lambda: self._on_modulation_mode('CWL'))
        self.pbCWU.clicked.connect(lambda: self._on_modulation_mode('CWU'))
        self.pbFMN.clicked.connect(lambda: self._on_modulation_mode('FMN'))
        self.pbSPEC.clicked.connect(lambda: self._on_modulation_mode('SPEC'))
        self.pbDIGL.clicked.connect(lambda: self._on_modulation_mode('DIGL'))
        self.pbDIGU.clicked.connect(lambda: self._on_modulation_mode('DIGU'))
        self.pbDRM.clicked.connect(lambda: self._on_modulation_mode('DRM'))

        #Volume
        self.slVol.valueChanged.connect(lambda i: self._on_volume_changed(i))
        self.set_volume(self.current_volume)

        #RF Attenuator
        self.pbAtten.toggled.connect(lambda i: self._on_rfatten_toggled(i))
        self.pbPreamp.toggled.connect(lambda i: self._on_rfpreamp_toggled(i))
        self.pbPa.toggled.connect(lambda i: self._on_audiopreamp_toggled(i))

    def wheelEvent(self, event):
        delta= ((event.angleDelta()/8)/15)
        mousepos = event.pos()
        obj = self.childAt(mousepos)
        vfo_digit_map = { self.pbDg9:9, self.pbDg8:8, self.pbDg7:7, self.pbDg6:6, self.pbDg5:5, self.pbDg4:4, self.pbDg3:3, self.pbDg2:2, self.pbDg1:1, self.pbDg0:0}
        if obj in vfo_digit_map:
            return self.on_vfo_wheel(vfo_digit_map[obj],event)
        event.accept()

    #Band Selection
    def set_band(self, band_id):
        self.band_objs[band_id].setChecked(True)
        self._on_band(band_id)

    def _on_band(self, band_id):
        print("_on_band %d button toggled"%band_id)
        #remember current band frequency with current vfo_freq
        self.band_freq_mem[self.current_band] = self.vfo_frequency
        #set the vfo to the memorized freq for band_id
        self.current_band = band_id
        self.set_vfo_frequency(self.band_freq_mem[band_id])
        self.on_band_event(band_id)

    def on_band_event(self, band_id):
        print("Band %d button toggled"%band_id)

    #VFO
    def on_vfo_digit(self, digit_place):
        print("VFO %d digit clicked"%digit_place)
        lo_freq = int(self.vfo_frequency)
        if 0 <= lo_freq < (10**10):
            self.set_lo_frequency(lo_freq)
            self.on_lo_frequency_event(lo_freq)

    def set_vfo_frequency(self,freq):
        freq = int(freq)
        if self.band_plans[self.itu_region][self.current_band][0] <= freq <= self.band_plans[self.itu_region][self.current_band][1]:
            self.vfo_frequency = int(freq)
            self.adjust_lo_freq()
            digits = ['0'] * 10
            digits += str(self.vfo_frequency)
            del digits[0:-10]
            self.pbDg9.setText(digits[0])
            self.pbDg8.setText(digits[1])
            self.pbDg7.setText(digits[2])
            self.pbDg6.setText(digits[3])
            self.pbDg5.setText(digits[4])
            self.pbDg4.setText(digits[5])
            self.pbDg3.setText(digits[6])
            self.pbDg2.setText(digits[7])
            self.pbDg1.setText(digits[8])
            self.pbDg0.setText(digits[9])
            self.on_vfo_frequency_event(freq)

    def on_vfo_frequency_event(self, freq):
        print("VFO changed to %d"%(int(freq)))

    def on_vfo_wheel(self,digit,event):
        delta= int(((event.angleDelta()/8)/15).y())
        digit = int(digit)
        event.accept()
        if 0 <= digit < 10:
            chng = (delta*(10**digit))
            vfo_freq = int(self.vfo_frequency + chng)
            if 0 <= vfo_freq < (10**10):
                self.set_vfo_frequency(vfo_freq)

    #LO Frequency
    def adjust_lo_freq(self):
        vfo = self.vfo_frequency
        lo = self.lo_frequency
        bw_high = self.current_bandwidth_high
        sample_rate = self.sample_rate
        #if below the lo
        if(vfo < lo):
            if(vfo - bw_high < lo - (sample_rate/2)):
                self.set_lo_frequency(vfo + bw_high)
        else:
            if(vfo + bw_high > lo + (sample_rate/2)):
                self.set_lo_frequency(vfo - bw_high)


    def set_lo_frequency(self,freq):
        print("LO set to %d"%(int(freq)))
        freq = int(freq)
        if self.band_plans[self.itu_region][self.current_band][0] <= freq <= self.band_plans[self.itu_region][self.current_band][1]:
            self.lo_frequency = int(freq)
            self.on_lo_frequency_event(freq)

    def on_lo_frequency_event(self, freq):
        print("LO changed to %d"%(int(freq)))

    #Bandwidth
    def set_bandwidth_high(self, bw):
        bw = int(bw)
        print("bandwidth_high set to %d"%(bw))
        _bw2button_map = {500:0,1800:1,2000:2,2400:3,2700:4,3000:5,3300:6,3700:7,4500:8}
        self.current_bandwidth_high = bw
        if (bw in _bw2button_map):
            bw_id = _bw2button_map[bw]
            self.bandwidth_objs[bw_id].setChecked(True)
        else:
            self.bandwidth_objs[8].setChecked(True)


    def _on_bandwidth_high(self,bw_id):
        print("bandwidth high button %d"%(int(bw_id)))
        _button2bw_map = {0:500,1:1800,2:2000,3:2400,4:2700,5:3000,6:3300,7:3700,8:4500,9:self.current_bandwidth_high}
        if(bw_id in _button2bw_map):
            bw = _button2bw_map[bw_id]
            self.current_bandwidth_high = bw
            self.on_bandwidth_high_event(bw)

    def on_bandwidth_high_event(self,bandwidth):
        print("Bandwidth High changed to %d"%(int(bandwidth)))
        pass

    def _on_bandwidth_low(self,bw_low):
        print("bandwidth low button %d"%(int(bw_low)))
        self.on_bandwidth_low_event(bw_low)

    def on_bandwidth_low_event(self,bandwidth):
        print("Bandwidth Low changed to %d"%(int(bandwidth)))
        pass

    def _on_modulation_mode(self,mode):
        self.modulation_mode = mode
        self.on_modulation_mode_event(mode)

    def on_modulation_mode_event(self,mode):
        print("Modulation Mode changed to %s"%(str(mode)))
        pass

    def set_volume(self,percent):
        percent=int(percent)
        if(100 < percent):
            percent=100
        elif(0 > percent):
            percent=0

        self.slVol.setValue(percent)
        self.current_volume = percent
        self._on_volume_changed(percent)

    def _on_volume_changed(self, percent):
        self.on_volume_changed_event(percent)

    def on_volume_changed_event(self,percent):
        print('on_volume_changed',percent)
        pass

    def _on_rfatten_toggled(self, toggled):
        self.on_rfatten_toggled_event(toggled)

    def on_rfatten_toggled_event(self, toggled):
        print('on_rfatten_toggled',toggled)
        pass

    def _on_rfpreamp_toggled(self, toggled):
        self.on_rfpreamp_toggled_event(toggled)

    def on_rfpreamp_toggled_event(self, toggled):
        print('on_rfpreamp_toggled',toggled)
        pass

    def _on_audiopreamp_toggled(self, toggled):
        self.on_audiopreamp_toggled_event(toggled)

    def on_audiopreamp_toggled_event(self, toggled):
        print('on_audiopreamp_toggled',toggled)
        pass

