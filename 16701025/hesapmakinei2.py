print("""
|-------------------|
|[1] Toplama Islemi |
|[2] Cikarma Islemi |
|[3] Bolme   Islemi |
|[4] Carpma  Islemi |
|[Q] Cikis          |
|-------------------|
   """)

giris = input("Islemi Seciniz: ")

if giris == "1":
    x = float(input("Ilk sayi: "))
    y = float(input("Ikinci Sayi: "))
    print("Islem Sonucu: ", x + y)

elif giris == "2":
    x = float(input("Ilk sayi: "))
    y = float(input("Ikinci Sayi: "))
    print("Islem Sonucu: ", x - y)

elif giris == "3":
    x = float(input("Ilk sayi: "))
    y = float(input("Ikinci sayi: "))
    print("Islem Sonucu : ", x / y)
elif giris == "4":
    x = float(input("Ilk sayi: "))
    y = float(input("Ikinci sayi : "))
    print("Islem sonucu : ", x*y)

else:
    print("Cikildi")
    quit()
