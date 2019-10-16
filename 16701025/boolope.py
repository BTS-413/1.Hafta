"""

and
or
not

"""

sayi = int(input("Sayi giriniz : "))

if sayi > 5 and sayi % 2 == 0:
    print("sayi 5'den buyuk ve cift")
if sayi < 4 or sayi % 2 == 1:
    print("tek ve 4'den kucuk")
x = int(input("X gir: "))
y = int(input("Y gir: "))

if x == 5 or y == 5:
    print("istedigimiz oldu")
else:
    print("En az birisi 5 olmak zorunda")
k = input("K degerini gir")
l = input("L degerini gir")

if not bool(k):
    print("geldi")

