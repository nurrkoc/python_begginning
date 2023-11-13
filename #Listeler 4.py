#Listeler 4

"""Liste Öğeleri Ekle"""

#append()Bir öğeyi eklemek için yöntemi kullanma
liste = [1,2,3]
liste.append(4)
print(liste)

#extend()Birden fazla öğe eklemek için yöntemini kullanma
liste = [1,2,3]
liste.extend([5,6])
print(liste)

"""Liste Öğeleri Silme"""

#pop()Son öğeyi silmek için yöntemi kullanma
liste = ['A','B','C']
son_eleman = liste.pop()
print("Son Eleman:", son_eleman)
print("Yeni Listede Kalanlar: ",liste)

#remove()Belirli bir öğeyi silmek için yöntemi kullanma
liste = ['A','B','C']
liste.remove('B')
print(liste)

#Del, Anahtar kelime ayrıca belirtilen dizini de kaldırır
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear() Liste hala duruyor ama içeriği yok.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


"""Liste Öğeleri Değiştirme"""

#index()Belirli bir öğenin konumunu bulmak için yöntemi kullanır
liste = ['A','B','C']
konum = liste.index('B')
print("Konum: ", konum)

#insert()Belirli bir konuma öğe eklemek için yöntemi kullanır
liste = ['A','B','C']
liste.insert(0,'X')
print(liste)

"""Liste Sorgulama"""

#count()Belirli bir öğenin kaç kez tekrar edildiğini sayar
liste = ['A','B','C','D','B','E','F','B']
sayac = liste.count('B')
print("B'nin Kaç Kere Tekrar Edildi? : ", sayac)

#sort()Listedeki elemanları sıralamaya yarayan yöntemi kullanır
liste = ['Z', 'M', 'T', 'A', 'O', 'P']
liste.sort()
print(liste)

#reverse()Listedeki elemanları tersine döndürür
liste = ['Z', 'M', 'T', 'A', 'O', 'P']
liste.reverse()
print(liste)



"""Liste Değişkenleri ve Yapılandırmaları"""
#Değişkenler
mylist = []
yourlist = list()
theirlist = list()
#Diziyi Boşaltmak
emptylist = mylist[:]
print(emptylist)
#Diziyi Kopya Almak
copyoflist = yourlist[:]
print(copyoflist)
#Dizinin Başlangıcından Birkaç Elemana Kadar Olan Diziyi Almak
firstfewitems = theirlist[:3]
print(firstfewitems)
#Dizinin Sonundan Birkaç Elemana Kadar Olan Diziyi Almak
lastfewitems = theirlist[-3:]
print(lastfewitems)
#Diziyi Sıralama
sortedlist = sorted(theirlist)
print(sortedlist)
#Diziyi Ters Çevrilmesi
reversedlist = theirlist[::-1]
print(reversedlist)
#Listeler Arasını Karıştırma
combinedlist = mylist + yourlist
print(combinedlist)
#Listeler Arasına Eklenebilir
anotherlist = combinedlist + theirlist
print(anotherlist)


