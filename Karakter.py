"""
Malik Sarı
pythonla hazır rastgele kütüphanlerini kullanmadan rastgele sayı üretimi ve rastgele karakter üretmek
mersenne twister algoritması
"""

class Rastgele_karakter():
    harfler = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p",
                    "r", "s", "ş", "t", "u", "ü", "v", "y", "z", "x", "A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ",
                    "H", "I", "İ", "J", "K", "L",
                    "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z", "X"]

    def __init__(self, seed=5489):
            self.state = [0] * 624
            self.f = 1812433253
            self.m = 397
            self.u = 11
            self.s = 7
            self.b = 0x9D2C5680
            self.t = 15
            self.c = 0xEFC60000
            self.l = 18
            self.index = 624
            self.lower_mask = (1 << 31) - 1
            self.upper_mask = 1 << 31

            self.state[0] = seed
            for i in range(1, 624):
                self.state[i] = self.int_32(self.f * (self.state[i - 1] ^ (self.state[i - 1] >> 30)) + i)

    def twist(self):
            for i in range(624):
                temp = self.int_32((self.state[i] & self.upper_mask) + (self.state[(i + 1) % 624] & self.lower_mask))
                temp_shift = temp >> 1
            if temp % 2 != 0:
                temp_shift = temp_shift ^ 0x9908b0df
            self.state[i] = self.state[(i + self.m) % 624] ^ temp_shift
            self.index = 0

    def get_random_number(self):
            if self.index >= 624:
                self.twist()
            y = self.state[self.index]
            y = y ^ (y >> self.u)
            y = y ^ ((y << self.s) & self.b)
            y = y ^ ((y << self.t) & self.c)
            y = y ^ (y >> self.l)
            self.index += 1
            return self.int_32(y)

    def int_32(self, number):
        return int(0xFFFFFFFF & number)

    def tek_Harf(self):
        """ rastgele tek bir  karakter üreten fonksiyon """
        return self.harfler[self.get_random_number() % len(self.harfler)]

    def kelime(self,x = "Kelimenin Karakter uzunluğu"):
        """ Uzunluğu belirtilen rastgele kelime"""
        kelime =""
        for i in range(x):
            kelime += self.tek_Harf()
        return kelime

    def Rastgele_Kelime(self):
        """rastgele kelime üreten fonksiyon"""
        kelime = ""

        for i in range(self.get_random_number() % 13):
            kelime += self.tek_Harf()
        return kelime

    def iki_karakter_tekHarf(self,q,i):
        """ alfabetik sıraya göre  belirlediğimiz iki karakter arasından rastgele karakter seçme """
        Belirli_Aralık = self.harfler[self.harfler.index(q):self.harfler.index(i)]

        kelime = ""

        for k in Belirli_Aralık:
            kelime += k
        if (self.harfler.index(q) == self.harfler.index(i) or self.harfler.index(i) <self.harfler.index(q)):
            # girilen karakterlerin alfabetik sıraya uygun olmaması durumunda çıkacak hatanın kontrolü
            exit("""
                <<<<<< !!!!! UYARI !!!!  >>>>>>
            Lütfen seçtiğiniz karakterlerin alfabetik sırasına dikkat ediniz

            """)
        return Belirli_Aralık[self.get_random_number() % len(Belirli_Aralık)]


    def rastgele_cümle(self):
        """rastgele cümle üreten fonksiyon"""
        cümle = " "
        for i in range(self.get_random_number() % 17):
            cümle += self.Rastgele_Kelime() + " "
        return cümle
    def karakter_secme(self,x):
        """Kendi tanımladığımız bir liste veya string karakterlerinden
        rastgele karakter seçen fonksiyon
        """
        YeniX = list(x)
        return YeniX[self.get_random_number() % len(YeniX)]


if __name__ == '__main__':
    nesne = Rastgele_karakter(139)

    liste ="malkikdşsfalşsALSŞDJASFŞOOEFf"

    for i in range(3):

        #print(nesne.Rastgele_Kelime())
        #print(nesne.tek_Harf())
        #print(nesne.iki_karakter_tekHarf("a","z"))
       #print(nesne.rastgele_cümle())
        print(nesne.karakter_secme(liste))

