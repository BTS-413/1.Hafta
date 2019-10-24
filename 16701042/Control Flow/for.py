print("Girilen Sayının Faktoriyelini Bulma")
sonuc=1;
sayi=input('1. Sayı: ')
for i in range(1,int(sayi)+1):
    sonuc*=i
    print("{0} sayısının faktoriyeli : {1}".format(sayi,sonuc))
