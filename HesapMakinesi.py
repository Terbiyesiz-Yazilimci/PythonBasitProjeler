import colorama 
from colorama import Fore,Back,Style
colorama.init()
from time import sleep
a=3
while  a ==3:
    print("\n"*60)
    print(Fore.RED)
    print("----------Hesap Makinesine Hoş Geldiniz----------")

    print(Fore.BLUE)
    print("Hangi İşlemi Yapmak İstersiniz??")
    print(Fore.YELLOW)
    print("""
    1.Toplama İşlemi
    2.Çıkarma İşlemi
    3.Çarpma İşlemi
    4.Bölme İşlemi
    """)
    işlem = input(Fore.MAGENTA + "Hangi İşlemi Yapmak İstiyorsanız Sayı Kodunu Giriniz.\n-Yapmak İstediğiniz İşlem Kodu;")
    if(işlem == '1'):
         sayı_1 =int(input(Fore.CYAN+"1.Sayı Değerini Giriniz\n-Sayı Değeri ="))
         sayı_2 = int(input(Fore.CYAN+"2.Sayı Değerini Giriniz \n-Sayı Değeri ="))
         sayı_1 = int(sayı_1)
         sayı_2 = int(sayı_2)
         print(Fore.GREEN)
         print(sayı_1+sayı_2)
         print(Fore.LIGHTYELLOW_EX + "İşlem Bitmiştir Aga :))")   
    elif(işlem == '2'):
         sayı_1 =int(input(Fore.CYAN+"1.Sayı Değerini Giriniz\n-Sayı Değeri ="))
         sayı_2 = int(input(Fore.CYAN+"2.Sayı Değerini Giriniz \n-Sayı Değeri ="))
         sayı_1 = int(sayı_1)
         sayı_2 = int(sayı_2)
         print(Fore.GREEN)
         print(sayı_1-sayı_2)
         print(Fore.LIGHTYELLOW_EX + "İşlem Bitmiştir Aga :))")   
    elif(işlem == '3'):
         sayı_1 =int(input(Fore.CYAN+"1.Sayı Değerini Giriniz\n-Sayı Değeri ="))
         sayı_2 = int(input(Fore.CYAN+"2.Sayı Değerini Giriniz \n-Sayı Değeri ="))
         sayı_1 = int(sayı_1)
         sayı_2 = int(sayı_2)
         print(Fore.GREEN)
         print(sayı_1*sayı_2)
         print(Fore.LIGHTYELLOW_EX + "İşlem Bitmiştir Aga :))")   
    elif (işlem == '4'):
         sayı_1 =int(input(Fore.CYAN+"1.Sayı Değerini Giriniz\n-Sayı Değeri ="))
         sayı_2 = int(input(Fore.CYAN+"2.Sayı Değerini Giriniz \n-Sayı Değeri ="))
         sayı_1 = int(sayı_1)
         sayı_2 = int(sayı_2)
         print(Fore.GREEN)
         print(sayı_1/sayı_2)
         print(Fore.LIGHTYELLOW_EX + "İşlem Bitmiştir Aga :))")   
    else:
         print(Fore.RED+"Kanka Bozdun Uygulamayı Kim Tamir Edicek Beni???")
         print("Kamil İmdat Bozdular Beni!!!")
         sleep(0.5)
         print("Kamil İmdat Bozdular Beni!!!")
         sleep(0.5)
         print("Kamil İmdat Bozdular Beni!!!")
         sleep(0.5)
         print("Kamil İmdat Bozdular Beni!!!")
         sleep(0.5)
         print("Kamil İmdat Bozdular Beni!!!")
         sleep(0.5)
         print("EN BAŞA DÖNÜLÜYORRRRRR !!!")
    sleep(3)
    
       
