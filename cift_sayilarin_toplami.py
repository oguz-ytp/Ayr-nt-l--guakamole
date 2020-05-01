sayi = int(input('Bir sayı girin : '))

toplam = 0
i = int(input('Sayı girin : '))
if i <= sayi:
    if i % 2 == 0:
        toplam = toplam + i
        i += 1
        print(i)

    else:
        print(i)
else:
    print(toplam)