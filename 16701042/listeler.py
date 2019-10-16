#listeleme ile girilen değerlerin tipini ekrana yazdırma
listeleme=["abc",12,10.6]

for i in listeleme:
    print(type(i))

#kitap listeleme örneği

kitapListe=["Python","C#","C++","Java"]

for i in kitapListe:
    print ("Kitabın Adı : {}".format(i))

eklenecek=input("Kitabın Adı :")
kitapListe += [eklenecek] # köşeli parantez kullanılmazsa girilen ifadeyi tek karakter olarak ekler.
print(kitapListe)
