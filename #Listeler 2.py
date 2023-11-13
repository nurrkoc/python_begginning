#Listeler 2

""""Öğelere Erişim Liste öğeleri indekslenmiştir ve bunlara indeks numarasına başvurarak erişebilirsiniz"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#Not: İlk öğenin indeksi 0'dır.

"""
Negatif İndeksleme
Negatif indeksleme sondan başlamak anlamına gelir

-1son öğeye atıfta bulunur, -2sondan ikinci öğeye vb. atıfta bulunur.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Not: Arama, dizin 2'de (dahil) başlayacak ve dizin 5'te (dahil değildir) bitecektir.


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# Öğenin Var olup olmadığını kontrol edin
# Belirli bir öğenin bir listede bulunup bulunmadığını belirlemek için inanahtar kelimeyi kullanın
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

else:
  print("No, 'apple' is not in the fruits list")

#Belirtilen öğenin bir listede yoksa ne olacağını göster
