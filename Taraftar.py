import colorama 
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
a=1
while  a == 1:
     print(Fore.CYAN)
     print('-------------Rastgele Deneme----------')
     print("""
     1.Galatasaray
     2.Beşiktaş
     3.Trabzonspor
     4.Fenerbahçe
     """)     
     takım = input("Taraftarı Olduğun Takımın Sıra Numarasını Yaz...\n-Takımın;")
     if(takım == "1"):
         b=1
         while b == 1:
             print(Back.RED+Fore.BLACK+"GALATASARAY")
             sleep(0.5)
             print(Back.YELLOW+Fore.BLACK+"GALATASARAY")
     elif (takım =="2"):
         c=1
         while  c ==1:
              print(Back.WHITE+Fore.RED+"BEŞİKTAŞ")
              sleep(0.5)
              print(Back.BLACK+Fore.RED+"BEŞİKTAŞ")
     elif(takım =="3"):
         d=1
         while d ==1:
              print(Back.RED+Fore.BLACK+"TRABZONSPOR")
              sleep(0.5)
              print(Back.BLUE+Fore.BLACK+"TRABZONSPOR")
     elif (takım =="4"):
         e=1
         while  e==1:
             print(Back.BLUE+Fore.BLACK+"FENERBAHÇE")
             sleep(0.5)
             print(Back.YELLOW+Fore.BLACK+"FENERBAHÇE")
     else:
         f=1
         while f==1:
             print(Fore.RED+Back.RESET)
             print("Yanlış Veya Hatalı Değer Girdiniz Önemle Düzgün Bişi Yaz Yada Çık ;)")


             