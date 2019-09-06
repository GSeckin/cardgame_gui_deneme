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
            while kontrolt3 < 1:
                cevap_tur3 = str(input("\n\tOyna!\n\t< kart çek / kart oyna >\n\t")).lower()
                cevap_tur3.strip()
                if cevap_tur3 == "kart çek":
                    kontrolt3 = 1
                    self.kart_cek_user_ng(orta.ortadaki_kart.mark7)
                    self.olasi_hamleleri_bul_ng()
                elif cevap_tur3 == "kart oyna":
                    kontrolt3 = 1
                    kontrol_r3 = self.hamle_sec_user_ng7(cards_7)
                    if kontrol_r3 == 0:
                        kontrolt3 = 0
                    else:
                        kontrol_r3.mark7 += orta.ortadaki_kart.mark7
                        self.kart_oyna_user_ng(kontrol_r3)
                else:
                    print("\n\tGeçerli bir cevap vermedin")
                    time.sleep(1)
                    print("\n\tBir daha dene")
                    time.sleep(1)

        kontrolt1 = 0
        kontrolt2 = 0
        while kontrolt1 < 1:
            cevap_tur1 = str(input("\n\tOyna!\n\t< kart çek / kart oyna >\n\t")).lower()
            cevap_tur1.strip()
            if cevap_tur1 == "kart çek":
                kontrolt1 = 1
                self.kart_cek_user_ng(1)
                self.olasi_hamleleri_bul_ng()
            elif cevap_tur1 == "kart oyna":
                kontrolt1 = 1
                kontrol_r1 = self.hamle_sec_user_ng()
                if kontrol_r1 == 0:
                    kontrolt1 = 0
                else: 
                    self.kart_oyna_user_ng(kontrol_r1)
                    kontrolt2 = 1
            else:
                print("\n\tGeçerli bir cevap vermedin")
                time.sleep(1)
                print("\n\tBir daha dene")
                time.sleep(1)
        
        while kontrolt2 < 1:
            cevap_tur2 = str(input("\n\tOyna!\n\t< kart oyna / turu bitir>\n\t")).lower()
            cevap_tur2.strip()
            if cevap_tur2 == "kart oyna":
                kontrolt2 = 1
                kontrol_r1 = self.hamle_sec_user_ng()
                if kontrol_r1 == 0:
                    kontrolt2 = 0
                else: 
                    self.kart_oyna_user_ng(kontrol_r1)
            elif cevap_tur2 == "turu bitir":
                kontrolt2 = 1
                time.sleep(1)
                print("\n\tTurun bitti.\n")
            else:
                print("\n\tGeçerli bir cevap vermedin")
                time.sleep(1)
                print("\n\tBir daha dene")
                time.sleep(1)
                    
    
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
        window.gui_kartoyna_np(card_instance)
        self.oyuncu.cards.remove(card_instance)
        window.gui_el_goster(self.oyuncu)
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
 