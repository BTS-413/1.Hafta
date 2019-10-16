#tekrarlanabilme özelliği
"""
def topla():
    sonuc=3+5
    print(sonuc)
topla()
"""
#parametrize özelliği
"""
def topla(birincisayi,ikincisayi):
    sonuc=birincisayi+ikincisayi
    print(sonuc)

topla(3,8)
"""
#return özelliği
def topla(sayi1,sayi2):
    sonuc=sayi1+sayi2
    return sonuc

print(topla(3,5))

print("sayı vardır : ",topla(12,23))

