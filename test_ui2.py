import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow

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
        self.gridsizeslider.sliderMoved.connect(self.change_grid_size1)
        self.gridsizeSpinBox.valueChanged.connect(self.change_grid_size2)



    def create_graph(self, e):
        print("button clicked")
        print(self.sender().objectName())

    def change_grid_size1(self):
        #print(self.gridsizeslider.sliderPosition())
        #print(self.sender().value())
        val = self.sender().value()
        self.gridsizeSpinBox.setValue(val)
        #self.gridsizeslider.setValue(val)

    def change_grid_size2(self):
        #print(self.gridsizeslider.sliderPosition())
        #print(self.sender().value())
        val = self.sender().value()
        #self.gridsizeSpinBox.setValue(val)
        self.gridsizeslider.setValue(val)

        pass

    def get_preview_input(self):
        print(dir(self.sender()))


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
