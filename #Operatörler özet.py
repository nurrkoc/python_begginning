#Operatörler özet

"""
Python Operatörleri
Operatörler değişkenler ve değerler üzerinde işlem yapmak için kullanılır.

Aşağıdaki örnekte +iki değeri toplamak için operatörü kullanıyoruz:

ÖrnekKendi Python Sunucunuzu edinin
print(10 + 5)
Python operatörleri aşağıdaki gruplara ayırır:

Aritmetik operatörler
Atama operatörleri
Karşılaştırma operatörleri
Mantıksal operatörler
Kimlik operatörleri
Üyelik operatörleri
Bitsel operatörler
Python Aritmetik Operatörleri
Aritmetik operatörler, yaygın matematiksel işlemleri gerçekleştirmek için sayısal değerlerle birlikte kullanılır:

Operator	Name	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
Python Atama Operatörleri
Atama operatörleri değişkenlere değer atamak için kullanılır:

Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
ADVERTISEMENT

Python Karşılaştırma Operatörleri
Karşılaştırma operatörleri iki değeri karşılaştırmak için kullanılır:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	
Python Mantıksal Operatörleri
Mantıksal operatörler koşullu ifadeleri birleştirmek için kullanılır:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
Python Kimlik Operatörleri
Kimlik operatörleri, nesneleri eşit olup olmadıklarını değil, gerçekte aynı nesne olup olmadıklarını ve aynı bellek konumuna sahip olup olmadıklarını karşılaştırmak için kullanılır:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y	
Python Üyelik Operatörleri
Üyelik operatörleri bir nesnede bir dizinin sunulup sunulmadığını test etmek için kullanılır:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
Python Bitsel Operatörler
Bitsel operatörler (ikili) sayıları karşılaştırmak için kullanılır:

Operator	Name	Description	Example	Try it
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
Operatör Önceliği
Operatör önceliği, işlemlerin gerçekleştirilme sırasını açıklar.

Örnek
Parantezlerin en yüksek önceliği vardır; bu, parantez içindeki ifadelerin ilk önce değerlendirilmesi gerektiği anlamına gelir:

print((6 + 3) - (6 + 3))
Örnek
Çarpma işlemi *, toplama işleminden daha yüksek önceliğe sahiptir +ve bu nedenle çarpma işlemleri, toplama işlemlerinden önce değerlendirilir:

print(100 + 5 * 3)
Öncelik sırası, en üstteki en yüksek öncelikten başlayarak aşağıdaki tabloda açıklanmıştır:

Operator	Description	Try it
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR	
Eğer iki operatör aynı önceliğe sahipse ifade soldan sağa doğru değerlendirilir.

Örnek
Toplama +ve çıkarma -aynı önceliğe sahiptir ve bu nedenle ifadeyi soldan sağa doğru değerlendiriyoruz:

print(5 + 4 - 7 + 3)
"""