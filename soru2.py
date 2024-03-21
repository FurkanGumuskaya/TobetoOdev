#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

kullaniciMaaş = int(input("lütfen maaşinizi giriniz: "))
kullaiciZam = int(input("lütfen zam oranini giriniz: %"))

kullaniciMaaş += (kullaniciMaaş*kullaiciZam)/100

print("Güncel Maaşiniz:", kullaniciMaaş)

