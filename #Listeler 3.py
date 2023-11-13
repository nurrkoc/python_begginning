#Listeler 3

# Öğe Değerini Değiştir
# Belirli bir öğenin değerini değiştirmek için dizin numarasına bakın
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Not: Eklenen öğe sayısı değiştirilen öğe sayısıyla eşleşmediğinde listenin uzunluğu değişecektir.

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Öğe Ekle
# Mevcut değerlerden herhangi birini değiştirmeden yeni bir liste öğesi eklemek için yöntemi kullanabiliriz insert().

# Yöntem insert()belirtilen dizine bir öğe ekler:


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#Not: Yukarıdaki örnek sonucunda liste artık 4 öğe içerecektir.