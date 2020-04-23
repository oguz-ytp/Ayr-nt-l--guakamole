girilen_dakika = input('Dakika girin : ')
girilen_dakika = int(girilen_dakika)

saat = (girilen_dakika // 60)
dakika = girilen_dakika % 60

print(girilen_dakika, 'dakika', saat, 'saat', dakika, 'dakikaya eşittir.')