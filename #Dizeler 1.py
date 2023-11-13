#Dizeler


print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



#1. konumdaki karakteri alın (ilk karakterin 0 konumunda olduğunu unutmayın)

a = "Hello, World!"
print(a[1])

a = "Hello, World!"
print(a[5])



"""IP uzunluğu"""
#Bir dizenin uzunluğunu elde etmek için işlevi kullanın len().

a = "Hello, World!"
print(len(a))



"""Dizeyi Kontrol Et"""
#Bir dizede belirli bir ifadenin veya karakterin bulunup bulunmadığını kontrol etmek için anahtar sözcüğünü kullanabiliriz in.

txt = "The best things in life are free!"
print("free" in txt)



"""DEĞİL olup olmadığını kontrol edin"""
#Belirli bir ifadenin veya karakterin bir dizede mevcut OLMADIĞINI kontrol etmek için anahtar sözcüğünü kullanabiliriz not in.

txt = "The best things in life are free!"
print("expensive" not in txt)

