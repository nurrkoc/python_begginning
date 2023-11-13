#Listeler 1

mylist = ["apple", "banana", "cherry"]
"""
Liste
Listeler birden fazla öğeyi tek bir değişkende depolamak için kullanılır.

Listeler, Python'da veri koleksiyonlarını depolamak için kullanılan 4 yerleşik veri türünden biridir; diğer 3'ü Tuple , Set ve Dictionary olup hepsi farklı nitelik ve kullanıma sahiptir.

Listeler köşeli parantez kullanılarak oluşturulur:
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Not=Liste öğeleri dizine eklenmiştir, ilk öğenin dizini vardır [0], ikinci öğenin dizini vardır [1]

#Kopyalara İzin Ver Listeler indekslendiğinden listeler aynı değere sahip öğeler içerebilir


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


"""
type()
Python'un bakış açısına göre listeler, 'list' veri türüne sahip nesneler olarak tanımlanır
"""

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# list() Yapıcısı
# Yeni bir liste oluştururken list() yapıcısını kullanmak da mümkündür .

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
