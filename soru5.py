#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayiGirisi = input("Lütfen bir sayi giriniz: ")

ters=sayiGirisi[::-1]

if ters == sayiGirisi:
    print('Girilen sayi palindrom')
else:
    print('Girilen sayi palindrom değil.')







