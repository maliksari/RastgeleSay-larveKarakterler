"""
Sonuçları hem ekrana hemde bir text  dosyasına yazdırma

"""
from Karakter import *
nesne = Rastgele_karakter()

karakterler = "kfdaALkşkOWOKQPmkldmaklmfQokdpl"

with open("sonuc.txt","w+") as f:
    f.write("Rastgele kelimeler   \n \n")
    for i in range(5):

        f.write(nesne.Rastgele_Kelime()+"\n")
    f.write("------------------------------------")
    f.write("Rastgele tek harfler")
    f.write("------------------------------------\n")
    for _ in range(5):
        f.write(nesne.tek_Harf()+ "\n")
    f.write("------------------------------------")
    f.write("Rastgele cümleler")
    f.write("------------------------------------\n")
    for _ in range(5):
        f.write(nesne.rastgele_cümle() + "\n")

# Consolda bu sonuçları görmek için aşağıdaki kodları etkinleştiriniz

print("Rastgele Tek Karakterler :","="*15,"Rastgele Kelimeler","="*15," Rastgele cümleler " )
for i in range(5):
  print(nesne.tek_Harf()," "*40,nesne.Rastgele_Kelime()," "*30,nesne.rastgele_cümle())
print("-"*200)
print("iki karakterden tek harf","="*10,"Belirli karakterlerden harf seçme")
for i in range(5):
    print(nesne.iki_karakter_tekHarf("d","Z")," "*40,nesne.karakter_secme(karakterler))

