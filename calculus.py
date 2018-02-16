print("Hesap Makinesi")

a=int(input("1. Sayı:"))
b=int(input("2. Sayı:"))
islem=input("işlem seçiniz")

if islem=="1":
    print("{} ile {} toplam:{}".format(a,b,a+b))
elif islem=="2":
    print("{} ile {} toplam:{}".format(a,b,a-b))
elif islem=="3":
    print("{} ile {} toplam:{}".format(a,b,a*b))
elif islem=="4":
    print("{} ile {} toplam:{}".format(a,b,a/b))
else:
    print("Geçersiz İşlem")
