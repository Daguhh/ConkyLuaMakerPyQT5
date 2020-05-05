import sys
from PyQt5 import QtWidgets, uic, QtGui

from MainWindow import Ui_MainWindow
from drawings import DrawingsList

"""
### Choice panel
self.RingGraphBtn
self.RingBtn
self.EllipseGraphBtn
self.EllipseBtn
self.LineBtn
self.BarGraphBtn
self.VarTextBtn
self.StaTextBtn

### Preview Panel
self.graphicsView
self.GridSizeSlider
self.MousePosLabel
self.gridsizeSpinBox

### SelectPanel
self.ObjectList
self.deleteBtn
self.RenameBtn

### Properties
self.PropList

"""

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # bin choice buttons
        self.ringgraphBtn.clicked.connect(self.create_graph)
        self.ringBtn.clicked.connect(self.create_graph)
        self.ellipsegraphBtn.clicked.connect(self.create_graph)
        self.ellipseBtn.clicked.connect(self.create_graph)
        self.lineBtn.clicked.connect(self.create_graph)
        self.bargraphBtn.clicked.connect(self.create_graph)
        self.vartextBtn.clicked.connect(self.create_graph)
        self.statextBtn.clicked.connect(self.create_graph)

        # Preview Panel Event
        #self.graphicsView.mousePressEvent(self.get_preview_input)
        self.gridsizeslider.sliderMoved.connect(self.change_grid_size)
        self.gridsizeSpinBox.valueChanged.connect(self.change_grid_size)

        self.drawings = DrawingsList()
        self.previewgraphicview.scene.send_object_list(self.drawings)

#        fenetre_widget = QWidget()
#
#        self.scene = QGraphicsScene(self)
#        self.scene.setSceneRect(0, 0, 200, 200)
#        self.scene.clear()
#
#        self.view =QGraphicsView(self.scene)
#        self.view.setScene(self.scene)
#        self.view.setCacheMode(QGraphicsView.CacheBackground)↓


    def create_graph(self, e):
        #self.previewgraphicview.scene.wait_for_input = True
        print("button clicked")
        print(self.sender().objectName())
        ID = self.drawings.create(self.sender().objectName())
        nb_input = self.drawings.draws_dct[ID].nb_input
        self.previewgraphicview.scene.input_request(ID, nb_input)


    def change_grid_size(self):
        sender_name = self.sender().objectName()
        val = self.sender().value()
        if sender_name == 'gridsizeslider':
            self.gridsizeSpinBox.setValue(val)
        elif sender_name == 'gridsizeSpinBox':
            self.gridsizeslider.setValue(val)
        self.graphicsView.gridsize = val


    def get_preview_input(self):
        print(dir(self.sender()))

class PreviewPanelFct:

    @staticmethod
    def change_grid_size():
        sender_name = self.sender().objectName
        print(sender_name)
        if sender_name:
            pass




app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
