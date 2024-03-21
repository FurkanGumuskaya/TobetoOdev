#Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

r = int(input("yari çap giriniz: "))
pi = 3.14
alan = (pi * r**2) / 2
cevre = float(2 * pi * r)

print("alani: ", alan)
print("çevresi: ", cevre)
print(f"pi {pi} kabul edilmiştir")

