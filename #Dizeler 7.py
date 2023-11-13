#Dizeler 7

"""Dize Yöntemleri"""

#Not: Tüm dize yöntemleri yeni değerler döndürür. Orijinal dizeyi değiştirmezler.

"""
Method	           Description
capitalize()	   İlk karakteri büyük harfe dönüştürür
casefold()	       Dizeyi küçük harfe dönüştürür
center()	       Ortalanmış bir dize döndürür
count()	           Belirli bir değerin bir dizede kaç kez oluştuğunu döndürür
encode()	       Dizenin kodlanmış bir sürümünü döndürür
endswith()         Dize belirtilen değerle bitiyorsa true değerini döndürür
expandtabs()	   Dizenin sekme boyutunu ayarlar
find()	           Belirtilen değer için dizeyi arar ve bulunduğu yerin konumunu döndürür
format()	       Bir dizede belirtilen değerleri biçimlendirir
format_map()	   Bir dizede belirtilen değerleri biçimlendirir
index()	           Belirtilen değer için dizeyi arar ve bulunduğu yerin konumunu döndürür
isalnum()	       Dizedeki tüm karakterler alfasayısal ise True değerini döndürür
isalpha()	       Dizedeki tüm karakterler alfabedeyse True değerini döndürür
isascii()	       Dizedeki tüm karakterler ascii karakterlerse True değerini döndürür
isdecimal()	       Dizedeki tüm karakterler ondalık sayıysa True değerini döndürür
isdigit()	       Dizedeki tüm karakterler rakam ise True değerini döndürür
isidentifier()	   Dize bir tanımlayıcı ise True değerini döndürür
islower()	       Dizedeki tüm karakterler küçük harf ise True değerini döndürür
isnumeric()	       Dizedeki tüm karakterler sayısal ise True değerini döndürür
isprintable()	   Dizedeki tüm karakterler yazdırılabilirse True değerini döndürür
isspace()	       Dizedeki tüm karakterler boşluk ise True değerini döndürür
istitle()	       Dize bir başlığın kurallarına uyuyorsa True değerini döndürür
isupper()	       Dizedeki tüm karakterler büyük harf ise True değerini döndürür
join()	           Yinelenebilir öğeleri dizenin sonuna birleştirir
ljust()	           Dizenin sola dayalı sürümünü döndürür
lower()	           Bir dizeyi küçük harfe dönüştürür
lstrip()	       Dizenin sol kesim versiyonunu döndürür
maketrans()	       Çevirilerde kullanılacak bir çeviri tablosunu döndürür
partition()	       Dizenin üç parçaya bölündüğü bir demet döndürür
replace()	       Belirtilen değerin belirtilen değerle değiştirildiği bir dize döndürür
rfind()	           Belirtilen değer için dizeyi arar ve bulunduğu yerdeki son konumu döndürür
rindex()	       Belirtilen değer için dizeyi arar ve bulunduğu yerdeki son konumu döndürür
rjust()	           Dizenin sağa yaslanmış versiyonunu döndürür
rpartition()	   Dizenin üç parçaya bölündüğü bir demet döndürür
rsplit()	       Dizeyi belirtilen ayırıcıda böler ve bir liste döndürür
rstrip()	       Dizenin sağ kesim versiyonunu döndürür
split()	           Dizeyi belirtilen ayırıcıda böler ve bir liste döndürür
splitlines()	   Dizeyi satır sonlarında böler ve bir liste döndürür
startswith()	   Dize belirtilen değerle başlıyorsa true değerini döndürür
strip()	           Dizenin kırpılmış bir versiyonunu döndürür
swapcase()	       Harfleri değiştirir, küçük harf büyük harfe dönüşür ve bunun tersi de geçerlidir
title()	           Her kelimenin ilk karakterini büyük harfe dönüştürür
translate()	       Çevrilmiş bir dize döndürür
upper()	           Bir dizeyi büyük harfe dönüştürür
zfill()	           Dizeyi başlangıçta belirtilen sayıda 0 değeriyle doldurur
"""
# Bu dosya Python'da string metotlarının nasıl kullanılacağını göst
# için hazırlanmıştır.

# Metodlar:
# --------------------------
# count(self, sub, start=None, end=None) -> int
# endswith(self, suffix, start=None, end=None) -> bool
# expandtabs(self, tabsize=8) -> str
# find(self, sub, start=None, end=None) -> int
# format_map(formatstring, mapping, *args) -> str
# index(self, sub, start=None, end=None) -> int
# isalpha() -> bool
# isdigit() -> bool
# isidentifier() -> bool
# islower() -> bool
# isspace() -> bool
# istitle() -> bool
# isupper() -> bool
# join(iterable) -> str
# ljust(width[, fillchar]) -> str
# lower() -> str
# lstrip([chars]) -> str
# maketrans(*x) -> str
# partition(sep) -> tuple
# replace(old, new[, count]) -> str
# rfind(sub, start=None, end=None) -> int
# rindex(sub, start=None, end=None) -> int
# rjust(width[, fillchar]) -> str
# rpartition(sep) -> tuple
# rsplit([sep [, max]]) -> list
# rstrip([chars]) -> str
# split([sep [, max]] [, /]) -> list
# splitlines([keepends] [/]) -> list
# startswith(prefix, start=None, end=None) -> bool
# strip([chars]) -> str
# swapcase() -> str
# title() -> str
# translate(table) -> str
# upper() -> str
# zfill(width) -> str

import string

def test():
    # create a string object
    s = "Hello World!"
    
    print("Original String : ",s)
    # using the method 'count' to get the number of times substring occurs in the given string
    print("\nCount of substring 'o':",s.count('o'))
    # using the method 'startswith' to check if the string starts with the specified prefix or not
    print("\nDoes it start with 'Hell'?",s.startswith('Hell'))
    # using the method 'endswith' to check if the string ends with the specified suffix or not
    print("\nDoes it end with 'ld!'?",s.endswith('ld!'))
    # using the method 'isalnum' to check if all characters are alphanumeric (letters and numbers only)
    print("\nisAlphabetic?",s.isalnum())
    # using the method 'isnumeric' to check if all characters are numeric (numbers only)
    print("\nisNumeric?",s.isnumeric())
    # using the method 'isspace' to check if all characters are whitespace
    print("\nisSpace?",s.isspace())

