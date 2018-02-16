import sys
from PyQt5 import QtWidgets

def Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Test For Test")
    
    etiket1=QtWidgets.QLabel(pencere)
    etiket1.setText("Ben bir test sürecindeyim")
    etiket1.move(200,30)

    # etiket1.setPixmap("resim_yolu.png")
    
    pencere.show()
    sys.exit(app.exec_())
Pencere()
