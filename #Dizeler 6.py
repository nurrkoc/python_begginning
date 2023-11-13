#Dizeler 6

"""Karakterlerden Kaçış"""

# Bir dizeye yasa dışı karakterler eklemek için bir kaçış karakteri kullanın.
# \Kaçış karakteri, eklemek istediğiniz karakterin ardından gelen ters eğik çizgidir .
# Yasadışı karaktere örnek olarak, bir dizenin içinde çift tırnak işaretiyle çevrelenmiş çift tırnak işareti gösterilebilir


"""
Çift tırnak içine alınmış bir dize içinde çift tırnak kullanırsanız bir hata alırsınız:

txt = "We are the so-called "Vikings" from the north."
"""

#Bu sorunu çözmek için kaçış karakterini kullanın \"

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


"""
Kaçış Karakterleri
Python'da kullanılan diğer kaçış karakterleri:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""
# Örnek
txt = "\nThis is a new line.\nThis is another one."
print(txt)
"""
Unicode Karakterler
Python3'te Unicode karakterleri de destekliyoruz.
Burada unicode karakterleri olarak belirtmemiz gerekiyor : u'' veya r''
Örneğimizde ;

txt = u"Merhaba Dünya!"
print(txt)
"""
# Unicode Karakterleri Kullanma
# Python2 ve Python3'te farklı bir şekilde unicode karakterleri kullanmamız g
#erek , python2 için u'' , python3 için r'' kullanılmalıdır.
# Python2
txt1 = u"Merhaba Dünya!"
print(txt1)

# Python3
txt2 = r"Merhaba Dünya!"
print(txt2)
