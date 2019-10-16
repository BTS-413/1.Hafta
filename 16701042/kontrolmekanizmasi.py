
#programın akışını kullanıcı girişlerini değiştirmek için kullanılan mekanizmalar

print("""

[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[E] Çıkış
""")
"""
sayi1=input("Birinci Sayi Giriniz: ")
sayi1=int(sayi1) # Girilen sayının veri tipini integer'a eşitlemek
sayi2=input("İkinci Sayi Giriniz: ")
sayi2=int(sayi2) #Girilen sayının veri tipini integer'a eşitlemek
giris=input("Seçiminiz: ")
"""
# if ve elif kullanımı ile hesap makinesi yapımı
# if bütün verileri ekrana bastırılan değerleri gösterir 
# elif ise sadece ilk doğru olan değeri ekrana bastırır. 

giris=input("Seçiminiz: ")

if giris=="1":
    sayi1=float(input("Sayi giriniz: "))
    sayi2=float(input("Sayi giriniz: "))
    print("toplama sonucu: ",sayi1+sayi2)

elif giris=="2":
    sayi1=float(input("Sayi Giriniz: "))
    sayi2=float(input("Sayi Giriniz: ")) 
    print("Çıkarma Sonucu: ",sayi1-sayi2)

elif giris=="3":
    sayi1=float(input("Sayi Giriniz: "))
    sayi2=float(input("Sayi Giriniz: "))
    print("Çarpma Sonucu: ",sayi1*sayi2)

elif giris=="4":
    sayi1=float(input("Sayi Giriniz: "))
    sayi2=float(input("Sayi Giriniz: "))
    print("Bölme Sonucu: ",sayi1/sayi2)

elif  giris=="E" or giris=="e":

    print("Çıkış Yapıldı!!!")
    quit()

else:
    print("Hatalı Değer Girildi...")
    quit()
