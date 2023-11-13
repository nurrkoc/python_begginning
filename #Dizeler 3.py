#Dizeler 3


"""Dizeleri değiştir"""


#büyük harf upper()Yöntem dizeyi büyük harfle döndürür.

import re


a = "Hello, World!"
print(a.upper())



#Küçük Harf Yöntem dizeyi lower()küçük harfle döndürür:

a = "Hello, World!"
print(a.lower())


#Boşlukları Kaldır Boşluk, asıl metinden önceki ve/veya sonraki boşluktur ve çoğu zaman bu boşluğu kaldırmak istersiniz. Yöntem strip(), başlangıçtaki veya sondaki tüm boşlukları kaldırır

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#Dizeyi Değiştir Yöntem replace(), bir dizeyi başka bir dizeyle değiştirir

a = "Hello, World!"
print(a.replace("H", "J"))


#Bölünmüş Dize Yöntem, split()belirtilen ayırıcı arasındaki metnin liste öğeleri haline geldiği bir liste döndürür. Yöntem split(), ayırıcının örneklerini bulursa dizeyi alt dizelere böler:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']





"""------------------------------------------------------------------------------------"""



#Büyük Harf 
def b_harf(dizi):
    return [item.upper() for item in dizi]
    print(b_harf(['merhaba', 'nasılsn']))

#Küçük harf
def k_harf(dizi):
    return [item.lower() for item in dizi]
    print(k_harf(['MERHABA', 'NASILSEN']))

#Tersleme
def ters(dizi):
    return dizi[::-1]
    print(ters([1,2,3,4]))

#Çift sayılar
def cft_sayilar(dizi):
    return [x for x in dizi if x % 2 == 0]
    print(cft_sayilar([1,2,3,4,5,6,7,8,9]))

#Gerilimli Sayılar
def gerilimli_sayilar(dizi):
    return [x for x in dizi if x > 0 and x < 10]
    print(gerilimli_sayilar([1,2,3,4,5,6,7,8,9,1
    ,2,3,4,5,6,7,8,9,10]))

#Farklı Karakterler
def farkli_karakter(dizi):
    return len(set(dizi))
    print(farkli_karakter('abc'))

#Eklenecek karakter
def eklenecek_karakter(dizi):
    return "".join("*" * (len(dizi) + 2))
    print(eklenecek_karakter('abc'))

#Yazdırma
def yazdir(dizi):
    for i in range(len(dizi)):
        print(dizi[i])
        print("\n")
    print(yazdir(['Merhaba','nasilsen']))
    #Harfli Diziler
def harflidiziler(dizi):
    return sorted(dizi)
    print(harflidiziler(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y ','z']))

#Harfli Diziler
def harflidiziler(dizi):
    return sorted(dizi)
    print(harflidiziler(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y ','z']))

#Harfli Diziler
def harflidiziler(dizi):
    return sorted(dizi)
    print(harflidiziler(['a','b','c','d','e','f','g','h','i','j','k ','l','m','n','o','p','q','r','s','t','u','v','w','x','y ','z']))


# upper()Yöntem dizeyi büyük harfle döndürür

# lower()Yöntemi, bir dizeyi küçük harfe dönüştürür.  

# capitalize() Yöntemi, ilk karakteri büyük harfe ve diğerlerini küçük    
# harfe dönüştürür.

# title() Yöntemi, her sözcükteki ilk karakteri büyük harfe dönüş 
# türdür.

# swapcase() Yöntemi, tüm harflerin yazı tipine göre durumlarını
# değiştirir.


print("Hello World".upper())
print("Hello World".lower())
print("Hello World".capitalize())
print("Hello World".title())
print("Hello World".swapcase())


"""Sayısal Dizeler"""
#int(), float(), complex() sayısal dizelerden sayıya çevirip onu
#sayısal dizeler olarak döndürür.
x = "1024"
y = int(x)
print(type(y))

x = "3.14159"
y = float(x)
print(type(y))

x = "2+7j"
y = complex(x)
print(type(y))

a = "3.14"
b = float(a)
print(type(b))

c = "6+7j"
d = complex(c)
print(type(d))
"""Dizeler içinde Arama"""
def arama_bulma():
    string = "Python is a great programming language."
    if "great" in string:
        return True
    else:
        return False

print(arama_bulma())
"""Birleşim (Concatenation)"""
string1 = "Hello"
string2 = "World!"
string3 = string1 + " " + string2
print(string3)

"""String Slicing"""
string = "Hello World!"
print(string[0]) # H
print(string[-1]) # !
print(string[:5]) # Hello
print(string[::-1]) # !dlroW olleH
print(string[1:-1]) # ello Worl

"""Finding the Index of an Item"""
string = "Hello, World!"
index = string.find('o')
if index != -1:
    print("Found at", index)
else:
    print("Not found")

"""Replacing Substrings"""
string = "Hello, World!"
new_string = string.replace('o', '*')
print(new_string)
"""Capitalizing and Lowercase Conversion"""
string = "hello world!".capitalize()
print(string)
string = "HELLO WORLD!".lower()
print(string)
"""Counting Occurrences"""
string = "Hello, World! I love Python."
count = string.count('o')
print(count)
"""Splitting Strings"""
string = "I am learning Python today."
words = string.split()
print(words)
"""Join Method"""
list = ["This", "is", "a", "test"]
joined_string = "-".join(list)
print(joined_string)
"""Strip Method"""
string = "\n   This is a test.\t\r"
cleaned_string = string.strip()
print(cleaned_string)

"""Dizeler içinde Karşılaştırma"""
string1 = "python"
string2 = "java"
if (string1 == string2):
    print("Eşit")
else:
    print("Uzunluğu Farklı veya Harfli Farklı.")


"""Kalanlama"""
#replace() metodu ile belli karakterleri başka karakterlerle değiştirebilirsiniz
s = "The quick brown fox jumps over the lazy dog."
print(s.replace('quick', 'slow'))
print(s.replace('fox', 'cat'))
print(s.replace('the ', ''))
print(s.replace('.', '-'))


"""Paragraf"""
#split() metodunu kullanarak paragraflara ayırabilirsiniz.
text = """
The first paragraph.
    Another paragraph.
    Yet another one.
    And an end.
"""
lines = text.split("\n")
for line in lines:
    print(line)


"""Çoklu Boşluktan Bir Paragraftan Oluşan Satırlardaki Boşluklari K
aldırma"""
#strip() metoduyla boşlukları kaldırarak satırdaki en son boşluğu sil
# stripped_line = line.strip()
# if not stripped_line:
#     continue
# words = stripped_line.split()
# for word in words:
#      print(word)
# print()


"""Büyük Harfli ve Küçük Harfli Karakterler Arasında Değişim"""
#translate() metodunu kullanarak büyük harfli ve küçük harfli karakterler ar
#asında değişim yapabilirsiniz.
translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyz",
"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
upper_string = s.upper().translate(translation_table)
lower_string = s.lower().translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(f'Original string: {s}')
print(f'Upper case: {upper_string}')
print(f'Lower case: {lower_string}')


"""Metin İçerisindeki Sayıları Bulma"""
#findall() metodunu kullanarak sayıları buluruz.
numbers = re.findall('\d+', s)
for number in numbers:
    print(number)


"""Sayısal Metni Hesaplamada Kullanma"""
num1 = int(numbers[0])
num2 = int(numbers[1])
result = num1 + num2
print(result)
"""Tek Tırnak İçeriğini Alma"""
import json
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'
person = json.loads(json_data)
print(person['name']) # John Doe
"""JSON Verilerini Yazma"""
with open('people.json', 'w') as file:
    json.dump([person], file)
    """Dosya Okuma ve Dosyalara Yazma"""
    #read() metodu ile dosyanın içeriğini okumalıyoruz.
    with open('file.txt', 'r') as file:
        content = file.read()
        print(content)
        
        #write() metodu ile dosyaya yazabiliriz.
        with open('new-file.txt', 'w') as new_file:
            new_file.write('Hello World!')
            #append() metodu ile bir dosyaya eklenebilir.
            with open('new-file.txt', 'a') as append_file:
                append_file.write(', How are you?')
                
