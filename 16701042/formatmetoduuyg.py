"""
konumları belirleme
sözcük atama
:> sağa yaslama ve alan ayırma
:< sola yaslama ve alan ayırma
:^ merkezde alan ayırma
:s yalnızca string ifade
:d yalnızca sayısal ifade
:b ikili sistemdeki karşılık
"""

#konum belirleme
degisken1="Muhammed"
degisken2="Özdemir"
ifade1="{1} {0}".format(degisken1,degisken2) #{} 1 veya 0 vererek 
                                             #cümledeki konumunu belirleme 
print(ifade1) #Muhammed Özdemir ekrana basar.Bu sıralama ile ekrana yazdırır.

#sağa yaslama
ifade2="|{:>15}|".format(degisken1) #15 karakterlik alan oluşturur.
print(ifade2)

#sola yaslama
ifade3="|{:<10}|".format(degisken2) #10 karakterlik alan oluşturur.
print(ifade3)

#merkezde alan ayırma
ifade4="|{:^20}|".format(degisken1) #20 karakterlik alanda belirtilen yazıyı ortalar.
print(ifade4)

#sadece string ifade 
ifade5="{:s}".format(degisken1) #sadece string ifade girileceğini belirtir.
print(ifade5)

#sadece sayısal ifade
ifade6="{:d}".format(23) #sadece sayısal ifade girileceğini belirtir.
print(ifade6)

#ikili sistem
ifade7="{:b}".format(23) #girilen sayının ikilik sistemdeki karşılığını gösterir.
print(ifade7)
