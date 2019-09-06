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

