
import sys
import PyQt5
# from PyQt5 import *
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
# from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
import time



class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.win = uic.loadUi(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\untitled.ui")
        self.win.show()
        self.adim1()
        # self.adim2()
        # self.adim3()
        


    def adim1(self):
        # time.sleep(1)
        self.win.label_5.setText("Birinci Adım")
    def adim2(self):
        # time.sleep(2)
        self.win.label_5.setText("İkinci Adım")
    def adim3(self):
        # time.sleep(7)
        self.win.label_5.setText("Üçüncü Adım")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    print("Merhaba")
    cevap1 = input("Bir meyve yazın:\n")
    print("Cevabınız: {}\n".format(cevap1))
    # time.sleep(2)

    window = Ana()

    # time.sleep(10)
    print("Yazı yazı yazı")
    # time.sleep(6)
    cevap2 = input("Bir de sebze yazın:\n")
    print("Cevabınız: {}".format(cevap2))
    
    window.adim2()

    print("Adım 2\n")
    cevap3 = input("3.adımı da çalıştıralım mı?\n")
    print("hemen çalıştırıyorum\n")

    window.adim3()

    print("onu da çalıştırdık\n")
    time.sleep(3)

    

    sys.exit(app.exec_())
    