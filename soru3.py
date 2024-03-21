#Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 =int(input("1. Sayiyi giriniz: "))
sayi2 =int(input("2. Sayiyi giriniz: "))
sayi3 =int(input("3. Sayiyi giriniz: "))
if sayi1 > sayi2 and sayi3:
    print("En büyük sayi:", sayi1)
elif sayi2 > sayi1 and sayi3:
    print("En büyük sayi: ",sayi2)
elif sayi3 > sayi1 and sayi2:
    print("En büyük sayi: ",sayi3)







#sayiListesi = []
#sayiListesi.append(int(input("1. Sayiyi giriniz: ")))
#sayiListesi.append(int(input("2. Sayiyi giriniz: ")))
#sayiListesi.append(int(input("3. Sayiyi giriniz: ")))
#print(max(sayiListesi))


# Bu şekilde boş bir liste oluşturup kullanıcıdan içine değer girmesini isteyip sonra max fonksiyonunu kullanarak da yapılabilir.