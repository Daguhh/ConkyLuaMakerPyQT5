#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class PreviewGraphicScene(QtWidgets):
    def __init__(self, parent):
        super().__init__(parent)


        self.pen=QtGui.QPen(QtGui.QColor(QtCore.Qt.green))
        self.pen.setWidth(5)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 200, 200)
        self.scene.clear()

        self.view =QGraphicsView(self.scene)
        self.view.setScene(self.scene)
        self.view.setCacheMode(QGraphicsView.CacheBackground)

    def mousePressEvent(self, e):
        print(e)
        print(e.pos())
        print(e.x())
        ellipse = self.scene.addEllipse(e.x(), e.y(), 50, 50, self.pen)
        print(ellipse)
        self.view.show()
