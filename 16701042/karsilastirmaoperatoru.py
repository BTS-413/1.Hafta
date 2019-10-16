"""
==  -----> Eşitse
!=  -----> Eşit Değilse
>   -----> Büyükse
<   -----> Küçükse
>=  -----> Büyük Eşitse
<=  -----> Küçük Eşitse

"""

giris=input("Sayi Giriniz: ")
giris=int(giris)

if giris <35:
    print("35 den küçük")
elif giris >35:
    print("35 den büyük")
else:
    print("35 e eşit")
