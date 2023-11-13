#Dizeler 2

"""Dilimleme"""

#Dizenin bir bölümünü döndürmek için başlangıç ​​dizinini ve bitiş dizinini iki nokta üst üste işaretiyle ayırarak belirtin.


b = "Hello, World!"
print(b[2:5])

z="Monday"
print(b[3:4])

y="deri ceket"
print(y[3:8])


"""Not: İlk karakterin indeksi 0'dır."""


#Başlangıçtan Dilim Başlangıç ​​dizini dışarıda bırakıldığında aralık ilk karakterden başlayacaktır:


b = "Hello, World!"
print(b[:5])

a="March"
print(a[:2])

x="python"
print(x[:5])



# Sonuna Kadar Dilimle Bitiş indeksini dışarıda bırakarak aralık sonuna kadar gidecektir:

b = "Hello, World!"
print(b[2:])



#Negatif İndeksleme Dilimi dizenin sonundan başlatmak için negatif dizinleri kullanın:

b = "Hello, World!"
print(b[-5:-2])
