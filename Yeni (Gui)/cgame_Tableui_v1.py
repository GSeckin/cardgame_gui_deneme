
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
import random


class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.win = uic.loadUi(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\cardgame_Table6.ui")

        # self.win.btpush1.clicked.connect(self.taslak_kart_dagit)
        # self.win.btpush2.clicked.connect(self.taslak_random_card)

        self.win.show()


    # def taslak_kart_dagit(self):
    #     im_cardback = QPixmap(r'C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\card_hand_tiltedx3_27percent.jpg')
    #     self.win.clabelA.setPixmap(im_cardback)
    #     self.win.clabelB.setPixmap(im_cardback)
    #     self.win.clabelC.setPixmap(im_cardback)
    
    # def taslak_random_card(self):
    #     im_card = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\deste_taslak1\maça_4.png")
    #     self.win.clabel1.setPixmap(im_card)
    #     im_card = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\deste_taslak1\karo_6.png")
    #     self.win.clabel2.setPixmap(im_card)
    #     im_card = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\deste_taslak1\kupa_10.png")
    #     self.win.clabel3.setPixmap(im_card)
    #     im_card = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\deste_taslak1\kupa_vale.png")
    #     self.win.clabel4.setPixmap(im_card)
    #     im_card = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\deste_taslak1\sinek_papaz.png")
    #     self.win.clabel5.setPixmap(im_card)
    #     im_card = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\deste_taslak1\karo_as.png")
    #     self.win.clabel6.setPixmap(im_card)
    #     im_card = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\deste_taslak1\maça_kız.png")
    #     self.win.clabel7.setPixmap(im_card)
 
    def gui_kartoyna(self,card_to_be_played):
        im_card_played = QPixmap(card_to_be_played.photo) 
        self.win.clabelMiddle.setPixmap(im_card_played)
    
    def gui_arrow_down(self):
        self.win.lbl_arrow_up.hide()
        self.win.lbl_arrow_down.show()
    
    def gui_arrow_up(self):
        self.win.lbl_arrow_up.show()
        self.win.lbl_arrow_down.hide()

    def gui_oyun_sirasi(self,shuffled_oyun_sirasi):
        self.win.lbl_sira_p1.setText(shuffled_oyun_sirasi[0].playername)
        shuffled_oyun_sirasi[0].gui_label = Ana.win.lbl_sira_p1
        self.win.lbl_sira_p2.setText(shuffled_oyun_sirasi[1].playername)
        shuffled_oyun_sirasi[1].gui_label = Ana.win.lbl_sira_p2
        self.win.lbl_sira_p3.setText(shuffled_oyun_sirasi[2].playername)
        shuffled_oyun_sirasi[2].gui_label = Ana.win.lbl_sira_p3
        self.win.lbl_sira_p4.setText(shuffled_oyun_sirasi[3].playername)
        shuffled_oyun_sirasi[3].gui_label = Ana.win.lbl_sira_p4

    def gui_highlight_turn(self,current_oyuncu_el):
        temporary = current_oyuncu_el.gui_label
        self.win.temporary.setFont(QtGui.QFont("Verdana",weight=QtGui.QFont.Bold))
        
    # def gui_turn_start_ng(self):


    def gui_el_playerABC(self,shuffled_list):
        if shuffled_list[0].playertype == "user":
            self.win.plabelA.setText(shuffled_list[1].playername)
            self.win.plabelB.setText(shuffled_list[2].playername)
            self.win.plabelC.setText(shuffled_list[3].playername)
        elif shuffled_list[1].playertype == "user":
            self.win.plabelA.setText(shuffled_list[2].playername)
            self.win.plabelB.setText(shuffled_list[3].playername)
            self.win.plabelC.setText(shuffled_list[0].playername)
        elif shuffled_list[2].playertype == "user":
            self.win.plabelA.setText(shuffled_list[3].playername)
            self.win.plabelB.setText(shuffled_list[0].playername)
            self.win.plabelC.setText(shuffled_list[1].playername)
        elif shuffled_list[3].playertype == "user":
            self.win.plabelA.setText(shuffled_list[0].playername)
            self.win.plabelB.setText(shuffled_list[1].playername)
            self.win.plabelC.setText(shuffled_list[2].playername)

        im_el_dolu = QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\card_hand_tiltedx3_27percent.jpg")
        self.win.clabelA.setPixmap(im_el_dolu)
        self.win.clabelB.setPixmap(im_el_dolu)
        self.win.clabelC.setPixmap(im_el_dolu)

    # def gui_el_goster1(self,current_oyuncu_el):
    #     if len(current_oyuncu_el.cards) < 14:
    #         num_el_goster = 0
    #         list_bt_El = [bt_El_1,bt_El_2,bt_El_3,bt_El_4,bt_El_5,bt_El_6,bt_El_7,bt_El_8,bt_El_9,bt_El_10,bt_El_11,bt_El_12,bt_El_13]
    #         for card_variable in current_oyuncu_el.cards:
    #             im_card_el_temp = QIcon(card_variable.photo) 
    #             self.win.list_bt_El[num_el_goster].setIcon(im_card_el_temp)
    #             num_el_goster += 1
    #     else:
    #         print("HATA !!!!!!!!\nSayıyı geçtiniz\nsayıyı geçtiniz\nsayıyı geçtiniz\nsayıyı geçtiniz\n")

    def gui_el_goster(self,current_oyuncu_el):
        if len(current_oyuncu_el.cards) == 1:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_4.setIcon(im_card_el_1)
        elif len(current_oyuncu_el.cards) == 2:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_3.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_4.setIcon(im_card_el_2)
        elif len(current_oyuncu_el.cards) == 3:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_3.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_4.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_5.setIcon(im_card_el_3)
        elif len(current_oyuncu_el.cards) == 4:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_2.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_3.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_4.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_5.setIcon(im_card_el_4)
        elif len(current_oyuncu_el.cards) == 5:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_2.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_3.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_4.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_5.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_6.setIcon(im_card_el_5)
        elif len(current_oyuncu_el.cards) == 6:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_1.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_2.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_3.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_4.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_5.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_6.setIcon(im_card_el_6)
        elif len(current_oyuncu_el.cards) == 7:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_1.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_2.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_3.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_4.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_5.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_6.setIcon(im_card_el_6)
            im_card_el_7 = QIcon(current_oyuncu_el.cards[6].photo) 
            self.win.bt_El_7.setIcon(im_card_el_7)
        elif len(current_oyuncu_el.cards) == 8:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_9.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_1.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_2.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_3.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_4.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_5.setIcon(im_card_el_6)
            im_card_el_7 = QIcon(current_oyuncu_el.cards[6].photo) 
            self.win.bt_El_6.setIcon(im_card_el_7)
            im_card_el_8 = QIcon(current_oyuncu_el.cards[7].photo) 
            self.win.bt_El_7.setIcon(im_card_el_8)
        elif len(current_oyuncu_el.cards) == 9:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_9.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_1.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_2.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_3.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_4.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_5.setIcon(im_card_el_6)
            im_card_el_7 = QIcon(current_oyuncu_el.cards[6].photo) 
            self.win.bt_El_6.setIcon(im_card_el_7)
            im_card_el_8 = QIcon(current_oyuncu_el.cards[7].photo) 
            self.win.bt_El_7.setIcon(im_card_el_8)
            im_card_el_9 = QIcon(current_oyuncu_el.cards[8].photo) 
            self.win.bt_El_8.setIcon(im_card_el_9)
        elif len(current_oyuncu_el.cards) == 10:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_11.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_9.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_1.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_2.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_3.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_4.setIcon(im_card_el_6)
            im_card_el_7 = QIcon(current_oyuncu_el.cards[6].photo) 
            self.win.bt_El_5.setIcon(im_card_el_7)
            im_card_el_8 = QIcon(current_oyuncu_el.cards[7].photo) 
            self.win.bt_El_6.setIcon(im_card_el_8)
            im_card_el_9 = QIcon(current_oyuncu_el.cards[8].photo) 
            self.win.bt_El_7.setIcon(im_card_el_9)
            im_card_el_10 = QIcon(current_oyuncu_el.cards[9].photo) 
            self.win.bt_El_8.setIcon(im_card_el_10)
        elif len(current_oyuncu_el.cards) == 11:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_11.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_9.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_1.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_2.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_3.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_4.setIcon(im_card_el_6)
            im_card_el_7 = QIcon(current_oyuncu_el.cards[6].photo) 
            self.win.bt_El_5.setIcon(im_card_el_7)
            im_card_el_8 = QIcon(current_oyuncu_el.cards[7].photo) 
            self.win.bt_El_6.setIcon(im_card_el_8)
            im_card_el_9 = QIcon(current_oyuncu_el.cards[8].photo) 
            self.win.bt_El_7.setIcon(im_card_el_9)
            im_card_el_10 = QIcon(current_oyuncu_el.cards[9].photo) 
            self.win.bt_El_8.setIcon(im_card_el_10)
            im_card_el_11 = QIcon(current_oyuncu_el.cards[10].photo) 
            self.win.bt_El_10.setIcon(im_card_el_11)
        elif len(current_oyuncu_el.cards) == 12:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_13.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_11.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_9.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_1.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_2.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_3.setIcon(im_card_el_6)
            im_card_el_7 = QIcon(current_oyuncu_el.cards[6].photo) 
            self.win.bt_El_4.setIcon(im_card_el_7)
            im_card_el_8 = QIcon(current_oyuncu_el.cards[7].photo) 
            self.win.bt_El_5.setIcon(im_card_el_8)
            im_card_el_9 = QIcon(current_oyuncu_el.cards[8].photo) 
            self.win.bt_El_6.setIcon(im_card_el_9)
            im_card_el_10 = QIcon(current_oyuncu_el.cards[9].photo) 
            self.win.bt_El_7.setIcon(im_card_el_10)
            im_card_el_11 = QIcon(current_oyuncu_el.cards[10].photo) 
            self.win.bt_El_8.setIcon(im_card_el_11)
            im_card_el_12 = QIcon(current_oyuncu_el.cards[11].photo) 
            self.win.bt_El_10.setIcon(im_card_el_12)
        elif len(current_oyuncu_el.cards) == 13:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_13.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_11.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_9.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_1.setIcon(im_card_el_4)
            im_card_el_5 = QIcon(current_oyuncu_el.cards[4].photo) 
            self.win.bt_El_2.setIcon(im_card_el_5)
            im_card_el_6 = QIcon(current_oyuncu_el.cards[5].photo) 
            self.win.bt_El_3.setIcon(im_card_el_6)
            im_card_el_7 = QIcon(current_oyuncu_el.cards[6].photo) 
            self.win.bt_El_4.setIcon(im_card_el_7)
            im_card_el_8 = QIcon(current_oyuncu_el.cards[7].photo) 
            self.win.bt_El_5.setIcon(im_card_el_8)
            im_card_el_9 = QIcon(current_oyuncu_el.cards[8].photo) 
            self.win.bt_El_6.setIcon(im_card_el_9)
            im_card_el_10 = QIcon(current_oyuncu_el.cards[9].photo) 
            self.win.bt_El_7.setIcon(im_card_el_10)
            im_card_el_11 = QIcon(current_oyuncu_el.cards[10].photo) 
            self.win.bt_El_8.setIcon(im_card_el_11)
            im_card_el_12 = QIcon(current_oyuncu_el.cards[11].photo) 
            self.win.bt_El_10.setIcon(im_card_el_12)
            im_card_el_13 = QIcon(current_oyuncu_el.cards[12].photo) 
            self.win.bt_El_12.setIcon(im_card_el_13)

        else:
            print("HATA !!!!!!!!\nSayıyı geçtiniz\nsayıyı geçtiniz\nsayıyı geçtiniz\nsayıyı geçtiniz\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())
    