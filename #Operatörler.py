#Operatörler

"""
Toplama +      3+6
Çıkarma -      6-3
Çarpma *       3*6
Bölme /        6/3
Üs Alma **     6**3
Mod alma %     6%3
"""


"""""
Eşittir ==            ad==’özge’
Eşit Değildir !=      ad!=’özge’
Büyüktür >            a>45
Küçüktür <            a<45
Büyük Eşittir >=      5>=a
Küçük Eşittir <=      a<=5
"""""

#Karşılaştırma operatörleri, karşılaştırma sonunda true (doğru) veya false (yanlış) değeri döndürür


a=4<1
print(a)

b=4>1
print(b)

c=4==1
print(c)

d=4!=1
print(d)


''''
Ve (and) and         a<4 and a>8
veya (or) or         a<4 or a<3
değil (not) not      not(a==b)
'''

"""
a b   a and b   a b   a or b   a  a’
1 1     1       1 1   1        1  0
0 1     0       0 1   1        0  1
1 0     0       1 0   1
0 0     0       0 0   0
"""

e=20+16/4-10*1+5
print(e)

f=(2**2+3*6)
print(f)

