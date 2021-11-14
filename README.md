# GNURadio Companion Python Qt SDR GUI oot block

This is a **Work in Progress**. Not everything works yet ... Jan, 5, 2020

Based on .ui file from [OpenExpertSDR](https://github.com/florintanasa/OpenExpertSDR)

This project creates a QT GNU Radio block which may be loaded into GNU Radio Companion. It will be located under [Core]/WD8RDE/QT/PyQt SDR GUI.

![PyQtSDRGUI-screenshot.png](https://github.com/wd8rde/gr-PyQtSDRGUI/blob/master/screenshots/PyQtSDRGUI-screenshot.png)

## Compatibility:
GNU Radio 3.13.13.5 and greater
Python 2.7
pyqt5

## Getting Source:
`git clone https://github.com/wd8rde/gr-PyQtSDRGUI.git`

## Dependancies:
`sudo apt install gnuradio`

## Compilation and Installation:
```
cd gr-PyQtSDRGUI
mkdir build
cd build
cmake ../
make
sudo make install`
```

## Usage:
![PyQtSDRGUI-properties-screenshot.png](https://github.com/wd8rde/gr-PyQtSDRGUI/blob/master/screenshots/PyQtSDRGUI-properties-screenshot.png)

### ITU Region:
Specifies the ITU Region that is used to set the VFO Band Limits, currently supports 'itu-region1', 'itu-region2', and 'itu-region3'.
### Band:
Specifies the Band Filter selection, these are currently defined as yaesu band constants, bypass:0, 160m:1, 80m:2, 40m:3, 30m:4, 20m:5, 17m:6, 15m:7, 12m:8, 10m:9, 6m:10.
### Bandwidth Low Cutoff:
Low cutoff Frequency in Hertz for Demod filter.
### Bandwidth High Cutoff:
High cutoff Frequency in Hertz for Demod filter.
### Volume:
Precent of full volume 0-100.
### VFO Frequency:
Frequency in Hertz as displayed in frequency digits.
### LO Frequency:
Frequency in Hertz as of the Local Oscilator frequency.
### Sample Rate:
Sample Rate of LO Frequency frames.
### Band Changed Variable:
GRC Variable that will be updated by Band Filter Change Signals. Currently defined as {bypass:0, 160m:1, 80m:2, 40m:3, 30m:4, 20m:5, 17m:6, 15m:7, 12m:8, 10m:9, 6m:10}.
### Bandwidth High Changed Variable:
GRC Variable that will be updated by Bandwidth High Change Signals. Integer in Hertz.
### Bandwidth Low Changed Variable:
GRC Variable that will be updated by Bandwidth Low Change Signals. Integer in Hertz.
### VFO Frequency Changed Variable:
GRC Variable that will be updated by VFO Frequency Change Signals. Integer 0-9999999999 in Hertz.
### LO Frequency Changed Variable:
GRC Variable that will be updated by LO Frequency Change Signals. Integer 0-9999999999 in Hertz.
### Modulation Mode Changed Variable:
GRC Variable that will be updated by Modulation Mode Change Signals. These are currently defined as AM':0,'SAM':1,'DSB':2,'LSB':3,'USB':4,'CWL':5,'CWU':6,'FMN':7,'SPEC':8,'DIGL':9,'DIGL':10,'DIGU':11,'DRM':12 }.
### Volume Changed Variable:
GRC Variable that will be updated by Volume Change Signals. Integer 0-100 in percent.
### RF Attenuator Changed Variable:
GRC Variable that will be updated by RF Attenuator Change Signals. Boolean True/False.
### RF Preamplifier Changed Variable:
GRC Variable that will be updated by RF Preamplifier Change Signals. Boolean True/False.
### Audio Preamplifier Changed Variable:
GRC Variable that will be updated by Audio Preamplifier Change Signals. Boolean True/False.

## Developement
- python/gr_PyQtSDRGUI.py::PyQtSDRGUI(Qt.QWidget,OpenSdrGuiLogic) creates GNU Radio Qt Block, provides accessor methods and Qt signals.
- python/OpenSdrGuiLogic.py::OpenSdrGuiLogic(Ui_OpenGRSDR) provides GUI behavour and logic.
- python/OpenGrSdrGui.py::Ui_OpenGRSDR(object) is generated from opengrsdrgui.ui using `pyuic5 -o opengrsdrgui.ui opengrsdrgui.ui`
- grc/wd8rde_gr_PyQtSDRGUI.xml defines block creation under GNU Radio Companion.
