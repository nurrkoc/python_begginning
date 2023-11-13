#Tuple(Demet)Veri Tipi

#Tuple elemanlarına ulaşma: Listelerdeki gibi indeks kullanılır

birimler = ("bit", "inç", "byte", "hertz", "piksel")
print(birimler[3])
""" Listelerde olduğu gibi negatif indekslerde kullanılabilir. -1 en sondaki eleman anlamına
gelirken -2 sondan iki önceki elemanı temsil eder."""

#Indeks aralıklarına göre yazdırma: Listelerde olduğu gibi başlangıç ve bitiş indeksleri verilerek istenilen aralık yazdırılabilir.
birimler = (1,2,3,4,5,6,7,8,9)
print(birimler[1:3])
#Tuple değiştirmek mümkün değil! Tupler sadece okunur (read-only). Değiştirilebilir bir listelere benzer farklıdırlar.


"""Tuple elemanlarını değiştirme: Tuple veri tipi tanımlanırken elemanların değiştirilemeyeceğinden bahsedildi. Eğer tuple veri tipi listeye çevrilirse elemanlar değiştirilebilir."""
birimler = (1,2,3,4,5,6,7)
birimler_liste=list(birimler) #burada tuple listeye çevrildi.
birimler_liste[2]=0 #listenin indeksi 2 olan elemanı değiştirildi.
print(birimler_liste)

"""Elemanın olup olmadığını sorgulama: Tuple veri tipinde de listelerde olduğu gibi in operatörü ile bir
elemanın listede olup olmadığı kontrol edilebilir. Eleman tuple’daysa True; yoksa False değerleri üretilir."""

birimler = (0,9,8,7,65,4,3,)
print( 8 in birimler)

"""Tuple uzunluğunu bulma: len fonksiyonu ile tuple’ın eleman sayısı bulunur"""
birimler = (1,2,3,4,55,7,8,5)
print(len(birimler))


"""Tuple içinde bir elemanın sayısını bulma: Bu işlem için listelerde olduğu gibi count fonksiyonu kullanılır"""
birimler = (1,23,34,55,6,87656,35,213,54,1,1,1)
say=birimler.count(1)
print(say)

"""Tuple içindeki elemanın indeksini bulma: Listelerde olduğu gibi index fonksiyonu kullanılır"""
birimler = (1,2,3,4,5,6)
print(birimler.index(4))