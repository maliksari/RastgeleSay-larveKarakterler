"""
 Pytest modülü ile test ettim oluşturduğum her bir fonksiyonu for döngüsüne alıp 100 farklı sonuç ürettim ve
 bunları listelere aktardım ve bunların birbirine benzermi değilmi durumlarını kontrol ettim
"""
from Karakter import *
import pytest

class Test_Rastgelekarakter():
    def test_tekharf(self):
        x = Rastgele_karakter(1586)
        y = Rastgele_karakter(98785)
        t = []
        k = []
        for _ in range(100):
            t += x.tek_Harf()
            k += y.tek_Harf()
        assert k != t

    def test_karakterSeçme(self):
        a = Rastgele_karakter(56684)
        b = Rastgele_karakter(1554)
        x, y = [], []
        belirlikarakterler = "fkljdaskkfeoıufhKJFHkljdsfIWQPQ"
        for i in range(100):
            x +=a.karakter_secme(belirlikarakterler)
            y += b.karakter_secme(belirlikarakterler)
        assert x != y

    def test_rastgelekelime(self):
        a = Rastgele_karakter(56684)
        b = Rastgele_karakter(1554)
        x,y = [],[]
        for i in range(100):
            x += a.Rastgele_Kelime()
            y += b.Rastgele_Kelime()
        assert x != y

    def test_rastgeleCümle(self):
        a = Rastgele_karakter(2984)
        b = Rastgele_karakter(9794)
        x,y = [],[]
        for i in range(100):
            x += a.rastgele_cümle()
            y += b.rastgele_cümle()
        assert x != y
    def test_ikikarak_tekharf(self):
        a = Rastgele_karakter(2984)
        b = Rastgele_karakter(9794)
        x, y = [], []
        for i in range(100):
            x += a.iki_karakter_tekHarf("a","y")
            y += b.iki_karakter_tekHarf("a","y")
        assert x != y
    def test_Karaktersecme(self):
        a = Rastgele_karakter(2984)
        b = Rastgele_karakter(9794)
        x, y = [], []
        liste = ["ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p",
                    "r", "s", "ş", "t", "u", "ü"]
        for i in range(10):
            x += a.karakter_secme(liste)
            y += b.karakter_secme(liste)
        assert x != y
if __name__ == '__main__':
    pytest.main()

