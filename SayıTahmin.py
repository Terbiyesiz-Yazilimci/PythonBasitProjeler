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
print(Fore.GREEN)
print("----------Tuttur Tuturabilirsen---------")
rastgele_sayı = random.randint(1,3)
a = 1
deneme=0
while a ==1:
    tahmin = input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
    deneme +=1
    print("\n"+Fore.WHITE+str(deneme)+" Kez Denedin Karşim..\n")
    tahmin = int(tahmin)
    if rastgele_sayı == tahmin:
         print(Fore.GREEN+"Şanlısın Kardeşşşş Nasıl Zihnimi Okudun Ama :))\n")
         rastgele_sayı1 = random.randint(1,5)
         print(Fore.CYAN + "Bunu Bulamazsın Çünkü Bu 2.Seviye")
         b=1
         deneme2=0
         while b ==1:
             tahmin1 =input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
             deneme2 +=1
             print("\n"+Fore.WHITE+str(deneme2)+" Kez Denedin Karşim..\n")
             tahmin1 = int(tahmin1)
             if rastgele_sayı1 == tahmin1:
                 print(Fore.CYAN +"Ama Bu Kadar Da Zeki Olamazsın :((\n")
                 print(Fore.YELLOW + "3.Seviyeye Geçelim O Zaman")
                 rastgele_sayı2 = random.randint(1,10)
                 c = 1
                 deneme3=0
                 while c ==1:
                     tahmin2 = input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
                     deneme3 +=1
                     print("\n"+Fore.WHITE+str(deneme3)+" Kez Denedin Karşim..\n")
                     tahmin2 = int(tahmin2)
                     if rastgele_sayı2 == tahmin2:
                         print(Fore.YELLOW + "Kanka Sen Beni Hackledin Mi Nasıl Biliyorsun?? :d\n")
                         print(Fore.RED + "EEEEE Seni 4.Seviyeye Geçiriyimde Gör (X_X)")
                         rastgele_sayı3 = random.randint(1,25)
                         d=1
                         deneme4=0
                         while d==1:
                             tahmin3 = input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
                             deneme4 +=1
                             print("\n"+Fore.WHITE+str(deneme4)+" Kez Denedin Karşim..\n")
                             tahmin3 = int(tahmin3)
                             if rastgele_sayı3 == tahmin3:
                                 print(Fore.RED + "İmdat Bu Adam Siber Dünyanın İçine Girmiş...Nasıl Biliyorsun Lannnnnnnnnnn(!_!)")
                                 print(Fore.YELLOW + "Tebrik Ederim İnsan Oyunu Kazandın!!!!!")
                                 toplam = deneme+deneme2+deneme3+deneme4
                                 print(Fore.CYAN + str(toplam) + " Kez Denemişsin Karşim Ama Sonunda Kazandın :))")
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
                                 print(Back.WHITE+Fore.RED)
                                 print("Ağla İnsan En Son Seviyeye Geldin Birde HAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHA")
                                 print("Hey İnsan Olan Kişi Sayı 1 İle 25 Arasında (w_w)")
                                 print(Back.RESET+Fore.RED)
                     else:
                         print(Back.WHITE+Fore.RED)
                         print("İnsan Değilmisin Hepiniz Benim Kadar Zeki Değilsiniz (O_O)")
                         print("Hey Ezik Sayı 1 İle 10 Arası (._.)")
                         print(Back.RESET+Fore.YELLOW)
             else:
                 print(Back.WHITE+Fore.RED)
                 print("Ezik Beni Yenemezsin Çünkü Ben 'Terbiyesiz Yazılımcı' HAHAHHAHAHAH ")
                 print("Tuttuğum Sayı 1 İle 5 Arası İnsan..")
                 print(Back.RESET+Fore.CYAN)
    else:
         print(Back.WHITE+Fore.RED)
         print("Kankacım Çok Yanlış Düşünüyorsun :/ ")
         print("Tuttuğum Sayı 1 İle 3 Arası :)")
         print(Back.RESET+Fore.GREEN)
