import colorama 
import random 
from colorama import Fore,Back,Style
colorama.init()
from time import sleep
import os
if os.name == 'nt':
    _ = os.system('cls')
elif os.name == 'mac':
    _ = os.system('clear')
elif os.name =='posix':
    _ = os.system('clear')
else:
    _ = os.name('clear')
türkiyenin_illeri =["Adana","Adıyaman","Afyon","Ağrı","Amasya","Ankara","Antalya","Artvin","Aydın","Balıkesir","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Isparta","Mersin","İstanbul","İzmir","Kars","Kastamonu","Kayseri","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya","Malatya","Manisa","Kahramanmaraş","Mardin","Muğla","Muş","Nevşehir","Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Şanlıurfa","Uşak","Van","Zonguldak","Aksaray","Bayburt","Karaman","Kırıkkale","Batman","Şırnak","Bartın","Ardahan","Iğdır","Yalova","Karabük","Kilis","Osmaniye","Düzce"]
print(Fore.RED+"---------Bil Bakalım Türkiyenin İlleri--------")
print(Fore.MAGENTA)
print("""
|****************************|
|     Ad:Terbiyesiz          |
|  Soyad:Robot               |
|   Amaç:Oyun Oynamak        |
|     NOT:81 İl Var          |
|     NOT:İlk Harf Büyük Yaz |
|                            |
|                            |
|                            |
|                            |
|****************************|
""")
rastgele = random.choice(türkiyenin_illeri)
a = 1
deneme = 0
while a ==1:
    tahmin=input(Fore.CYAN + "Bil Bakalım Hangi Şehirdeyim ??\n-Bulunduğum Şehir;")
    deneme += 1
    if (tahmin == rastgele):
        print(Fore.CYAN + str(deneme) + " Kez Denemişsin Karşim Ama Sonunda Kazandın :))")
        print(Fore.GREEN + "Uygulamadan Çıkılıyor....")
        print("-5..")
        sleep(1)
        print("-4..")
        sleep(1)
        print("-3..")
        sleep(1)
        print("-2..")
        sleep(1)
        print("-1..")
        sleep(1)
        print("-0..")
        print("-Terbiyesiz Yazılımcı İyi Günler Diler...")
        sleep(2)
        if os.name == 'nt':
              _ = os.system('cls')
        elif os.name == 'mac':
              _ = os.system('clear')
        elif os.name =='posix':
              _ = os.system('clear')
        else:
              _ = os.name('clear')
        exit()
    else:
        if deneme ==1:
             print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
             print("İpucu;" +rastgele[:1])
        if deneme == 2:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +rastgele[:2])
        elif deneme == 5:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +rastgele[:3])
        elif  deneme ==10:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +rastgele[:4])
        elif  deneme ==17:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +rastgele[:5])