import random

def sayi_uret(baslangic = 0, bitis = 100, adet = 6):
    sayilar = set()

    while len(sayilar) < adet:
        sayilar.add(random.randint(baslangic, bitis))
    return sayilar
print(sayi_uret())