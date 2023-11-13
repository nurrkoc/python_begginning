#Değişkenler 1

#Bir değişkene ilk kez değer atadığınız anda yaratılır.

x = 5
y = "Jerry"
print(x)
print(y)


#Değişkenlerin belirli bir türle bildirilmesine gerek yoktur ve hatta ayarlandıktan sonra türü bile değiştirebilirler.

x = 4       # x is of type int
x = "Salı" # x is now of type str
print(x)


#Bir değişkenin veri tipini belirtmek istiyorsanız bu, cast ile yapılabilir.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#Bir değişkenin veri tipini fonksiyonla alabilirsiniz type().

x = 5
y = "Jerry"
print(type(x))
print(type(y))


"""
Tek veya Çift Tırnak?
Dize değişkenleri tek veya çift tırnak kullanılarak bildirilebilir
"""
x = "John"
# is the same as
x = 'John'


#Değişken adları büyük/küçük harfe duyarlıdır.

a = 4
A = "Sally"
#A ile a farklıdır

