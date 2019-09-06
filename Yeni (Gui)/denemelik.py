import time

class Denemelik:
    def __init__(self):
        self.elma = ""
        self.armut = ""
        self.nar = ""


list1 = [1,2,3]
list2 = ["a","b","c"]
# list3 = [elma,armut,nar]
list4 = ["elma","armut","nar"]

Deneme1 = Denemelik()

# print(Deneme1.elma,Deneme1.armut,Deneme1.nar,sep="\nyeni ")

# for item in list4:
#     print(item)
#     Deneme1.item = "var"

# print(Deneme1.elma,Deneme1.armut,Deneme1.nar,sep="\nboşmu? ")

print("İşaret kontrolü başlıyor\n")

isaret1 = 0

while isaret1 == 0:
    if isaret1 == 1:
        break
    else: 
        time.sleep(2)

print("Bitti\n")