# -*- coding: cp1254 -*- #t�rk�e karakter kullanmak i�in
yazi = "alfabe"
sayi = 0

for harf in yazi: #yazi icersinde ki her bir ogeyi teker teker x degiskenine ata, ve her biri icin tek tek calis
    print (harf,end= "") #bu dongüharf sayisi kadar tekrarlarir, end atarsak asa degilde yan yana ondururondr

for harf in yazi:
    sayi +=1

print(sayi) # d�ng�n�n d�nd�gü kez kadarki say
print (len(yazi)) #kontrol icn
