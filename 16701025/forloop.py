# -*- coding: cp1254 -*- #tÃrkÃe karakter kullanmak iÃin
yazi = "alfabe"
sayi = 0

for harf in yazi: #yazi icersinde ki her bir ogeyi teker teker x degiskenine ata, ve her biri icin tek tek calis
    print (harf,end= "") #bu dongÃ¼harf sayisi kadar tekrarlarir, end atarsak asa degilde yan yana ondururondr

for harf in yazi:
    sayi +=1

print(sayi) # dÃngÃnÃn dÃndÃgÃ¼ kez kadarki say
print (len(yazi)) #kontrol icn
