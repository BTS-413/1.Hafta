x = input("Birinci sayi : ")
k = bool(x)

if k == False:
    print("Sayi girisi hatali ")
    x = input("Tekrar giriniz : ")

y = input("Ikinci sayi :")
print(int(x)+int(y))
