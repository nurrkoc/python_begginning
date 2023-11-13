#Setler

myset = {"apple", "banana", "cherry"}
# Not: Ayarlanan öğeler değiştirilemez, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Not: Setler sırasızdır, dolayısıyla öğelerin hangi sırayla görüneceğinden emin olamazsınız.

"""
Öğeleri Ayarla
Ayarlanan öğeler sırasızdır, değiştirilemez ve yinelenen değerlere izin vermez.

sırasız
Sırasız, bir setteki öğelerin tanımlanmış bir sıraya sahip olmadığı anlamına gelir.

Ayarlanan öğeler, onları her kullandığınızda farklı bir sırada görünebilir ve indeks veya anahtarla başvurulamaz.

Değiştirilemez
Set öğeleri değiştirilemez; yani set oluşturulduktan sonra öğeleri değiştiremeyiz.

Bir set oluşturulduktan sonra öğelerini değiştiremezsiniz ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.

Kopyalara İzin Verilmez
Kümelerde aynı değere sahip iki öğe bulunamaz.
"""
#Not:True ve değerleri 1, kümelerde aynı değer olarak kabul edilir ve kopya olarak kabul edilir:
#Not:False ve değerleri 0, kümelerde aynı değer olarak kabul edilir ve kopya olarak kabul edilir:

sayilar = {1, 2, 3, 4, 5}
print(6 in sayilar)

#Küme veri tipinde eleman eklemek için add() fonksiyonu kullanılır.
sayilar = {1, 2, 3, 4, 5}
sayilar.add(6)
print(sayilar)

#Tek bir eleman yerine birden fazla eleman eklemek için update() fonksiyonu kullanılır.
sayilar = {1, 2, 3, 4, 5}
sayilar.update([6,7,8])
print(sayilar)

 #Set içindeki bir elemanı silmek için remove() ya da discard() fonksiyonları kullanılır. Her iki fonksiyonunun kullanımı aynıdır.
sayilar = {1, 2, 3, 4, 5}
sayilar.discard(3)
print(sayilar)