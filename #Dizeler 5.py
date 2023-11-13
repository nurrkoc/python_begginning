#Dizeler 5

""" Biçim - Dizeler"""

# #Dize Formatı
# Python Değişkenleri bölümünde öğrendiğimiz gibi, dizeleri ve sayıları şu şekilde birleştiremeyiz

age = 16
age=str(age)
txt = "My name is Jerry, I am " + age
print(txt)
# Bu kodda hata oluşur. Neden?

"""Yöntem format()iletilen bağımsız değişkenleri alır, biçimlendirir ve bunları yer tutucuların bulunduğu dizeye yerleştirir {}"""

#format()Dizelere sayı eklemek için yöntemi kullanın :

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#Bu kodun sonucunda: My name is John, and I am 36

"""format() yöntemi sınırsız sayıda argüman alır ve ilgili yer tutuculara yerleştirilir:"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# Sonuç: I want 3 pieces of item 567 for 49.95 dollars.

"""{0}Bağımsız değişkenlerin doğru yer tutuculara yerleştirildiğinden emin olmak için dizin numaralarını kullanabilirsiniz """
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# Sonuç: I want to pay 49.95 dollars for 3 pieces of item 567.
