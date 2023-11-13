#Veri Türleri

"""
Programlamada veri türü önemli bir kavramdır.

Değişkenler farklı türdeki verileri depolayabilir ve farklı türler farklı şeyler yapabilir.

Python, bu kategorilerde varsayılan olarak aşağıdaki veri türlerini yerleşik olarak içerir:
"""



"""
Metin Türü:	       str

Sayısal Türler:	   int, float, complex

Sıra Türleri:	   list, tuple, range

Haritalama Türü:   dict

Türleri Ayarla:	   set,frozenset

Boole Türü:	       bool

İkili Tipler:	   bytes, bytearray, memoryview

Hiçbiri Türü:	   NoneType
"""



"""Veri Türünü Alma"""
#Herhangi bir nesnenin veri türünü aşağıdaki işlevi kullanarak alabilirsiniz type():

x = 5
print(type(x))

y="hello"
print(type(y))





"""EXAMPLE"""
#x = "Hello World"	                            str	
#x = 20	                                        int	
#x = 20.5	                                    float	
#x = 1j	                                        complex	
#x = ["apple", "banana", "cherry"]	            list	
#x = ("apple", "banana", "cherry")	            tuple	
#x = range(6)	                                range	
#x = {"name" : "John", "age" : 36}	            dict	
#x = {"apple", "banana", "cherry"}	            set	
#x = frozenset({"apple", "banana", "cherry"})	frozenset	
#x = True	                                    bool	
#x = b"Hello"	                                bytes	
#x = bytearray(5)	                            bytearray	
#x = memoryview(bytes(5))	                    memoryview	
#x = None	                                    NoneType



x = 5
print(type(x))

x = "Hello World"
print(type(x))

x = 20.5
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

x = True
print(type(x))


