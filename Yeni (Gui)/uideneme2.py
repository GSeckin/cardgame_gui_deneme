
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
        self.kontrolsayisi = 0
        self.cevap_genel = "a"
        self.cevap_genel_kontrol = 0
        self.win.pushButton_5.clicked.connect(self.bas_butona)
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

    def kontrolsayisi(self):
        self.kontrolsayisi = 0
    
    def bas_butona(self):
        self.cevap_genel = "b"
        self.cevap_genel_kontrol = 1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    print("Merhaba")
    cevap1 = input("Bir meyve yazın:\n")
    print("Cevabınız: {}\n".format(cevap1))
    # time.sleep(2)

    window = Ana()

    # while window.cevap_genel_kontrol == 0:
    #     time.sleep(1)
    #     print("a")
        
    #     # sayi = 0
    #     # sayi += 1
    #     # print(sayi)

    while window.cevap_genel_kontrol == 0:
        window.cevap_genel = input("cevap_genel bekliyorum\n")
    
    # if window.cevap_genel == "a":
    #     print("a")
    # if window.cevap_genel == "b":
    #     print("b")

    print("Bitti Bitti Bitti Bitti Bitti Bitti Bitti Bitti Bitti Bitti  Bitti")
    # # time.sleep(10)
    # print("Yazı yazı yazı")
    # # time.sleep(6)
    # cevap2 = input("Bir de sebze yazın:\n")
    # print("Cevabınız: {}".format(cevap2))
    
    # window.adim2()

    # print("Adım 2\n")
    # cevap3 = input("3.adımı da çalıştıralım mı?\n")
    # print("hemen çalıştırıyorum\n")

    # window.adim3()

    # print("onu da çalıştırdık\n")
    # time.sleep(3)

    

    sys.exit(app.exec_())
    