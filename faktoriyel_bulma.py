sayi = input('Faktöriyelini bulmak istediğiniz sayıyı girin : ')
sayi = int(sayi)

sonuc = 1

for i in range(1, sayi + 1):
    sonuc = sonuc * i
print(str(sayi) + '!', 'Sayısının faktöriyeli =', sonuc)