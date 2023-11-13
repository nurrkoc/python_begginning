#Boolean

#Boolean'lar iki değerden birini temsil eder: Trueveya False.

print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

"""Bir if ifadesinde bir koşulu çalıştırdığınızda Python Trueveya değerini döndürür False"""

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#İşlev, bool()herhangi bir değeri değerlendirmenize ve size Trueveya False karşılığında vermenize olanak tanır.
print(bool("Hello"))
print(bool(15))


"""Bazı Değerler Yanlış"""
#Aslında , , , , number ve value Falsegibi boş değerler dışında değerini değerlendiren çok fazla değer yoktur . Ve elbette değer olarak değerlendirilir .()[]{}""0NoneFalseFalse
x = None
y = "None"
z = []
w = {}
v = ()
u = set()
print(bool(x), bool(y), bool(z), bool(w), bool(v), bool(u))


"""Boole Hesaplaması"""
is_student = True
age = 27
if age >= 18 and is_student:
    print("You are eligible for voting.")
elif age < 18 or not is_student:
    print("Sorry, you cannot vote yet.")
