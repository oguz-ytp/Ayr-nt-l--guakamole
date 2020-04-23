girilen_dakika = input('Dakika girin : ')
girilen_dakika = int(girilen_dakika)

saat = (girilen_dakika // 60)
dakika = girilen_dakika % 60

print(str(girilen_dakika) + '   ==>   ' + str(saat) + ':' + str(dakika) + ' dakikaya eşittir.')