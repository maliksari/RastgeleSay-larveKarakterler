# Rastgele Saylar ve Karakterler
Python İle rastgele karakter ve rastgele sayı 
Rastgele Sayı üreteci olarak MERSENNE TWİSTER Algoritması kullanılmıştır....

Mersenne Twister (sözde rastlantısal sayı üreteci)
"Aritmetik yöntemlerle rastsal sayılar üretmeye çalışan biri büyük günah işliyordur."
John Von Neumann 

Günümüzde random sayı üreteçleri donanımsal özellikleri kullanarak (sistem saati vb.) çalışıyor olsada çoğu programlama dili aritmetik yöntemlerle rastgele sayı üretmektedir. Aritmetik olarak rastgele sayı üretmenin avantajı şüphesiz hız olacaktır. Bilimsel simülasyonlar üzerindeki üretilmesi gereken milyonlarca rastsal eğer donanımsal olarak üretilirse epey zaman kaybı olacaktır. Bunu çözmenin bir yolu önceden rastsal sayı dizisinin oluşturulup saklanması olsa bile bir çok gerçek zamanlı simulasyonda işlevsiz kalacaktır. Python dili ve bir çok programlama dili varsayılan random sayı jeneratörü olarak mersenne twister algoritmasını tercih etmektedir. 

Algoritma, Makoto Matsumoto ve Takuji Nishimura  tarafından 1998 yılında tanıtılmıştır. Temel olarak algoritma çekirdeği 19,937 bit uzunluğunda, bu bitler 624 değişik dizi de tutuluyor ve bunlardan 623 tanesi kullanılırken son dizi elemanı ve kalan 31 kullanılmıyor. XOR ile kaydırma kaydedicileri her seferinde dizi elemanlarını birer kere kaydırıyor. Kaydırma periyodu 2^19937-1 (yani Mersenne asal sayıları, algoritmanın ismi de buradan geliyor) olduğu için her periyod ta dizi içindeki bitler rastgele kaydırılmış oluyor.





Algoritmanın pseudo kodu aşağıdaki gibidir;


for i = 0 to 623

  temp = first bit of a(i) followed by last 31 bits of a(i+1) ;
  
  a(i) = temp shifted right one bit xor
  
         X'9908B0DF' if temp is odd xor
         
         a(i+397) ;
         
 next i
 
 
for i = 0 to 226

  temp = first bit of a(i) followed by last 31 bits of a(i+1) ;
  
  a(i) = temp shifted right one bit xor
  
         X'9908B0DF' if temp is odd xor
         
         a(i+397) ;
         
 next i
 
 for i = 227 to 622
 
  temp = first bit of a(i) followed by last 31 bits of a(i+1) ;
  
  a(i) = temp shifted right one bit xor
  
         X'9908B0DF' if temp is odd xor
         
         a(i-227) ;
         
 next i
 
 temp = first bit of a(623) followed by last 31 bits of a(0) ;
 
 a(i) = temp shifted right one bit xor
 
        X'9908B0DF' if temp is odd xor
        
        a(396) ;
        
 
L = 19937

W = 32

M = 397

A = X'9908B0DF'

 
N = floor( L/W ) + 1

R = L mod W

 
for i = 0 to N-M-1

  temp = first R bits of x(i) followed by last W-R bits of x(i+1) ;
  
  x(i) = temp shifted right one bit xor
  
         A if temp is odd xor
         
         x(i+M) ;
         
 next i
 
 for i = N-M to N-2
 
  temp = first R bits of x(i) followed by last W-R bits of x(i+1) ;
  
  x(i) = temp shifted right one bit xor
  
         A if temp is odd xor
         
         x(i+M-N) ;
         
 next i
 
 temp = first R bits of x(N-1) followed by last W-R bits of x(0) ;
 
 x(N-1) = temp shifted right one bit xor
 
          A if temp is odd xor
          
          x(M-1) ; 
          
Bu yazı şu adresten alınmıştır = http://www.yasinhoca.com/2018/06/mersenne-twister-sozde-rastlantsal-say.html 
