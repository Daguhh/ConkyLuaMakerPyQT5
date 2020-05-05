#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsLineItem, QGraphicsItem


class DrawingsList:

    def __init__(self):
        self.draws_dct = {}
        self.q_objects = {'ellipsegraphBtn' : MyEllipse,
                            'Ring Graph' : MyEllipse}
        #self.draw_generator()
        self.genID = self.id_generator()

    @staticmethod
    def id_generator():
        def genID():
            i = 0
            while True:
                i += 1
                yield f"ellipse_#{i}"
        return genID

    def create(self, item):
        print(item)

        if item in self.q_objects.keys():
            new_id = self.genID()
            new_draw = DrawItem(self.q_objects[item])
            self.draws_dct[new_id] = new_draw
        else:
            print(f'can not create unkown {item} object')

        return new_id


class DrawItem:

    def __init__(self, itemclass):

        self.properties = {}
        self.nb_input = 1
        #self.create(itemclass)
        self.buffer=[]
        self.itemclass = itemclass

    def create(self):

        print(self.buffer)
        x, y = self.buffer[0]
        w, h = 50, 50

        self.draw = self.itemclass(x,y,w,h)

        return self.draw

    #def buffer(self, mouse_input):
    #    pass

    def get_input(self, pos):
        if self.nb_input > 0:
            self.nb_input -= 1
            self.buffer.append(pos)
        else:
            self.create(self.itemclass)



class MyEllipse(QGraphicsEllipseItem):

    def __init__(self, x, y, w, h):

        x = x - w/2
        y = y - h/2
        super(MyEllipse, self).__init__(x, y, w, h)
        self.setFlags(QGraphicsItem.ItemIsMovable)

        self.pen=QtGui.QPen(QtGui.QColor(QtCore.Qt.green))
        self.pen.setWidth(15)
        self.setPen(self.pen)

    def mousePressEvent(self, e):
        print(self.name)
        print('click on ellipse')

