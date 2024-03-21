#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

kullanciBoy = int(input("Lütfen Boyunuzu giriniz: ")) / 100
kullaniciAgirlik = int(input("lütfen kilonuzu giriniz "))

VKİ = float(kullaniciAgirlik/(kullanciBoy*kullanciBoy))
VKİ = round(VKİ, 1)
print("Vücut Kitle İndeksi (VKİ):", VKİ)

if VKİ < 18.5:
    print("Zayifsiniz")
elif 18.5<= VKİ <= 24.9:
    print("Normalsiniz")
elif 25 <= VKİ <= 29.9:
    print("Hafif şişmansiniz")
elif 30 <= VKİ <= 34.9:
    print("Orta derecede şişmansiniz")
elif 35 <= VKİ <= 39.9:
    print("Ağir derecede şişmansiniz")
else:
    print("Çok ağir derecede şişmansiniz")



#round çıkan değeri yuvarlar
# 1 ise virgülden sonra 1 değer al