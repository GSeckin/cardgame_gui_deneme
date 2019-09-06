import random
import time
import sys 

import PyQt5
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap


########## İskambil Oyunu için Kod
########## Hazırlayan: Görkem Seçkin
########## Başlangıç Tarihi: 15 Nisan 2019
########## Son Düzenleme Tarihi:  2019

########## list_types ve list_card_values, Iskambil class'ının instance attribute'una verilmek için;cardType,cardValue
list_types = ["kupa","karo","maça","sinek"]
list_card_values = ["as",2,3,4,5,6,7,8,9,10,"vale","kız","papaz"]
########## list_abcd ve dict_for_creating sadece instance yaratmak için tek sefer kullanılıyor.
list_abcd = ["A","B","C","D"]
########## list_13 hem instance yaratmak hem de Iskambil class'ının instance attribute'una verilmek için var;cardValue_int
list_13 = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
dict_for_creating = {}
for a in range(0,13):
    for b in range(0,4):
        dict_for_creating.update({ (list_abcd[b] + list_13[a]) : [list_types[b],list_card_values[a],list_13[a]] })

########## oyun_raporu, oyun sırasında bütün olanları not ediyor
oyun_raporu = "\n\t\t\t OYUN RAPORU\n"


########## Bir destedeki bütün kağıtlar Iskambil class'ının instance'ı olarak tanımlanır. 
class Iskambil:
    tanimli = []
    def __init__(self,cardType,cardValue,cardValue_int):
        self.type = cardType
        self.value = cardValue
        self.value_int = cardValue_int
        self.name = "{}_{}".format(self.type,self.value)
        self.tanimli.append(self.name)
        self.mark10 = ""
        self.markAS = ""
        self.mark7 = 2
        self.photo = "C:\\Users\\Görkem\\Documents\\GitHub\\Python6Desktop\\Yeniler\\deste_taslak1\\" + self.name + ".png" 

########## all_cards (52 iskambil kağıdı instance'larını içeren bir liste) oluşturuluyor.
all_cards = []
for a in dict_for_creating:
    all_cards.append(Iskambil(dict_for_creating[a][0],dict_for_creating[a][1],int(dict_for_creating[a][2])))

########## dict_lookup (bütün iskambil kağıtlarının all_cards'daki index numarasını bize gösteren bir dictionary. İleride kullanım amaçlı.
dict_lookup = {}
integer1 = 0
for a in Iskambil.tanimli:
    dict_lookup.update({ a : integer1 })
    integer1 +=1

########## Oyun oynanırken, ortada en üstteki kağıdın değerini tutuyor. Girdi olarak bir iskambil kağıdı instance'ı alıyor.
class Orta:
    ortada = []
    def __init__(self, card_instance):
        self.type = card_instance.type
        self.value = card_instance.value
        self.value_int = card_instance.value_int
        self.ortada.append(card_instance)
        self.ortadaki_kart = card_instance
        if self.value == "vale":
            global secim
            self.type = secim
    
    @classmethod
    def baslangic(cls):
        kart_degil = Iskambil("sinek",0,0)
        return Orta(kart_degil)

########## Karışık sıralanmış 52 kağıtlık deste oluşturuyor. all_cards listesini kullanıyor. Çıktı: deck adında liste. random modülünü kullanıyor.
def create_deck():
        sayi_listesi = list(range(52))
        random.shuffle(sayi_listesi)
        deck = []
        for i in sayi_listesi:
            deck.append(all_cards[i]) 
        return deck

########## Desteyi karıyor. deck adlı listenin elemanlarının sırasını depiştiriyor. Çıktı: deck adında liste. random modülünü kullanıyor.      
def shuffle_deck(input_deck):
    random.shuffle(input_deck)
    return input_deck

########## Bir oyuncunun eli. yeni_el, verilen sayıda kağıdı desteden çekip self.cards listesine ekliyor.
############### game eklemesi: self.playertype, bilgisayar ise 111, eğer kullanıcı ise string olarak kaydedilecek
############### game eklemesi: yeni_el_user(), kullanıcıya el oluşturmak için
class El:
    def __init__(self,player):
        self.playername = str(player)
        self.cards = []
        self.gui_label = 0

    def yeni_el(self,a):
        self.cards = [deck.pop(0) for i in range(a)]
        self.playertype = 111

    def yeni_el_user(self,a):
        self.cards = [deck.pop(0) for i in range(a)]
        self.playertype = "user"



class Tur:
    def __init__(self,oyuncu_el):
        self.oyuncu = oyuncu_el
        if orta.value == 7:
            cards_7 = []
            for card in self.oyuncu.cards:
                if card.value == 7:
                    cards_7.append(card)
            if len(cards_7) != 0:
                selected_7 = random.choice(cards_7)
                selected_7.mark7 += orta.ortadaki_kart.mark7
                self.kart_oyna(selected_7)

            else: 
                self.kart_cek(orta.ortadaki_kart.mark7)
                self.olasi_hamleleri_bul()
                if len(self.hamleler) == 0:
                    self.kart_cek(1)
                    self.olasi_hamleleri_bul()
                    if len(self.hamleler) != 0:
                        self.kart_oyna(random.choice(self.hamleler))
                else:
                    self.kart_oyna(random.choice(self.hamleler))
        else:
            self.olasi_hamleleri_bul()
            if len(self.hamleler) == 0:
                self.kart_cek(1)
                self.olasi_hamleleri_bul()
                if len(self.hamleler) != 0:
                    self.kart_oyna(random.choice(self.hamleler))
            else:
                self.kart_oyna(random.choice(self.hamleler))

    def olasi_hamleleri_bul(self):
        global oyun_raporu
        self.hamleler = []
        for card in self.oyuncu.cards:
            if card.type == orta.type:
                self.hamleler.append(card)
            elif card.value == orta.value:
                self.hamleler.append(card)
            elif card.value == "vale":
                self.hamleler.append(card)
        if i < 4:
            hamleler_ilk_tur = []
            for card in self.hamleler:
                if card.type != "sinek":
                    continue
                if card.value == "as" or card.value == 7 or card.value == 10 or card.value == "vale":
                    continue
                hamleler_ilk_tur.append(card)
            self.hamleler = hamleler_ilk_tur
        oyun_raporu += "olası hamleler: {}\n".format([h.name for h in self.hamleler])
        

########## kart_cek'te, tek deste oynandığı için "if len(deck) < 8: ifadesi" var. 
##########Eğer çift deste oynanırsa, burayı 16 yap! (çünkü bir anda çekilebilecek max. kart sayısı 16 olur(8tane7))
    def kart_cek(self,a):
        global deck
        global oyun_raporu
        
        try:
            global orta
            oyun_raporu += "\ndeste uzunluğu, kart çekemeden önce: {}\n".format(len(deck))
            cards_to_be_drawn = [deck.pop(0) for i in range(a)]
            self.oyuncu.cards.extend(cards_to_be_drawn)
            print("\n{} {} kart çekti".format(self.oyuncu.playername,a))
            time.sleep(1)
            oyun_raporu += "deste uzunluğu, kart çektiktikten sonra: {}\n".format(len(deck))
            oyun_raporu += "{}'in yeni eli: {}\n".format(self.oyuncu.playername,[k.name for k in self.oyuncu.cards])
            if len(deck) < 8:
                print("\ndestedeki kart sayısı:",len(deck))
                time.sleep(1)
                oyun_raporu += "\ndestedeki kart sayısı: {}\n".format(len(deck))
                oyun_raporu += "ortadaki kart sayısı: {}\n".format(len(orta.ortada))
                temporary_deck1 = orta.ortada[1:-1]
                temporary_deck1 = shuffle_deck(temporary_deck1)
                deck.extend(temporary_deck1)
                Orta.ortada = [orta.ortada[0],orta.ortada[-1]]
                for card in deck:
                    card.mark10 = ""
                    card.markAS = ""
                    card.mark7 = 2
                print("ortadaki kağıtlar karılıp yeni deste yapıldı")
                time.sleep(1)
                oyun_raporu += "ortadaki kağıtlar karılıp yeni deste yapıldı\n"
                time.sleep(1)
                print("destedeki kart sayısı:{}".format(len(deck)))
                time.sleep(1)
                oyun_raporu += "destedeki kart sayısı:{}\n".format(len(deck))
                oyun_raporu += "Deste:{}\n".format([k.name for k in deck])
                oyun_raporu += "ortada kalanlar: {}\n".format([k.name for k in orta.ortada])
        except Exception as hata :
            print("\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck]))
            oyun_raporu += "\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck])
            print(hata)
            oyun_raporu += "Hata:{}\n".format(hata)

    def kart_oyna(self,card_instance):
        global oyun_raporu
        if card_instance.value == "vale":
            global secim
            secim = random.choice(list_types)
        global orta
        orta = Orta(card_instance)
        window.gui_kartoyna_np(card_instance)
        self.oyuncu.cards.remove(card_instance)
        print("\n\t\t\t{} {} oynadı".format(self.oyuncu.playername,card_instance.name))
        oyun_raporu += "{} {} oynadı\n".format(self.oyuncu.playername,card_instance.name)
        oyun_raporu += "ortadaki kart sayısı: {}\n".format(len(orta.ortada))
        if card_instance.value == "vale":
            print("valeden dolayı değişen orta: {}".format(secim))
            oyun_raporu += "valeden dolayı değişen orta: {}\n".format(secim)


 

############# Tutorial için Tur_user class'ı, oyunu öğrenmek isteyen kullanıcı için uyarlanmış Tur class'ı

class Tur_normalgame:
    def __init__(self,oyuncu_el):
        self.oyuncu = oyuncu_el

        time.sleep(1)
        print("\n\tTur sende")
        global oyun_raporu
        oyun_raporu += "\n\tTur sende\n"
        time.sleep(1)
        print("\n\tortanın değeri:\n\t{} {}".format(orta.type,orta.value))
        oyun_raporu += "\n\tortanın değeri:\n\t{} {}\n".format(orta.type,orta.value)
        time.sleep(2)
        print("\n\tElinde {} kart var".format(len(self.oyuncu.cards)))
        oyun_raporu += "\n\tElinde {} kart var\n".format(len(self.oyuncu.cards))
        time.sleep(1)
        print("\n\t{}".format([k.name for k in self.oyuncu.cards]))
        oyun_raporu += "\n\t{}\n".format([k.name for k in self.oyuncu.cards])
        self.olasi_hamleleri_bul_ng()
        time.sleep(3)
 
        if orta.value == 7:
            cards_7 = []
            for card in self.oyuncu.cards:
                if card.value == 7:
                    cards_7.append(card)
            kontrolt3 = 0
            # while kontrolt3 < 1:
            #     cevap_tur3 = str(input("\n\tOyna!\n\t< kart çek / kart oyna >\n\t")).lower()
            #     cevap_tur3.strip()
            #     if cevap_tur3 == "kart çek":
            #         kontrolt3 = 1
            #         self.kart_cek_user_ng(orta.ortadaki_kart.mark7)
            #         self.olasi_hamleleri_bul_ng()
            #     elif cevap_tur3 == "kart oyna":
            #         kontrolt3 = 1
            #         kontrol_r3 = self.hamle_sec_user_ng7(cards_7)
            #         if kontrol_r3 == 0:
            #             kontrolt3 = 0
            #         else:
            #             kontrol_r3.mark7 += orta.ortadaki_kart.mark7
            #             self.kart_oyna_user_ng(kontrol_r3)
                # else:
                #     print("\n\tGeçerli bir cevap vermedin")
                #     time.sleep(1)
                #     print("\n\tBir daha dene")
                #     time.sleep(1)

        kontrolt1 = 0
        kontrolt2 = 0
        # while kontrolt1 < 1:
        #     cevap_tur1 = str(input("\n\tOyna!\n\t< kart çek / kart oyna >\n\t")).lower()
        #     cevap_tur1.strip()
        #     if cevap_tur1 == "kart çek":
        #         kontrolt1 = 1
        #         self.kart_cek_user_ng(1)
        #         self.olasi_hamleleri_bul_ng()
        #     elif cevap_tur1 == "kart oyna":
        #         kontrolt1 = 1
        #         kontrol_r1 = self.hamle_sec_user_ng()
        #         if kontrol_r1 == 0:
        #             kontrolt1 = 0
        #         else: 
        #             self.kart_oyna_user_ng(kontrol_r1)
        #             kontrolt2 = 1
        #     else:
        #         print("\n\tGeçerli bir cevap vermedin")
        #         time.sleep(1)
        #         print("\n\tBir daha dene")
        #         time.sleep(1)
        
        # while kontrolt2 < 1:
        #     cevap_tur2 = str(input("\n\tOyna!\n\t< kart oyna / turu bitir>\n\t")).lower()
        #     cevap_tur2.strip()
        #     if cevap_tur2 == "kart oyna":
        #         kontrolt2 = 1
        #         kontrol_r1 = self.hamle_sec_user_ng()
        #         if kontrol_r1 == 0:
        #             kontrolt2 = 0
        #         else: 
        #             self.kart_oyna_user_ng(kontrol_r1)
        #     elif cevap_tur2 == "turu bitir":
        #         kontrolt2 = 1
        #         time.sleep(1)
        #         print("\n\tTurun bitti.\n")
        #     else:
        #         print("\n\tGeçerli bir cevap vermedin")
        #         time.sleep(1)
        #         print("\n\tBir daha dene")
        #         time.sleep(1)
                    
    
    def olasi_hamleleri_bul_ng(self):
        global oyun_raporu
        self.hamleler = []
        for card in self.oyuncu.cards:
            if card.type == orta.type:
                self.hamleler.append(card)
            elif card.value == orta.value:
                self.hamleler.append(card)
            elif card.value == "vale":
                self.hamleler.append(card)
        if i < 4:
            hamleler_ilk_tur = []
            for card in self.hamleler:
                if card.type != "sinek":
                    continue
                if card.value == "as" or card.value == 7 or card.value == 10 or card.value == "vale":
                    continue
                hamleler_ilk_tur.append(card)
            self.hamleler = hamleler_ilk_tur
        oyun_raporu += "olası hamleler: {}\n".format([h.name for h in self.hamleler])

    def kart_cek_user_ng(self,a):
        global deck
        global oyun_raporu
        try:
            global orta
            time.sleep(1)
            oyun_raporu += "\ndeste uzunluğu, kart çekemeden önce: {}\n".format(len(deck))
            cards_to_be_drawn = [deck.pop(0) for i in range(a)]
            self.oyuncu.cards.extend(cards_to_be_drawn)
            print("\n\t{} kart çektin".format(a))
            oyun_raporu += "\n\t{} kart çektin\n".format(a)
            time.sleep(1)
            oyun_raporu += "deste uzunluğu, kart çektiktikten sonra: {}\n".format(len(deck))
            print("\n\tÇektiğin kartlar\n\t{}".format([k.name for k in cards_to_be_drawn]))
            oyun_raporu += "\n\tÇektiğin kartlar\n\t{}\n".format([k.name for k in cards_to_be_drawn])
            if len(deck) < 8:
                print("\ndestedeki kart sayısı: {}".format(len(deck)))
                oyun_raporu += "\ndestedeki kart sayısı: {}\n".format(len(deck))
                oyun_raporu += "ortadaki kart sayısı: {}\n".format(len(orta.ortada))
                temporary_deck1 = orta.ortada[1:-1]
                temporary_deck1 = shuffle_deck(temporary_deck1)
                deck.extend(temporary_deck1)
                Orta.ortada = [orta.ortada[0],orta.ortada[-1]]
                for card in deck:
                    card.mark10 = ""
                    card.markAS = ""
                    card.mark7 = 2
                print("ortadaki kağıtlar karılıp yeni deste yapıldı")
                oyun_raporu += "ortadaki kağıtlar karılıp yeni deste yapıldı\n"
                time.sleep(1)
                print("destedeki kart sayısı:",len(deck))
                oyun_raporu += "destedeki kart sayısı: {}\n".format(len(deck))
                oyun_raporu += "Deste: {}\n".format([k.name for k in deck])
                oyun_raporu += "ortada kalanlar: {}\n".format([k.name for k in orta.ortada])
                time.sleep(2)
        except Exception as hata :
            print("\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck]))
            oyun_raporu += "\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck])
            print(hata)
            oyun_raporu += "Hata: {}\n".format(hata)

    def hamle_sec_user_ng(self):
        global oyun_raporu
        kontrol1 = 0
        while kontrol1 < 1:
            time.sleep(1)
            print("\n\tElindeki kartlar:\n\t{}".format([k.name for k in self.oyuncu.cards]))
            oyun_raporu += "\n\tElindeki kartlar:\n\t{}\n".format([k.name for k in self.oyuncu.cards])
            cevap_hamle_sec = str(input("\n\tHangi kartı oynamak istersin?\n\tgeri dönmek istiyorsan <geri> yaz\n\t")).lower()
            oyun_raporu += "\n\toynanmak istenen kart: {}\n".format(cevap_hamle_sec)
            for card in self.hamleler:
                if card.name == cevap_hamle_sec:
                    hamle = card
                    kontrol1 = 1
                    return hamle
            if cevap_hamle_sec == "geri":
                return 0
            elif i < 4:
                print("\n\tTur ilk kez sana geldi\n\tİlk turda 7'li, 10'lu, 'vale' veya 'as' oynayamazsın,\n\tve sadece 'sinek' oynayabilirsin")
                time.sleep(2)
                print("\n\tElinde uygun kart yoksa kart çek\n\t")
            else:    
                print("\n\tOynayabileceğin bir kartı yazmadın")
                oyun_raporu += "\n\tOynayabileceğin bir kartı yazmadın\n"
                time.sleep(1)
                cevap_info = str(input("\n\tKart oynama kurallarına gözatmak ister misin?\n\tKurallara bakmak için <e>, geçmek için <h> yaz\n\t")).lower()
                cevap_info2 = cevap_info.lstrip("<")
                cevap_info3 = cevap_info2.rstrip(">")
                if cevap_info == "e":
                    print("Bir kartı oynayabilmen için şu 3 koşuldan en az birini sağlamassı lazım:\n\t_ kartın değeri, ortanın değeriyle aynı\n\t_ kartın şekli, ortanın şekliyle aynı\n\t_ vale (ortanın değeri ya da şeklinden bağımsız, her an oynanabilir\n\t)")

    def hamle_sec_user_ng7(self,cards_7):
        global oyun_raporu
        kontrol1 = 0
        while kontrol1 < 1:
            time.sleep(1)
            print("\n\tElindeki kartlar:\n\t{}".format([k.name for k in self.oyuncu.cards]))
            oyun_raporu += "\n\tElindeki kartlar:\n\t{}\n".format([k.name for k in self.oyuncu.cards])
            cevap_hamle_sec = str(input("\n\tHangi kartı oynamak istersin?\n\tgeri dönmek istiyorsan <geri> yaz\n\t")).lower()
            oyun_raporu += "\n\toynanmak istenen kart: {}\n".format(cevap_hamle_sec)
            for card in cards_7:
                if card.name == cevap_hamle_sec:
                    hamle = card
                    kontrol1 = 1
                    return hamle
            if cevap_hamle_sec == "geri":
                return 0
            else:    
                print("\n\tOynayabileceğin bir kartı yazmadın")
                oyun_raporu += "\n\tOynayabileceğin bir kartı yazmadın\n"
                time.sleep(1)
                print("\n\tEn son {} oynandı".format(orta.ortadaki_kart.name))
                oyun_raporu += "\n\tEn son {} oynandı\n".format(orta.ortadaki_kart.name)
                time.sleep(1)
                print("\n\tEğer elinde 7'li varsa, onu oynayabilirsin")
                oyun_raporu += "\n\tEğer elinde 7'li varsa, onu oynayabilirsin\n"
                time.sleep(1)
                print("\n\tYoksa, kart çekmek zorundasın")
                oyun_raporu += "\n\tYoksa, kart çekmek zorundasın"
                time.sleep(1)

    def kart_oyna_user_ng(self,card_instance):
        global oyun_raporu
        if card_instance.value == "vale":
            time.sleep(1)
            cevap_vale = str(input("\n\tOrta ne olsun istersin?\n\t<kupa/karo/maça/sinek>\n\t")).lower()
            global secim
            secim = cevap_vale
        global orta
        orta = Orta(card_instance)
        self.oyuncu.cards.remove(card_instance)
        time.sleep(1)
        print("\n\t{} oynadın".format(card_instance.name))
        oyun_raporu += "\n\t{} oynadın\n".format(card_instance.name)
        time.sleep(1)
        oyun_raporu += "\n\tElindekiler\n\t{}\n".format([k.name for k in self.oyuncu.cards])
        oyun_raporu += "\nortadaki kart sayısı: {}\n".format(len(orta.ortada))
        if card_instance.value == "vale":
            print("valeden dolayı değişen orta: {}".format(secim))
            oyun_raporu += "valeden dolayı değişen orta: {}\n".format(secim)
            time.sleep(1)        
 


def giris_karsilama():
    karsilama_yazisi = """
    \n\t\t\tPYTHON'LA OYNAYALIM
    \n\tMerhaba,\n\tPis Yedili oyununa hoşgeldin!\n
    """
    print("_"*125)
    print(karsilama_yazisi)
    time.sleep(2)
    # cevap1 = str(input("\n\tPis Yedili oynamayı biliyor musun?\n<Evet/Hayır>\n")).lower()
    # if cevap1 == "evet":
    #     print("\n\tHemen başlayalım!")
    #     time.sleep(2)
    # else:
    #     print("\n\tplaceholder text")
    #     time.sleep(2)
    cevap2 = str(input("\n\tÖncelikle, adını aşağıya yazar mısın?\n"))
    print("\n\tTeşekkürler {}".format(cevap2))
    time.sleep(2)
    print("\n\tKartları dağıtmaya başlıyorum")
    time.sleep(1)
    return cevap2
    

def oyunabasla():
    # dosya = open("C:\My folder for Visual Studio Code\cardgame\cardgame_game_tutorial_ciktilari\\v2_normalgame3.txt","w+")

    global orta
    orta = Orta.baslangic()
    global deck
    deck = create_deck()
    global oyun_raporu
    oyun_raporu += "Oyun başlatıldı\n"

    global window
    window = Ana()

    user_playername = giris_karsilama()
    oyun_raporu += "Oyuncunun(kullanıcı) adı: {}\n".format(user_playername)

    # print("-----KONTROL before window-----")
    # window = Ana()
    # print("-----KONTROL after window-----")


    oyun_raporu += "oyundaki kart sayısı: {}\n52 kart + başlangıçta ortayı belirten 'kart',(joker yok)\n".format(len(Iskambil.tanimli))
    oyun_raporu += "Destedeki kartlar, sırayla:\n{}\n".format([k.name for k in deck])
    
    # time.sleep(1)
    oyuncu1_el = El("oyuncu1")
    oyuncu1_el.yeni_el(7)
    # print("\n{}, 7 kartı var".format(oyuncu1_el.playername))
    oyun_raporu += "Oyuncu1'in eli: {}\n".format([k.name for k in oyuncu1_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])
    # time.sleep(1)
    oyuncu2_el = El("oyuncu2")
    oyuncu2_el.yeni_el(7)
    # print("{}, 7 kartı var".format(oyuncu2_el.playername))
    oyun_raporu += "Oyuncu2'nin eli: {}\n".format([k.name for k in oyuncu2_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])
    # time.sleep(1)
    oyuncu3_el = El("oyuncu3")
    oyuncu3_el.yeni_el(7)
    # print("{}, 7 kartı var".format(oyuncu3_el.playername))
    oyun_raporu += "Oyuncu3'ün eli: {}\n".format([k.name for k in oyuncu3_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])

    # time.sleep(2)
    user_el = El(user_playername)
    user_el.yeni_el_user(7)
    # print("\n\tElindeki kartlar:\n\t{}\n\n\n\n".format([k.name for k in user_el.cards]))
    # time.sleep(4)
    oyun_raporu += "Kullanıcının eli: {}\n".format([k.name for k in user_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])

    oyun_raporu += "başlangıçta ortada: {},{},{}\n".format(orta.type,orta.value,orta.value_int)
    list1 = [oyuncu1_el,oyuncu2_el,oyuncu3_el,user_el]
    oyun_raporu += "list1: {}\n".format([k.playername for k in list1])
    random.shuffle(list1)
    oyun_raporu += "list1 karıştırıldı: {}\n".format([k.playername for k in list1])
    # print("\n\toyun sırası:{}".format([k.playername for k in list1]))
    oyun_raporu += "oyun sırası: {}\n".format([k.playername for k in list1])
    # time.sleep(3)

    print("-----KONTROL before gui_el_player_ABC------ ")
    window.gui_el_playerABC(list1)
    # window.win.clabelMiddle.setPixmap(QPixmap(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\card_hand_tiltedx3_27percent.jpg"))
    print("-----KONTROL after gui_el_player_ABC------ ")
    window.gui_el_goster(user_el)
    window.gui_oyun_sirasi(list1)
    window.gui_arrow_down()

    # cevap_basla = 0
    # while cevap_basla == 0:
    #     if cevap_basla == 1:
    #         break
    #     else: 
    #         time.sleep(2)

    tur_limiti = 600
    global i
    i = 0

    def duz():
        global i
        global oyun_raporu
        while i < tur_limiti:
            if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                orta.ortadaki_kart.mark10 = "marked"
                print("Oyun sırası tersine döndü")
                oyun_raporu += "Oyun sırası tersine döndü"
                time.sleep(1)
                ters()
            elif orta.value == "as" and orta.ortadaki_kart.markAS == "":
                orta.ortadaki_kart.markAS = "marked"
                duz_atla()
            else:
                current = list1[0]
                # print("Sırada: {}".format(current.playername))
                oyun_raporu += "Sırada: {}\n".format(current.playername)
                del list1[0]
                list1.append(current)

                if current.playertype == "user":
                    window.gui_highlight_turn(current)
                    window.gui_arrow_down()
                    Tur_normalgame(current)
                    window.gui_el_goster(current)
                    time.sleep(1)
                    check_singlewin_user(current)

                else:
                    window.gui_highlight_turn(current)
                    window.gui_arrow_down()
                    Tur(current)
                    check_singlewin(current)

                print("orta:",orta.type,orta.value)
                oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
                time.sleep(2)
                if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                    var_for_change_list = list1[-1]
                    del list1[-1]
                    list1.insert(0,var_for_change_list)
                # print("oyun sırası: {}".format([k.playername for k in list1]))
                oyun_raporu += "oyun sırası: {}\n".format([k.playername for k in list1])
                i +=1
                oyun_raporu += "i(tur sayısı)={}\n".format(i)

    def ters():
        global i
        global oyun_raporu
        while i < tur_limiti:
            if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                orta.ortadaki_kart.mark10 = "marked"
                print("Oyun sırası tersine döndü")
                oyun_raporu += "Oyun sırası tersine döndü"
                time.sleep(1)
                duz()
            elif orta.value == "as" and orta.ortadaki_kart.markAS == "":
                orta.ortadaki_kart.markAS = "marked"
                ters_atla()
            else:
                current = list1[-1]
                # print("Sırada: {}".format(current.playername))
                oyun_raporu += "Sırada: {}\n".format(current.playername)
                del list1[-1]
                list1.insert(0,current)

                if current.playertype == "user":
                    window.gui_highlight_turn(current)
                    window.gui_arrow_up()
                    Tur_normalgame(current)
                    window.gui_el_goster(current)
                    time.sleep(1)
                    check_singlewin_user(current)

                else:
                    window.gui_highlight_turn(current)
                    window.gui_arrow_up()
                    Tur(current)
                    check_singlewin(current)

                print("orta:",orta.type,orta.value)
                oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
                time.sleep(2)
                if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                    var_for_change_list = list1[0]
                    del list1[0]
                    list1.append(var_for_change_list)
                # print("oyun sırası(tersten): {}".format([k.playername for k in list1]))
                oyun_raporu += "oyun sırası(tersten): {}\n".format([k.playername for k in list1])
                i +=1
                oyun_raporu += "i(tur sayısı)={}\n".format(i)

    def duz_atla():
        global i
        global oyun_raporu
        current = list1[0]
        # print("Sırada: {}".format(current.playername))
        oyun_raporu += "Sırada: {}\n".format(current.playername)
        del list1[0]
        list1.append(current)
        print("\n{} atlandı".format(current.playername))
        oyun_raporu += "\n{} atlandı\n".format(current.playername)
        time.sleep(1)
        print("orta:",orta.type,orta.value)
        oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
        print("oyun sırası: {}".format([k.playername for k in list1]))
        oyun_raporu += "oyun sırası: {}\n".format([k.playername for k in list1])
        i +=1
        oyun_raporu += "i(tur sayısı)={}\n".format(i)

    def ters_atla():
        global i
        global oyun_raporu
        current = list1[-1]
        # print("Sırada: {}".format(current.playername))
        oyun_raporu += "Sırada: {}\n".format(current.playername)
        del list1[-1]
        list1.insert(0,current)
        print("\n{} atlandı".format(current.playername))
        oyun_raporu += "\n{} atlandı\n".format(current.playername)
        time.sleep(1)
        print("orta:",orta.type,orta.value)
        oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
        print("oyun sırası(tersten): {}".format([k.playername for k in list1]))
        oyun_raporu += "oyun sırası(tersten): {}\n".format([k.playername for k in list1])
        i +=1
        oyun_raporu += "i(tur sayısı)={}\n".format(i)


    def check_singlewin(current_player_el):
        global i
        global oyun_raporu
        if len(current_player_el.cards) == 0:
            time.sleep(1)
            print("\n\n\tÜzgünüm,\n\t{} kazandı!\n\tonun elindeki kartlar: {}\n".format(current_player_el.playername,current_player_el.cards))
            oyun_raporu += "\n\n\tÜzgünüm,\n\t{} kazandı!\n\tonun elindeki kartlar: {}\n".format(current_player_el.playername,current_player_el.cards)
            list1.remove(current_player_el)
            endplayer1,endplayer2,endplayer3 = list1[0],list1[1],list1[2]
            time.sleep(2)
            print("Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(endplayer1.playername,[k.name for k in endplayer1.cards],endplayer2.playername,[k.name for k in endplayer2.cards],endplayer3.playername,[k.name for k in endplayer3.cards]))
            time.sleep(3)
            oyun_raporu += "Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(endplayer1.playername,[k.name for k in endplayer1.cards],endplayer2.playername,[k.name for k in endplayer2.cards],endplayer3.playername,[k.name for k in endplayer3.cards])
            oyun_raporu += "bu oyun {} tur sürdü".format(i)
            i = tur_limiti
            cevap_win = input("\n\tÇıkmak için 'enter'a tıklayın\n")


    def check_singlewin_user(current_player_el):
        global i
        global oyun_raporu
        if len(current_player_el.cards) == 0:
            time.sleep(1)
            print("\n\n\tTebrikler!\n\tBu oyunu sen kazandın!\n\telindeki kartlar: {}\n".format(current_player_el.cards))
            oyun_raporu += "\n\n\tTebrikler!\n\tBu oyunu sen kazandın!\n\telindeki kartlar: {}\n".format(current_player_el.cards)
            time.sleep(2)
            print("Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(oyuncu1_el.playername,[k.name for k in oyuncu1_el.cards],oyuncu2_el.playername,[k.name for k in oyuncu2_el.cards],oyuncu3_el.playername,[k.name for k in oyuncu3_el.cards]))
            time.sleep(3)
            oyun_raporu += "Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(oyuncu1_el.playername,[k.name for k in oyuncu1_el.cards],oyuncu2_el.playername,[k.name for k in oyuncu2_el.cards],oyuncu3_el.playername,[k.name for k in oyuncu3_el.cards])
            oyun_raporu += "bu oyun {} tur sürdü".format(i)
            i = tur_limiti
            cevap_win = input("\n\tÇıkmak için 'enter'a tıklayın\n")


    listabc = [k.playername for k in list1]

    duz()
    
    # dosya.writelines(oyun_raporu)
    # dosya.close()


class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.win = uic.loadUi(r"C:\Users\Görkem\Documents\GitHub\Python6Desktop\Yeniler\cardgame_Table6.ui")

        # self.win.btpush1.clicked.connect(self.taslak_kart_dagit)
        # self.win.btpush2.clicked.connect(self.taslak_random_card)

        self.win.bt_El_1.hide()
        self.win.bt_El_2.hide()
        self.win.bt_El_3.hide()
        self.win.bt_El_4.hide()
        self.win.bt_El_5.hide()
        self.win.bt_El_6.hide()
        self.win.bt_El_7.hide()
        self.win.bt_El_8.hide()
        self.win.bt_El_9.hide()
        self.win.bt_El_10.hide()
        self.win.bt_El_11.hide()
        self.win.bt_El_12.hide()
        self.win.bt_El_13.hide()

        self.win.show()

 
    def gui_kartoyna_np(self,card_to_be_played):
        im_card_played = QPixmap(card_to_be_played.photo) 
        self.win.clabelMiddle.setPixmap(im_card_played)

    def gui_kartoyna_p(self,card_to_be_played):
        im_card_played = QPixmap(card_to_be_played.photo) 
        self.win.clabelMiddle.setPixmap(im_card_played)
        self.gui_el_goster()
    
    def gui_arrow_down(self):
        self.win.lbl_arrow_up.hide()
        self.win.lbl_arrow_down.show()
    
    def gui_arrow_up(self):
        self.win.lbl_arrow_up.show()
        self.win.lbl_arrow_down.hide()

    def gui_oyun_sirasi(self,shuffled_oyun_sirasi):
        self.win.lbl_sira_p1.setText(shuffled_oyun_sirasi[0].playername)
        shuffled_oyun_sirasi[0].gui_label = window.win.lbl_sira_p1
        self.win.lbl_sira_p2.setText(shuffled_oyun_sirasi[1].playername)
        shuffled_oyun_sirasi[1].gui_label = window.win.lbl_sira_p2
        self.win.lbl_sira_p3.setText(shuffled_oyun_sirasi[2].playername)
        shuffled_oyun_sirasi[2].gui_label = window.win.lbl_sira_p3
        self.win.lbl_sira_p4.setText(shuffled_oyun_sirasi[3].playername)
        shuffled_oyun_sirasi[3].gui_label = window.win.lbl_sira_p4

    def gui_highlight_turn(self,current_oyuncu_el):
        window.win.lbl_sira_p1.setFont(QtGui.QFont("Verdana",10))
        window.win.lbl_sira_p2.setFont(QtGui.QFont("Verdana",10))
        window.win.lbl_sira_p3.setFont(QtGui.QFont("Verdana",10))
        window.win.lbl_sira_p4.setFont(QtGui.QFont("Verdana",10))
        temporary = current_oyuncu_el.gui_label
        temporary.setFont(QtGui.QFont("Verdana",15,weight=QtGui.QFont.Bold))
        
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

    def gui_el_goster(self,current_oyuncu_el):
        if len(current_oyuncu_el.cards) == 1:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_4.setIcon(im_card_el_1)

            self.win.bt_El_1.hide()
            self.win.bt_El_2.hide()
            self.win.bt_El_3.hide()
            self.win.bt_El_4.show()
            self.win.bt_El_5.hide()
            self.win.bt_El_6.hide()
            self.win.bt_El_7.hide()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.hide()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

        elif len(current_oyuncu_el.cards) == 2:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_3.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_4.setIcon(im_card_el_2)

            self.win.bt_El_1.hide()
            self.win.bt_El_2.hide()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.hide()
            self.win.bt_El_6.hide()
            self.win.bt_El_7.hide()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.hide()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

        elif len(current_oyuncu_el.cards) == 3:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_3.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_4.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_5.setIcon(im_card_el_3)

            self.win.bt_El_1.hide()
            self.win.bt_El_2.hide()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.hide()
            self.win.bt_El_7.hide()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.hide()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

        elif len(current_oyuncu_el.cards) == 4:
            im_card_el_1 = QIcon(current_oyuncu_el.cards[0].photo) 
            self.win.bt_El_2.setIcon(im_card_el_1)
            im_card_el_2 = QIcon(current_oyuncu_el.cards[1].photo) 
            self.win.bt_El_3.setIcon(im_card_el_2)
            im_card_el_3 = QIcon(current_oyuncu_el.cards[2].photo) 
            self.win.bt_El_4.setIcon(im_card_el_3)
            im_card_el_4 = QIcon(current_oyuncu_el.cards[3].photo) 
            self.win.bt_El_5.setIcon(im_card_el_4)

            self.win.bt_El_1.hide()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.hide()
            self.win.bt_El_7.hide()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.hide()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.hide()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.hide()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.hide()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.hide()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.hide()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.show()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.hide()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.show()
            self.win.bt_El_8.hide()
            self.win.bt_El_9.show()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.show()
            self.win.bt_El_8.show()
            self.win.bt_El_9.show()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.hide()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.show()
            self.win.bt_El_8.show()
            self.win.bt_El_9.show()
            self.win.bt_El_10.hide()
            self.win.bt_El_11.show()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.show()
            self.win.bt_El_8.show()
            self.win.bt_El_9.show()
            self.win.bt_El_10.show()
            self.win.bt_El_11.show()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.hide()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.show()
            self.win.bt_El_8.show()
            self.win.bt_El_9.show()
            self.win.bt_El_10.show()
            self.win.bt_El_11.show()
            self.win.bt_El_12.hide()
            self.win.bt_El_13.show()

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

            self.win.bt_El_1.show()
            self.win.bt_El_2.show()
            self.win.bt_El_3.show()
            self.win.bt_El_4.show()
            self.win.bt_El_5.show()
            self.win.bt_El_6.show()
            self.win.bt_El_7.show()
            self.win.bt_El_8.show()
            self.win.bt_El_9.show()
            self.win.bt_El_10.show()
            self.win.bt_El_11.show()
            self.win.bt_El_12.show()
            self.win.bt_El_13.show()        


        else:
            print("HATA !!!!!!!!\nSayıyı geçtiniz\nsayıyı geçtiniz\nsayıyı geçtiniz\nsayıyı geçtiniz\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyunabasla()
    sys.exit(app.exec_())
