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
kamil = 1
toplam_dogru = 0
toplam_ayt_dogru_ea = 0
toplam_ayt_dogru_m = 0
toplam_ayt_dogru_s = 0
while kamil ==1:
    print(Fore.LIGHTMAGENTA_EX)
    print("""
     /$$$$$$$$ /$$     /$$ /$$$$$$$$       /$$$$$$  /$$     /$$ /$$$$$$$$       /$$   /$$ /$$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$
    |__  $$__/|  $$   /$$/|__  $$__/      /$$__  $$|  $$   /$$/|__  $$__/      | $$  | $$| $$_____/ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$|_  $$_/ /$$__  $$|_  $$_/
      | $$    \  $$ /$$/    | $$        | $$  \ $$ \  $$ /$$/    | $$         | $$  | $$| $$      | $$  \__/| $$  \ $$| $$  \ $$| $$  \__/  | $$  | $$  \__/  | $$  
      | $$     \  $$$$/     | $$ /$$$$$$| $$$$$$$$  \  $$$$/     | $$         | $$$$$$$$| $$$$$   |  $$$$$$ | $$$$$$$$| $$$$$$$/| $$        | $$  |  $$$$$$   | $$  
      | $$      \  $$/      | $$|______/| $$__  $$   \  $$/      | $$         | $$__  $$| $$__/    \____  $$| $$__  $$| $$____/ | $$        | $$   \____  $$  | $$  
      | $$       | $$       | $$        | $$  | $$    | $$       | $$         | $$  | $$| $$       /$$  \ $$| $$  | $$| $$      | $$    $$  | $$   /$$  \ $$  | $$  
      | $$       | $$       | $$        | $$  | $$    | $$       | $$         | $$  | $$| $$$$$$$$|  $$$$$$/| $$  | $$| $$      |  $$$$$$/ /$$$$$$|  $$$$$$/ /$$$$$$
      |__/       |__/       |__/        |__/  |__/    |__/       |__/         |__/  |__/|________/ \______/ |__/  |__/|__/       \______/ |______/ \______/ |______/
                                                                                                                                                          
    """)
    print(Fore.MAGENTA+"""
                          -------Terbiyesiz Yazılımcı Tarafından Geliştirildi..-------

                          -------Terbiyesiz Yazılımcı İyi Eğlenceler Diler :)---------

             ---------Puanların Asıl Sonuçtan Sapma İhtimali Vardır Çünkü Güncel Kaynak Bulunamadı------

            ---------Net Hesaplama Esnasında Değer Giremeden Enter Tuşuna Basarsanız Uygulama Kapanır!!!-------

                  -------NET HESAPLAMADAN KULLANAMAZSINIZ AKSİ TAKTİRDE UYGULAMA KAPANIR!!!------
     """)
    print(Fore.GREEN+"""
    (1) Net Hesaplama
    (2) TYT Hesaplama
    (3) AYT Hesaplama
    (4) Uygulamadan Çık
    """)
    giris = input("Yapmak İstediğiniz İşlemi Seçin\n-Karar Verdiysen Başlayalım;")
    cikis = 1
    if giris == "1":
        while cikis == 1:
             print(Fore.MAGENTA + """
             -------Terbiyesiz Yazılımcı Tarafından Geliştirildi..-------

             -------Terbiyesiz Yazılımcı İyi Eğlenceler Diler :)---------
             """)
             print(Fore.GREEN + """
             (1) TYT Net Hesaplama
             (2) AYT Net Hesaplama  
             (3) Anasayfa
             """)
             giris2 = input("Yapmak İstediğiniz İşlemi Seçin\n-Karar Verdiysen Başlayalım;")
             if giris2 == "1":
                 a=1
                 while a == 1:
                     print(Fore.YELLOW + "Türkçe Soru Sayısı 40 Tanedir..")
                     turkce_dogru = int(input(Fore.GREEN + "Bana Türkçeden Kaç Doğrun Var Söyler Misin??\n--Türkçe Doğru Sayın;"))
                     turkce_yanlis = int(input("Bana Türkçeden Kaç Yanlışın Var Söyler Misin??\n--Türkçe Yanlış Sayın;"))
                     turkce_bos = int(input("Bana Türkçeden Kaç Boşun Olduğunu Söyler Misin??(Yoksa 0 Yazınız)\n--Türkçe Boş Sayın;"))
                     if turkce_dogru + turkce_yanlis + turkce_bos == 40:
                         print(Fore.YELLOW + "Hesaplanıyor...\n")
                         sleep(2)
                         turkce_net_yanlis = turkce_yanlis / 4
                         turkce_net_dogru = turkce_dogru-turkce_net_yanlis
                         print(Fore.GREEN + "Türkçe Net Sayın = " + str(turkce_net_dogru) + "\n")
                         a = 2
                     else:
                         print(Fore.RED + "\n" + "Toplam Soru Sayısı 40 Etmiyor Tekrar Deneyiniz..")
                         a = 1
                 b=1
                 while b == 1:
                     print(Fore.YELLOW + "Sosyal Soru Sayısı 20 Tanedir..")
                     sosyal_dogru = int(input(Fore.GREEN + "Bana Sosyal Bilimlerden Kaç Doğrun Var Söyler Misin??\n--Sosyal Bilimler Doğru Sayın;"))
                     sosyal_yanlıs = int(input("Bana Sosyal Bilimlerden Kaç Doğrun Var Söyler Misin??\n--Sosyal Bilimler Yanlış Sayın;"))
                     sosyal_bos = int(input("Bana Sosyal Bilimlerden Kaç Yanlış Olduğunu Söyler Misin??\n--Sosyal Bilimler Boş Sayın;"))
                     if sosyal_dogru + sosyal_yanlıs + sosyal_bos == 20:
                         print(Fore.YELLOW + "Hesaplanıyor..")
                         sleep(2)
                         sosyal_net_yanlis = sosyal_yanlıs / 4
                         sosyal_net_dogru = sosyal_dogru - sosyal_net_yanlis
                         print(Fore.GREEN + "Sosyal Net Sayın = " + str(sosyal_net_dogru) + "\n")
                         b = 2
                     else:
                         print(Fore.RED + "Toplam Soru Sayısı 20 Etmiyor Tekrar Deneyiniz..")
                         b = 1
                 c=1
                 while c == 1:
                     print(Fore.YELLOW + "Temel Matematik Soru Sayısı 40 Tanedir..")
                     tml_mat_dogru = int(input(Fore.GREEN + "Bana Temel Matematikten Kaç Doğrun Var Söyler Misin??\n--Temel Matematik Doğru Sayın;"))
                     tml_mat_yanlis = int(input("Bana Temel Matematikten Kaç Yanlışın Var Söyler Misin??\n--Temel Matematik Yanlış Sayın;"))
                     tml_mat_bos = int(input("Bana Temel Matematikten Kaç Boşun Var Söyler Misin??\n--Boş Sayın;"))
                     if tml_mat_dogru + tml_mat_yanlis + tml_mat_bos == 40:
                         print(Fore.YELLOW + "Hesaplanıyor..")
                         sleep(2)
                         tml_mat_net_yanlis = tml_mat_yanlis / 4
                         tml_mat_net_dogru = tml_mat_dogru - tml_mat_net_yanlis
                         print(Fore.GREEN + "Temel Matematik Net Sayın = " + str(tml_mat_net_dogru) + "\n")
                         c = 2
                     else:
                         print(Fore.RED + "Toplam Soru Sayısı 40 Etmiyor Tekrar Deneyiniz..")
                         c =1
                 d=1
                 while d == 1:
                     print(Fore.YELLOW + "Toplam Soru Sayısı 20 Tanedir..")
                     fen_bilimleri_dogru =  int(input(Fore.GREEN + "Bana Fen Bilimlerinden Kaç Doğrun Var Söyler Misin??\n--Fen Bilimleri Doğru Sayın;"))
                     fen_bilimleri_yanlis = int(input("Bana Fen Bilimlerinden Kaç Yanlışın Var Söyler Misin??\n--Fen Bilimleri Yanlış Sayın;"))
                     fen_bilimleri_bos = int(input("Bana Fen Bilimlerinden Kaç Boşun Var Söyler Misin??\n--Fen Bilimleri Boş Sayın;")) 
                     if fen_bilimleri_dogru + fen_bilimleri_yanlis + fen_bilimleri_bos == 20:
                         print(Fore.YELLOW + "Hesaplanıyor..")
                         sleep(2)
                         fen_bilimleri_net_yanlis = fen_bilimleri_yanlis / 4
                         fen_bilimleri_net_dogru = fen_bilimleri_dogru - fen_bilimleri_net_yanlis
                         print(Fore.GREEN + "Fen Bilimleri Net Sayın = " + str(fen_bilimleri_net_dogru) + "\n")
                         d = 2
                     else:
                         print(Fore.RED + "Toplam Soru Sayısı 20 Etmiyor Tekrar Deneyiniz..")
                         d = 1
                 e = 1
                 while e == 1:
                     print(Fore.YELLOW + "Toplam Net Sayın Hesaplanıyor..")
                     toplam_dogru = turkce_dogru + sosyal_dogru + tml_mat_dogru + fen_bilimleri_dogru
                     toplam_yanlıs = turkce_yanlis + sosyal_yanlıs + tml_mat_yanlis + fen_bilimleri_yanlis
                     toplam_bos = turkce_bos + sosyal_bos + tml_mat_bos + fen_bilimleri_bos
                     if toplam_dogru + toplam_yanlıs + toplam_bos == 120:
                         toplam_net_yanlis = toplam_yanlıs / 4
                         toplam_net_dogru = toplam_dogru - toplam_net_yanlis
                         print(Fore.GREEN + "Toplam Net Sayın = " + str(toplam_net_dogru) + "\n")
                         cikis = 2
                         sleep(4)
                         e = 2
                     else:
                         print(Fore.RED + "Sanırsam Yanlış Birşeyler Oldu..Uygulama Sonlandırılıyor..")
                         exit()
             elif giris2 == "2":
                 cikis2 = 1
                 while cikis2 == 1:
                     print(Fore.YELLOW + "\nAYT Net Puanını Hesaplayalım O Zaman..")
                     print("\n"*2)
                     print(Fore.GREEN + """
                     (1) Sayısal
                     (2) Eşit Ağırlık
                     (3) Sözel
                     (4) Anasayfa
                     """)
                     bolum_ayt = input("Bölümünün Sayı Değeri Nedir??\n--Bölümün;")
                     if bolum_ayt ==  "1":
                         g = 1
                         while g == 1:
                             print(Fore.YELLOW + "Matematik Soru Sayısı 40 Tanedir..")
                             mat_dogru = int(input(Fore.GREEN + "Bana Matematikten Kaç Doğrun Var Söyler Misin??\n--Matematik Doğru Sayın;"))
                             mat_yanlis = int(input("Bana Matematikten Kaç Yanlışın Var Söyler Misin??\n--Matematik Yanlış Sayın;"))
                             mat_bos = int(input("Matematikten Kaç Boşun Var Söyler Misin??\n--Matematik Boş Sayın;"))
                             if mat_bos + mat_dogru + mat_yanlis ==40:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 mat_net_yanlis = mat_yanlis / 4
                                 mat_net_dogru = mat_dogru - mat_net_yanlis
                                 print(Fore.GREEN + "\nMatematik Net Sayın =" + str(mat_net_dogru))
                                 g = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 40 Etmiyor Tekrar Deneyiniz..") 
                                 g = 1
                         h = 1
                         while h == 1:
                             print(Fore.YELLOW + "Fizik Soru Sayısı 14 Tanedir..")
                             fizik_dogru = int(input(Fore.GREEN + "Bana Fizikten Kaç Doğrun Var Söyler Misin??\n--Fizik Doğru Sayın;"))
                             fizik_yanlis = int(input("Fizikten Kaç Yanlışın Var Söyler Misin Bana??\n--Fizik Yanlış Sayın;"))
                             fizik_bos = int(input("Fizikten Kaç Boşun Var Söyler Misin Bana??\n--Fizik Boş Sayın;"))
                             if fizik_bos + fizik_dogru + fizik_yanlis == 14:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 fizik_net_yanlis = fizik_yanlis / 4
                                 fizik_net_dogru = fizik_dogru - fizik_net_yanlis
                                 print(Fore.GREEN + "\nFizik Net Sayın =" + str(mat_net_dogru))
                                 h = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 14 Etmiyor Tekrar Deneyiniz..")
                                 h = 1
                         i = 1
                         while i == 1:
                             print(Fore.YELLOW + "Kimya Soru Sayısı 13 Tanedir..")
                             kimya_dogru = int(input(Fore.GREEN + "Kimyadan Kaç Doğrun Var Bana Söyler Misin??\n--Kimya Doğru Sayın;"))
                             kimya_yanlis = int(input("Kimyadan Kaç Yanlışın Var Söyler Misin??\n--Kimya Yanlış Sayın;"))
                             kimya_bos = int(input("Kimya Boş Sayını Söyler Misin ??\n--Kimya Boş Sayın;"))
                             if kimya_bos + kimya_dogru + kimya_yanlis == 13:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 kimya_net_yanlis = kimya_yanlis / 4
                                 kimya_net_dogru = kimya_dogru - kimya_net_yanlis
                                 print(Fore.GREEN + "\nKimya Net Sayın =" + str(kimya_net_dogru))
                                 i = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 13 Etmiyor Tekrar Deneyiniz..")
                                 i = 1
                         j = 1
                         while j == 1:
                             print(Fore.YELLOW + "Biyoloji Soru Sayısı 13 Tanedir..")
                             biyoloji_dogru = int(input(Fore.GREEN + "Biyolojiden Kaç Doğru Var Söyler Misin??\n--Biyoloji Doğru Sayın;"))
                             biyoloji_yanlis = int(input("Biyolojiden Kaç Yanlışın Var Söyler Misin??\n--Biyoloji Yanlış Sayın;"))
                             biyoloji_bos = int(input("Biyoloji Boş Sayınızı Bana Söyler Misiniz??\n--Biyoloji Boş Sayın;"))
                             if biyoloji_bos + biyoloji_dogru + biyoloji_yanlis == 13:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 biyoloji_net_yanlis = biyoloji_yanlis / 4
                                 biyoloji_net_dogru = biyoloji_dogru - biyoloji_net_yanlis
                                 print(Fore.GREEN + "\nBiyoloji Net Sayın = " + str(biyoloji_net_dogru))
                                 j = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 13 Etmiyor Tekrar Deneyiniz..")
                                 j = 1
                         k = 1
                         while k ==1:
                             print(Fore.YELLOW + "\nToplam Net Sayın Hesaplanıyor..")
                             toplam_ayt_dogru_m = mat_dogru + fizik_dogru + kimya_dogru + biyoloji_dogru
                             toplam_ayt_yanlis_m = fizik_yanlis + mat_yanlis + kimya_yanlis + biyoloji_yanlis
                             toplam_ayt_bos_m = fizik_bos + mat_bos + kimya_bos + biyoloji_bos
                             if toplam_ayt_bos_m + toplam_ayt_dogru_m + toplam_ayt_yanlis_m == 80:
                                 toplam_net_ayt_yanlis_m = toplam_ayt_dogru_m / 4
                                 toplam_net_ayt_dogru_m = toplam_ayt_dogru_m - toplam_net_ayt_yanlis_m
                                 print(Fore.GREEN + "Toplam Net Sayın = " + str(toplam_net_ayt_dogru_m) + "\n")
                                 cikis2 = 2
                                 sleep(3)
                                 k = 2
                             else:
                                 print(Fore.RED + "Toplam Soru Sayısı 80 Etmiyor Tekrar Deneyiniz..")
                                 k = 1
                     elif bolum_ayt == "2":
                        l = 1
                        while l == 1:
                            print(Fore.YELLOW + "Edebiyat Soru Sayısı 24 Tanedir..")
                            edebiyat_dogru = int(input(Fore.GREEN + "Edebiyattan Kaç Doğrun Var Söyler Misin??\n--Edebiyat Doğru Sayın;"))
                            edebiyat_yanlis = int(input("Edebiyattan Kaç Yanlışın Var Söyler Misin??\n--Edebiyat Yanlış Sayın;"))
                            edebiyat_bos =  int(input("Edebiyattan Kaç Boşun Var Söyler Misin??\n--Edebiyat Boş Sayın;"))
                            if edebiyat_dogru + edebiyat_yanlis + edebiyat_bos == 24:
                                 edebiyat_net_yanlis = edebiyat_yanlis / 4
                                 edebiyat_net_dogru = edebiyat_dogru - edebiyat_net_yanlis
                                 print(print(Fore.GREEN + "Edebiyat Net Sayın =" + str(edebiyat_net_dogru)))
                                 l = 2
                            else:
                                 print(Fore.RED + "Toplam Soru Sayısı 24 Etmiyor Tekrar Deneyiniz..")
                                 l = 1
                        m = 1
                        while m == 1:
                            print(Fore.YELLOW + "Coğrafya Soru Sayısı 6 Tanedir..")
                            cografya_1_dogru = int(input(Fore.GREEN + "Coğrafyadan Kaç Doğrun Var Söyler Misin??\n--Coğrafya Doğru Sayın;"))
                            cografya_1_yanlis = int(input("Coğrafyadan Kaç Yanlışın Var Söyler Misin??\n--Coğrafya Yanlış Sayın;"))
                            cografya_1_bos =  int(input("Coğrafyadan Kaç Boşun Var Söyler Misin??\n--Coğrafya Boş Sayın;"))
                            if cografya_1_dogru + cografya_1_yanlis + cografya_1_bos == 6:
                                 cografya_1_net_yanlis = cografya_1_yanlis / 4
                                 cografya_1_net_dogru = cografya_1_dogru - cografya_1_net_yanlis
                                 print(print(Fore.GREEN + "Coğrafya Net Sayın =" + str(cografya_1_net_dogru)))
                                 m = 2
                            else:
                                 print(Fore.RED + "Toplam Soru Sayısı 6 Etmiyor Tekrar Deneyiniz..")
                                 m = 1
                        n = 1
                        while n == 1:
                            print(Fore.YELLOW + "Tarih Soru Sayısı 10 Tanedir..")
                            tarih_1_dogru = int(input(Fore.GREEN + "Tarihten Kaç Doğrun Var Söyler Misin??\n--Tarih Doğru Sayın;"))
                            tarih_1_yanlis = int(input("Tarihten Kaç Yanlışın Var Söyler Misin??\n--Tarih Yanlış Sayın;"))
                            tarih_1_bos =  int(input("Tarihten Kaç Boşun Var Söyler Misin??\n--Tarih Boş Sayın;"))
                            if tarih_1_dogru + tarih_1_yanlis + tarih_1_bos == 10:
                                 tarih_1_net_yanlis = tarih_1_yanlis / 4
                                 tarih_1_net_dogru = tarih_1_dogru - tarih_1_net_yanlis
                                 print(print(Fore.GREEN + "Tarih Net Sayın =" + str(tarih_1_net_dogru)))
                                 n = 2
                            else:
                                 print(Fore.RED + "Toplam Soru Sayısı 10 Etmiyor Tekrar Deneyiniz..")
                                 n = 1
                        o = 1
                        while o == 1:
                            print(Fore.YELLOW + "Matematik Soru Sayısı 40 Tanedir..")
                            mate_dogru = int(input(Fore.GREEN + "Matematikten Kaç Doğrun Var Söyler Misin??\n--Matematik Doğru Sayın;"))
                            mate_yanlis = int(input("Matematikten Kaç Yanlışın Var Söyler Misin??\n--Matematik Yanlış Sayın;"))
                            mate_bos =  int(input("Matematikten Kaç Boşun Var Söyler Misin??\n--Matematik Boş Sayın;"))
                            if mate_dogru + mate_yanlis + mate_bos == 40:
                                 mate_net_yanlis = mate_yanlis / 4
                                 mate_net_dogru = mate_dogru - mate_net_yanlis
                                 print(print(Fore.GREEN + "Matematik Net Sayın =" + str(mate_net_dogru)))
                                 o = 2
                            else:
                                 print(Fore.RED + "Toplam Soru Sayısı 40 Etmiyor Tekrar Deneyiniz..")
                                 o = 1
                        p = 1
                        while p == 1:
                             print(Fore.YELLOW + "Toplam Net Sayın Hesaplanıyor..")
                             toplam_ayt_dogru_ea = edebiyat_dogru + cografya_1_dogru + tarih_1_dogru + mate_dogru
                             toplam_ayt_yanlis_ea = edebiyat_yanlis + cografya_1_yanlis + tarih_1_yanlis + mate_yanlis
                             toplam_ayt_bos_ea = edebiyat_bos + cografya_1_bos + tarih_1_bos + mate_bos
                             if toplam_ayt_bos_ea + toplam_ayt_dogru_ea + toplam_ayt_yanlis_ea == 80:
                                 toplam_net_ayt_yanlis_ea = toplam_ayt_dogru_ea / 4
                                 toplam_net_ayt_dogru_ea = toplam_ayt_dogru_ea - toplam_net_ayt_yanlis_ea
                                 print(Fore.GREEN + "Toplam Net Sayın = " + str(toplam_net_ayt_dogru_ea) + "\n")
                                 cikis2 = 2
                                 sleep(3)
                                 p = 2
                             else:
                                 print(Fore.RED + "Toplam Soru Sayısı 80 Etmiyor Tekrar Deneyiniz..")
                                 p = 1
                     elif bolum_ayt == "3":
                         r = 1
                         while r == 1:
                             print(Fore.YELLOW + "Edebiyat Soru Sayısı 24 Tanedir..")
                             edeb_dogru = int(input(Fore.GREEN + "Bana Edebiyattan Kaç Doğrun Var Söyler Misin??\n--Edebiyat Doğru Sayın;"))
                             edeb_yanlis = int(input("Bana Edebiyattan Kaç Yanlışın Var Söyler Misin??\n--Edebiyat Yanlış Sayın;"))
                             edeb_bos = int(input("Edebiyattan Kaç Boşun Var Söyler Misin??\n--Edebiyat Boş Sayın;"))
                             if edeb_bos + edeb_dogru + edeb_yanlis == 24:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 edeb_net_yanlis = edeb_yanlis / 4
                                 edeb_net_dogru = edeb_dogru - edeb_net_yanlis
                                 print(Fore.GREEN + "\nEdebiyat Net Sayın =" + str(edeb_net_dogru))
                                 r = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 24 Etmiyor Tekrar Deneyiniz..") 
                                 r = 1
                         s = 1
                         while s == 1:
                             print(Fore.YELLOW + "Coğrafya Soru Sayısı 6 Tanedir..")
                             cog_1_dogru = int(input(Fore.GREEN + "Bana Coğrafyadan Kaç Doğrun Var Söyler Misin??\n--Coğrafya Doğru Sayın;"))
                             cog_1_yanlis = int(input("Coğrafyadan Kaç Yanlışın Var Söyler Misin Bana??\n--Coğrafya Yanlış Sayın;"))
                             cog_1_bos = int(input("Coğrafyadan Kaç Boşun Var Söyler Misin Bana??\n--Coğrafya Boş Sayın;"))
                             if cog_1_bos + cog_1_dogru + cog_1_yanlis == 14:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 cog_1_net_yanlis = cog_1_yanlis / 4
                                 cog_1_net_dogru = cog_1_dogru - cog_1_net_yanlis
                                 print(Fore.GREEN + "\nCoğrafya Net Sayın =" + str(cog_1_net_dogru))
                                 s = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 6 Etmiyor Tekrar Deneyiniz..")
                                 s = 1
                         t = 1
                         while t == 1:
                             print(Fore.YELLOW + "Tarih Soru Sayısı 10 Tanedir..")
                             trh_1_dogru = int(input(Fore.GREEN + "Tarihten Kaç Doğrun Var Bana Söyler Misin??\n--Tarih Doğru Sayın;"))
                             trh_1_yanlis = int(input("Tarihten Kaç Yanlışın Var Söyler Misin??\n--Tarih Yanlış Sayın;"))
                             trh_1_bos = int(input("Tarihten Boş Sayını Söyler Misin ??\n--Tarih Boş Sayın;"))
                             if trh_1_bos + trh_1_dogru + trh_1_yanlis == 10:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 trh_1_net_yanlis = trh_1_yanlis / 4
                                 trh_1_net_dogru = trh_1_dogru - trh_1_net_yanlis
                                 print(Fore.GREEN + "\nTarih Net Sayın =" + str(kimya_net_dogru))
                                 t = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 10 Etmiyor Tekrar Deneyiniz..")
                                 t = 1
                         u = 1
                         while u == 1:
                             print(Fore.YELLOW + "Tarih-2 Soru Sayısı 11 Tanedir..")
                             trh_2_dogru = int(input(Fore.GREEN + "Tarih-2 Kaç Doğru Var Söyler Misin??\n--Tarih-2 Doğru Sayın;"))
                             trh_2_yanlis = int(input("Tarih-2 Kaç Yanlışın Var Söyler Misin??\n--Tarih-2 Yanlış Sayın;"))
                             trh_2_bos = int(input("Tarih-2 Boş Sayınızı Bana Söyler Misiniz??\n--Tarih-2 Boş Sayın;"))
                             if trh_2_bos + trh_2_dogru + trh_2_yanlis == 11:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 trh_2_net_yanlis = trh_2_yanlis / 4
                                 trh_2_net_dogru = trh_2_dogru - trh_2_net_yanlis
                                 print(Fore.GREEN + "\nTarih-2 Net Sayın = " + str(trh_2_net_dogru))
                                 u = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 11 Etmiyor Tekrar Deneyiniz..")
                                 u = 1
                         y = 1
                         while y == 1:
                             print(Fore.YELLOW + "Coğrafya-2 Soru Sayısı 11 Tanedir..")
                             cog_2_dogru = int(input(Fore.GREEN + "Coğrafya-2 Kaç Doğru Var Söyler Misin??\n--Coğrafya-2 Doğru Sayın;"))
                             cog_2_yanlis = int(input("Coğrafya-2 Kaç Yanlışın Var Söyler Misin??\n--Coğrafya-2 Yanlış Sayın;"))
                             cog_2_bos = int(input("Coğrafya-2 Boş Sayınızı Bana Söyler Misiniz??\n--Coğrafya-2 Boş Sayın;"))
                             if cog_2_bos + cog_2_dogru + cog_2_yanlis == 11:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 cog_2_net_yanlis = cog_2_yanlis / 4
                                 cog_2_net_dogru = cog_2_dogru - cog_2_net_yanlis
                                 print(Fore.GREEN + "\nCoğrafya-2 Net Sayın = " + str(cog_2_net_dogru))
                                 y = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 11 Etmiyor Tekrar Deneyiniz..")
                                 y = 1
                         z = 1
                         while z == 1:
                             print(Fore.YELLOW + "Felsefe Soru Sayısı 12 Tanedir..")
                             fels_dogru = int(input(Fore.GREEN + "Felsefede Kaç Doğru Var Söyler Misin??\n--Felsefe Doğru Sayın;"))
                             fels_yanlis = int(input("Felsefede Kaç Yanlışın Var Söyler Misin??\n--Felsefe Yanlış Sayın;"))
                             fels_bos = int(input("Felsefede Boş Sayınızı Bana Söyler Misiniz??\n--Felsefe Boş Sayın;"))
                             if fels_bos + fels_dogru + fels_yanlis == 12:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 fels_net_yanlis = fels_yanlis / 4
                                 fels_net_dogru = fels_dogru - fels_net_yanlis
                                 print(Fore.GREEN + "\nFelsefe Net Sayın = " + str(fels_net_dogru))
                                 z = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 12 Etmiyor Tekrar Deneyiniz..")
                                 z = 1
                         ab = 1
                         while ab == 1:
                             print(Fore.YELLOW + "Din Kültürü ve Ahlak Bilgisi Soru Sayısı 6 Tanedir..")
                             din_dogru = int(input(Fore.GREEN + "Din Kültürü ve Ahlak Bilgisinde Kaç Doğru Var Söyler Misin??\n--Din Kültürü ve Ahlak Bilgisi Doğru Sayın;"))
                             din_yanlis = int(input("Din Kültürü ve Ahlak Bilgisinde Kaç Yanlışın Var Söyler Misin??\n--Din Kültürü ve Ahlak Bilgisi Yanlış Sayın;"))
                             din_bos = int(input("Din Kültürü ve Ahlak Bilgisinde Boş Sayınızı Bana Söyler Misiniz??\n--Din Kültürü ve Ahlak Bilgisi Boş Sayın;"))
                             if din_bos + din_dogru + din_yanlis == 6:
                                 print(Fore.YELLOW + "\nHesaplanıyor..")
                                 sleep(2)
                                 din_net_yanlis = din_yanlis / 4
                                 din_net_dogru = din_dogru - din_net_yanlis
                                 print(Fore.GREEN + "\nDin Kültürü ve Ahlak Bilgisi Net Sayın = " + str(din_net_dogru))
                                 ab = 2
                             else:
                                 print(Fore.RED + "\nToplam Soru Sayısı 6 Etmiyor Tekrar Deneyiniz..")
                                 ab = 1
                         v = 1
                         while v ==1:
                             print(Fore.YELLOW + "\nToplam Net Sayın Hesaplanıyor..")
                             toplam_ayt_dogru_s = edeb_dogru + cog_1_dogru + trh_1_dogru + trh_2_dogru +cog_2_dogru + din_dogru + fels_dogru
                             toplam_ayt_yanlis_s = edeb_yanlis + cog_1_yanlis + trh_1_yanlis + trh_2_yanlis +cog_2_yanlis +din_yanlis + fels_yanlis
                             toplam_ayt_bos_s = edeb_bos + cog_1_bos + trh_1_bos + trh_2_bos + cog_2_bos + din_bos + fels_bos
                             if toplam_ayt_bos_s + toplam_ayt_dogru_s + toplam_ayt_yanlis_s == 80:
                                 toplam_net_ayt_yanlis_s = toplam_ayt_dogru_s / 4
                                 toplam_net_ayt_dogru_s = toplam_ayt_dogru_s - toplam_net_ayt_yanlis_s
                                 print(Fore.GREEN + "Toplam Net Sayın = " + str(toplam_net_ayt_dogru_s) + "\n")
                                 cikis2 = 2
                                 sleep(3)
                                 v = 2
                             else:
                                 print(Fore.RED + "Toplam Soru Sayısı 80 Etmiyor Tekrar Deneyiniz..")
                                 v = 1
                     elif bolum_ayt == "4":
                         print(Fore.RED + "Anasayfaya Dönülüyor..")
                         cikis2 = 2
                     else:
                         print(Fore.RED + "--Yanlış Seçeneği Tuşladınız Veya Tanınmayan Harf Girişi Yapıldı!!!\n--5 Saniye Bekle Ceza Aldınız!!!")
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
                         print("--Tekrardan Başlatılıyor...")
                         sleep(2)
                         cikis = 1
             elif giris2 == "3":
                 print(Fore.RED + "Anasayfaya Dönülüyor..")
                 cikis = 2
             else:
                 print(Fore.RED + "--Yanlış Seçeneği Tuşladınız Veya Tanınmayan Harf Girişi Yapıldı!!!\n--5 Saniye Bekle Ceza Aldınız!!!")
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
                 print("--Tekrardan Başlatılıyor...")
                 sleep(2)
                 cikis = 1               
    elif giris == "2":
        kamil1=1
        while kamil1 ==1:
            if toplam_dogru > 0:
                print("\n"*25)
                print(Fore.GREEN + """
                 --Hadi TYT Puanını Hesaplayalım O Zaman Dostum..
                 """)
                print("\n"*3)
                tyt_turkce = turkce_net_dogru * 3.14
                tyt_matematik = tml_mat_net_dogru * 3.72
                tyt_sosyal_bilimler = sosyal_net_dogru * 3.03
                tyt_fen_bilimleri = fen_bilimleri_net_dogru * 3.49
                tyt_ilk_toplam = tyt_turkce + tyt_matematik + tyt_sosyal_bilimler + tyt_fen_bilimleri + 100
                if tyt_ilk_toplam>150:
                     diploma_notu = int(input(Fore.GREEN + "Diploma Puanını Girmen Gerekiyor..\n--Diploma Notun;"))
                     tyt_toplam= (diploma_notu * 0.6) + tyt_ilk_toplam
                     print(Fore.YELLOW + "Hesaplanıyor..")
                     sleep(2)
                     print(Fore.GREEN + "TYT Puanın = " + str(tyt_toplam))
                     sleep(5)
                     kamil1=2
                     sleep(1)
                     kamil = 1
                elif tyt_ilk_toplam<150:
                     print(Fore.YELLOW + "Hesaplanıyor..")
                     sleep(2)
                     print(Fore.GREEN + "TYT Puanın = " + str(tyt_ilk_toplam))
                     sleep(5)
                     kamil1=2
                     sleep(1)
                     kamil = 1
            elif toplam_dogru ==0:
                print(Fore.RED + "Kayıtlı Net Değerleri Bulunamadı..")
                sleep(1)
                print("\n" + Fore.YELLOW + "Giriş Bölümünü Okumadın Mı Dostum??")
                sleep(2)
                print(Fore.GREEN + "Anasayfaya Yönlendirilyorsunuz..")
                print(Fore.YELLOW + "\n" +"Bu İşlem Biraz Zaman Alabilir..")
                print(Fore.GREEN)
                print("-3..")
                sleep(1)
                print("-2..")
                sleep(1)
                print("-1..")
                sleep(1)
                print(Fore.MAGENTA + "Net Hesaplaycıya Giriniz Dostumm..")
                sleep(2)
                kamil1 = 2
    elif giris == "3":
        kamil3 = 1
        while kamil3 == 1:
             if toplam_ayt_dogru_s or toplam_ayt_dogru_ea or toplam_ayt_dogru_m > 0:
                 print("""
                 (1) Sayısal
                 (2) Eşit Ağırlık
                 (3) Sözel
                 (4) Anasayfa
                  """)
                 ayt_bolum = input("Bölümünün Sayı Değeri Nedir??\n--Bölümün;")
                 if (ayt_bolum == "1") and (toplam_ayt_dogru_m >0):
                         kontrol = 1
                         while kontrol == 1:
                             print("\n25")
                             print(Fore.GREEN + """
                             ----Haydii Dostum AYT Sayısal Puanını Ölçelimm...
                              """)
                             ayt_fizik_m = fizik_net_dogru * 2.85
                             ayt_kimya_m = kimya_net_dogru * 3.07
                             ayt_biyoloji_m = biyoloji_net_dogru * 3.07
                             ayt_mat_m = mat_net_dogru * 3
                             ayt_ilk_toplam_m = ayt_biyoloji_m + ayt_fizik_m + ayt_kimya_m + ayt_mat_m + 100
                             diploma_notu = int(input(Fore.GREEN + "Diploma Puanını Girmen Gerekiyor..\n--Diploma Notun;"))
                             ayt_toplam_m =((diploma_notu * 5)*0.6)+ayt_ilk_toplam_m
                             print(Fore.YELLOW + "Hesaplanıyor..")
                             sleep(2)
                             print(Fore.GREEN + "TYT Puanın = " + str(ayt_toplam_m))
                             sleep(3)
                             kontrol = 2
                             sleep(2)
                             kamil3 = 1
                 elif (ayt_bolum == "2") and (toplam_ayt_dogru_ea >0):
                         kontrol2 = 1
                         while kontrol2 == 1:
                             print("\n25")
                             print(Fore.GREEN + """
                             ----Haydii Dostum AYT Eşit Ağırlık Puanını Ölçelimm...
                             """)
                             ayt_edeb_ea  = edebiyat_net_dogru * 3
                             ayt_mat_ea = mate_net_dogru * 3
                             ayt_trh_ea = tarih_1_net_dogru * 2.8
                             ayt_cog_ea = cografya_1_net_dogru * 3.33
                             ayt_ilk_toplam_ea = ayt_cog_ea + ayt_edeb_ea + ayt_mat_ea + ayt_trh_ea + 100
                             diploma_notu = int(input(Fore.GREEN + "Diploma Puanını Girmen Gerekiyor..\n--Diploma Notun;"))
                             ayt_toplam_ea =((diploma_notu * 5)*0.6)+ayt_ilk_toplam_ea
                             print(Fore.YELLOW + "Hesaplanıyor..")
                             sleep(2)
                             print(Fore.GREEN + "TYT Puanın = " + str(ayt_toplam_ea))
                             sleep(3)
                             kontrol2 = 2
                             sleep(2)
                             kamil3 = 1
                 elif (ayt_bolum == "3") and (toplam_ayt_dogru_s >0):
                        kontrol3 = 1
                        while kontrol3 == 1:
                             print("\n25")
                             print(Fore.GREEN + """
                             ----Haydii Dostum AYT Eşit Ağırlık Puanını Ölçelimm...
                             """)
                             ayt_edeb_s = edeb_net_dogru * 3 
                             ayt_trh_1_s = trh_1_net_dogru * 2.8
                             ayt_cog_1_s = cog_1_net_dogru * 3.33
                             ayt_trh_2_s = trh_2_net_dogru  * 2.91
                             ayt_cog_2_s = cog_2_net_dogru * 2.91
                             ayt_fels_s = fels_net_dogru * 3
                             ayt_dikab_s = din_net_dogru * 3.33
                             ayt_ilk_toplam_s = ayt_edeb_s + ayt_trh_1_s + ayt_cog_1_s + ayt_trh_2_s +ayt_cog_2_s + ayt_fels_s + ayt_dikab_s + 100 
                             diploma_notu = int(input(Fore.GREEN + "Diploma Puanını Girmen Gerekiyor..\n--Diploma Notun;"))
                             ayt_toplam_s =((diploma_notu * 5)*0.6)+ayt_ilk_toplam_s
                             print(Fore.YELLOW + "Hesaplanıyor..")
                             sleep(2)
                             print(Fore.GREEN + "TYT Puanın = " + str(ayt_toplam_ea))
                             sleep(3)
                             kontrol3 = 2
                             sleep(2)
                             kamil3 = 1
                 elif ayt_bolum == "4":
                         print(Fore.RED + "Anasayfaya Dönülüyor..")
                         sleep(2)
                         kamil3 = 2
                 else:
                     print(Fore.RED + "--Yanlış Seçeneği Tuşladınız Veya Tanınmayan Harf Girişi Yapıldı!!!\n--5 Saniye Bekle Ceza Aldınız!!!")
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
                     print("--Tekrardan Başlatılıyor...")
                     sleep(2)
             elif toplam_ayt_dogru_m or toplam_ayt_dogru_ea or toplam_ayt_dogru_s ==0:
                 print(Fore.RED + "Kayıtlı Net Değerleri Bulunamadı..")
                 sleep(1)
                 print("\n" + Fore.YELLOW + "Giriş Bölümünü Okumadın Mı Dostum??")
                 sleep(2)
                 print(Fore.GREEN + "Anasayfaya Yönlendirilyorsunuz..")
                 print(Fore.YELLOW + "\n" +"Bu İşlem Biraz Zaman Alabilir..")
                 print(Fore.GREEN)
                 print("-3..")
                 sleep(1)
                 print("-2..")
                 sleep(1)
                 print("-1..")
                 sleep(1)
                 print(Fore.MAGENTA + "Net Hesaplaycıya Giriniz Dostumm..")
                 sleep(2)
                 kamil3 = 2
    elif  giris == "4":
        print(Fore.RED + "Uygulamadan Çıkılıyor..")
        sleep(3)
        exit()
    else:
        print(Fore.RED + "--Yanlış Seçeneği Tuşladınız Veya Tanınmayan Harf Girişi Yapıldı!!!\n--5 Saniye Bekle Ceza Aldınız!!!")
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
        print("--Tekrardan Başlatılıyor...")
        sleep(2)
        kamil = 1
#1.Gün Gece TYT Net Hesaplama Bitirildi..Toplam Net Sayısı Hesaplandı..
#2.Gün Sabah TYT Puanı Hesaplama Bölümü Bitirldi..TYT Puanı Hesaplandı..AYT Net Hesaplama Bölümüne Giriş Yapıldı..
#2.Gün Akşam Anasayfaya Dönme Seçenekleri Eklendi..Belli Başlı Hatalar Giderildi..
#2.Gün Gece AYT Net Hesplamasına Birkaç Tane Ders Eklendi..
#3.Gün Sabah AYT Net Hesaplama Bitirildi...Toplam Net Hesaplandı..
#3.Gün Öğlen Uygulama Bitirildi...Teslim Edildi....