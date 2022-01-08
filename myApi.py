from colorama import Fore
import time


def welcome():
    print("HOŞ GELDİN"), time.sleep(2)
    print("Benim adım", Fore.RED, "HangMFman", Fore.RESET), time.sleep(3)
    print(
        "Oyunun amacı, ben senin için bir kelime seçeceğim. Sende o kelimeyi harf tahmin ederek bulmaya çalışacaksın."), time.sleep(
        3)
    print(Fore.YELLOW, "Dikkat et", Fore.RESET,
          "her tahmin edeceğin kelimenin harf sayısı kadar deneme hakkın var."), time.sleep(3)
    print("Eğer yanlış tahmin edersen ben ölürüm. Ve beni kodlayanlar beni üldüren kişileri sevmezler."), time.sleep(3)
    print("Ayrıca beni kodlayan", Fore.GREEN, "Furkan ve Muhammede", Fore.RESET,
          "selamlar. Onları çok seviyoruz <3"), time.sleep(3)
    print(Fore.YELLOW, "HAZIRSAN BAŞLAYALIM"), time.sleep(1)

def a_y_ready():
    key = True
    while key == True:
        a_y_ready = input("Hazırsan 'Y' değilsen 'N' yaz. Eğer hazır değilsen sana 15 saniye veriyorum.\n"
                      "15 saniye sonra oyun otomatik başlayacak. \n>>>")
        a_y_ready = a_y_ready.lower()

        countdown = 16
        countdowninGame = 5
        if a_y_ready == "n":
            key = False
            print("Peki prenses seni bekliyoruz.", Fore.RESET)
            for i in range(15):
                countdown -= 1
                print("Kalan:", countdown)
                time.sleep(1)
        elif a_y_ready == "y":
            key = False
            print("")
        else:
            key = True
            print("Hatalı Giriş Yaptınız.\n")
welcome()
a_y_ready()
