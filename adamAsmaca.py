import random
import time
import myApi
from colorama import Fore, Back, Style

myApi.welcome()

myApi.a_y_ready()

print(Fore.RESET,"\nHaydi Başlayalım\n")

####

kelimeler = ["Araba", "MF", "Society"]

t_messages = ["\nAdam: Tebrikler doğru tahmin.\n", "\nAdam: Tahminin güzel\n", "\nAdam: Sen neymişsin be!\n", "\nAdam: Beni furkan ve muhammed kodladı\n", "\nAdam: Böyle devam et\n",
                                                                                                                   "Adam: Yapıyorsun bu sporu\n"]
f_messages = ["\nAdam: Ah bee yakındı\n", "\nAdam: Tekrar dene\n", "\nAdam: Hey dikkatli ol öldüreteceksin beni\n", "\nAdam: beni kodlayanlara kurban olun siz.\n", "\nTamamm tamam kızma, sakince tahmin et!\n"  ]

hedef_kelime = random.choice(kelimeler) #Kelimeler listesinden bir kelime seçer.
hedef_kelime = hedef_kelime.upper() #Bilgisayarın seçtiği kelimeyi küçük harfe çevirir.

harfler = list() # Bulunacak olan kelime için boş liste oluşturur.

deneme_hakki = len(hedef_kelime) # Oyuncuya seçilen kelime kadar deneme sayısı sunar.

kac_kelime= len(hedef_kelime)

for i in range(kac_kelime): #i döngüsünü seçinlen kelimenin karakter sayısı kadar döndür
    harfler.append("-") #Her dönüşte harfler listesine "-" ekle.

while harfler.count("-") > 0:  # harfler listesindeki - sayısı 0 dan büyük olduğu sürece döndür.
    print(harfler)
    harf = input("Harf Tahmin Edin: ") #kullanıcıdan harf tahmin etmesi istenir.
    harf = harf.upper() #kullanıcının girdiği harf küçük harfe çevrilir.

    if hedef_kelime.find(harf) == -1: # eğer hedef kelimede, kullanıcının girdiği kelime yoksa deneme hakkını bir azalt.
        deneme_hakki -= 1
        print(Fore.RED,random.choice(f_messages),Fore.RESET)
        if deneme_hakki <= 0: # eğer deneme hakki 0 dan küçük ya da eşitse oyunu bitir.
            print(Fore.RED,"Kaybettiniz",Fore.RESET)
            exit()

    else: # onun dışında
        print(Fore.MAGENTA,random.choice(t_messages),Fore.RESET)
        for i in range(len(hedef_kelime)): # hedef kelime sayısı kadar i döngüsünü döndür
            if harf == hedef_kelime[i]: # eğer harf hedef_kelimenin içinde varsa
                harfler[i] = harf # harfler listeninde bulunan yerleri girilen harfle değiştir.
print(harfler) # Son durumu yazdır.
print("Tebrikler")
