import time
class HesapMakinesi():

    def __init__(self, value1, value2):
        self.deger1 = value1
        self.deger2 = value2

    def Toplama(self):
        return self.deger1 + self.deger2

    def Carpma(self):
        return self.deger1 * self.deger2

    def Cikarma(self):
        return self.deger1 - self.deger2

    def Bolme(self):
        return self.deger1 / self.deger2



while True:
    print("""
    [1] Toplama
    [2] Çarpma
    [3] Çıkarma
    [4] Bölme
    [Q] Çıkış
    """)

    secim = input('Yapmak istediğiniz işlem numarasını girin : ')

    if secim == 'q' or secim == 'Q':
        print('Çıkış Yapılıyor...')
        time.sleep(1)
        quit()

    sayi1 = int(input('Birinci sayıyı girin : '))
    sayi2 = int(input('İkinci sayıyı girin  :  '))
    parametre = HesapMakinesi(sayi1, sayi2)

    if secim == '1':
        print('Cevap:\n' + str(sayi1), '+', sayi2, '=', parametre.Toplama())
        time.sleep(2)

    elif secim == '2':
        print('Cevap:\n' + str(sayi1), 'x', sayi2, '=', parametre.Carpma())
        time.sleep(2)

    elif secim == '3':
        print('Cevap:\n' + str(sayi1), '-', sayi2, '=', parametre.Cikarma())
        time.sleep(2)

    elif secim == '4':
        print('Cevap:\n' + str(sayi1), '/', sayi2, '=', parametre.Bolme())
        time.sleep(2)