#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class GridSizeSlider(QtWidgets.QSlider):
    def __init__(self, parent):
        print("slider init")
        super(GridSizeSlider, self).__init__(parent)

#    def sliderMoved2(self, e):
#        print(e)
#        print(dir(e))#e.pos())
#
#
#    def valueChanged(self, e):
#        print("changerd")
#
#    def sliderPressed(self, e):
#        print("oressed")
#
#    def sliderMoved(self, e):
#        print("moved")
#
#    def sliderReleased(self, e):
#        print('released')
