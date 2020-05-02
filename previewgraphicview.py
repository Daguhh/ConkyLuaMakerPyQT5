#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class PreviewGraphicView(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(PreviewGraphicView, self).__init__(parent)

    def mousePressEvent(self, e):
        print(e)
        print(e.pos())
