karakter = input('Lütfen bir kelime giriniz : ')
print(karakter.title())  # title() metodu karakterin baş karflerini büyültmeye kullanılır.

karakter = karakter.split(' ')
karakter = list(karakter)
for x in karakter:
    print(x.capitalize(), end = ' ')