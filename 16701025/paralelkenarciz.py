def sagSlas(adet):
    for i in range(int(adet)):
        print("/",end="")#alt satira inmemesi icin end'i  duzeldik.

def solSlas(adet):
    for i in range(int(adet)):
        print("\\",end="") #kacis dizi olarak gormemesi icin 2 tane  "\" koyduk

def satirAtla(adet):
    for i in(range(int(adet))):
        print() #alt satira inecek range kadar

def bosluk(adet):
    for i in range(int(adet)):
        print(" ",end="")
def ustKisim(cap):
    baslangicBosluk = cap/2-1
    for i in range(int(cap/2)):
        bosluk(baslangicBosluk-i)
        sagSlas(1)
        bosluk(i*2)
        solSlas(1)
        satirAtla(1)


def altKisim(cap):
    baslangicBosluk = cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solSlas(1)
        bosluk(baslangicBosluk - i*2)
        sagSlas(1)
        satirAtla(1)

def paralelkenar(cap):
    ustKisim(cap)
    altKisim(cap)
paralel = input("Siz girin biz cizelim A.S: ")
paralelkenar(int(paralel))
