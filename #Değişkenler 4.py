#Değişkenler 4

"""ÇIKIŞ DEĞİŞKENLERİ"""

#Python print()işlevi genellikle değişkenlerin çıktısını almak için kullanılır.

x = "Python is awesome"
print(x)


#Fonksiyonda print()birden fazla değişkenin çıktısını virgülle ayırarak alırsınız

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


#   " + " (artı) Operatörü birden fazla değişkenin çıktısını almak için de kullanabilirsiniz

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#Sayılar için +karakter matematiksel bir operatör olarak çalışır

x = 5
y = 20
print(x + y)


#İşlevde print(), bir dizeyi ve bir sayıyı operatörle birleştirmeye çalıştığınızda + Python size bir hata verecektir:

x = 5
y = "John"
print(x + y)


#İşlevde birden çok değişkenin çıktısını almanın en iyi yolu, print()bunları farklı veri türlerini bile destekleyen virgüllerle ayırmaktır:

x = 5
y = "John"
print(x, y)
