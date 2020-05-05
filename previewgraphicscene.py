#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class PreviewGraphicScene(QtWidgets.QWidget):
    def __init__(self, parent):
        super(PreviewGraphicScene, self).__init__(parent)

        self.layout = QtWidgets.QHBoxLayout(self)

        self.scene = MyGraphicScene(self.layout)

        self.view =QtWidgets.QGraphicsView(self.scene)
        self.view.setScene(self.scene)
        self.view.setCacheMode(QtWidgets.QGraphicsView.CacheBackground)

        self.layout.addWidget(self.view)
        self.setLayout(self.layout)

class MyGraphicScene(QtWidgets.QGraphicsScene):

    def __init__(self, parent):
        super(MyGraphicScene, self).__init__()
        self.setSceneRect(0,0,600,400)
        self.clear()

        self.wait_for_input = -1
        self.ellipse_count = 0

    def send_object_list(self, drawings):
        self.drawings = drawings

#    def dragEnterEvent(self, e):
#        print('drag')

    def input_request(self, sender_id, nb_input):
        self.requester_ID = sender_id
        self.wait_for_input = nb_input

    def mousePressEvent(self, e):
        print('')
        print(' --- new event --- ')
        print('click on scene')
        print(f'wait for input : {self.wait_for_input}')

        if self.wait_for_input > 0:
            self.wait_for_input -= 1
            pos = (e.scenePos().x(), e.scenePos().y())
            self.drawings.draws_dct[self.requester_ID].get_input(pos)
        else:
            QtWidgets.QGraphicsScene.mousePressEvent(self, e)

        if self.wait_for_input == 0:
            self.wait_for_input -= 1
            self.addItem(self.drawings.draws_dct[self.requester_ID].create())

class MyEllipse(QtWidgets.QGraphicsEllipseItem):

    def __init__(self, x, y, w, h):
        super(MyEllipse, self).__init__(x, y, w, h)
        self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable)

        self.pen=QtGui.QPen(QtGui.QColor(QtCore.Qt.green))
        self.pen.setWidth(15)
        self.setPen(self.pen)


#    def hoverEnterEvent(self, e):
#        print('hover ellipse')
#
#    def hoverLeaveEvent(self, e):
#        print('hover leave')

    def mousePressEvent(self, e):
        print(self.name)
        print('click on ellipse')

#    def dragEnterEvent(self,e):
#        print('drag_item')

