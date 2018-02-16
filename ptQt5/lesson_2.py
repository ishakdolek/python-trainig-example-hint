import sys
from PyQt5 import QtWidgets


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Test For Test")

    okay=QtWidgets.QPushButton()
    okay.setText("Gönder")  
    cancel=QtWidgets.QPushButton("Cancel")

    h_box=QtWidgets.QHBoxLayout()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    pencere.show()
    sys.exit(app.exec_())


Pencere()
