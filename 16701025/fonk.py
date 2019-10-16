# tekrar etmek yerine fonksyonlar olustururz
x = 5 # degisken tanimlama
"""
  def topla():         #def ile fonksiyon tanimliyoruz
      yapilacaklar     #fonksiyonu cagirdigimizda yapilacaklari yaziyorz
  topla()              # olarak cagirirsak ekrana yapicaklar islemi yapar
                       # fonksiyonlar tekrar tekrar cagiralabilir
"""

def topla():
    sonuc = 3+5
    print(sonuc)
topla() #fonksiyonlari istedigimi kadr cagirabilirz.
print("ara")
topla()

"""
fonksiyonu parametrize etmeye bakalim
def topla(sayi1,sayi2):              #burda fonksiyon 2 adet parametre almistir
    print("toplam:",sayi1+sayi2)
"""
sayi1 = input("Birinci sayi: ") #birinci sayi aliyoruz
sayi2 = input("Ikinci sayi: ")  #ikinci sayi aliyoruz
def toplam(sayi1, sayi2):       # 2 sayi alan bir fonksiyon olusturuyoruz
    print("Toplamlari : ",int(sayi1)+int(sayi2)) #toplamlarini hesaplatip bastiriyoruz
toplam(sayi1,sayi2)             # fonksiyonu cagiriyoruz, fonksiyonu parametrize olarak kullanabiliyoruz.

"""
sonucu print ile ekrana basmayiz genelde

"""

def toplama(birincisayi,ikincisayi):
    sonuc = birincisayi + ikincisayi
    return sonuc  #return ile yazdirdigimizda ise daha iyi bir sonuc alirisz bu sefer asagida print kullanbilirz.
    #print(sonuc) #burda print kullandigimiz icin sadece fonk cagirdigimizda cikti alabiliyorduk

print(toplama(5,3)) #burda print etmeye calistigimizda ise bize NONE geliyor yani deger dondurmedi anlamina geliyor.

toplama(12,23)#verilen parametlerelerin toplami sayisi vardir artik bunun icinde cagirdigimiz fonkyon sonuc'a donusuyor.diger
              # durumda icerisini bos goruyor ve NONE degerini aliyor


