#Dizeler 4

"""Dize Birleştirme"""

#İki dizeyi birleştirmek veya birleştirmek için + operatörünü kullanabilirsiniz.

#a Değişkeni değişkenle b değişkende birleştir c:

a = "Hello"
b = "World"
c = a + b
print(c)
#Çıktısı: HelloWorld

x="fen"
y="bu"
z= x+ y
print (z)
#Çıktısı: fenbu


#Aralarına boşluk eklemek için şunu ekleyin " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


#Birden fazla dizenin birleştirilmesi

d1 ="Merhaba"
d2 ="Selamlar"
d3 = d1 + " ve " + d2
print(d3)
#Çıktısı: Merhaba ve Selamlar


#Dizeyi sayacak olan bir fonksiyonun nasıl olması gerektiğini bulm
def count_chars(string):
    return len(string)

text = "Python is awesome!"
count = count_chars(text)
print("The number of characters in the text is", count)
#Çıktısı: The number of characters in the text is 17


#Dizeyi harfler arasına koymak
def insert_space(sentence, index):
    words = sentence.split()
    new_words = [word[0] for word in words]
    new_words.insert(index, ' ')
    new_words.extend([word[1:] for word in words])
    return ''.join(new_words)

sentence = "Thisisatextwithnospaces"
result = insert_space(sentence, 5)
print(result)
#Çıktısı: This is a text with nospaces
