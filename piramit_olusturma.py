satir = int(input('Bir sayı girin : '))

for i in range(satir):
    print(" " * (satir - i - 1) + "*" * (2 * i + 1))