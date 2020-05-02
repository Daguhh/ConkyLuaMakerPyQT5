import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("ConkyLuaMakerPyQt5.ui")
window.show()
app.exec()
