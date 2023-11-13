#Listeler 6

"""Listeleri kopyala"""
# Listelerin nasıl kopyalanacağını gösteren bir program yazıyoruz. list() 
list1 = [1,2,3]
list2 = list(list1)
print("Kopya: ", list2)

#Kopya oluşturmanın yolları vardır; yollardan biri yerleşik List yöntemini kullanmaktır copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

