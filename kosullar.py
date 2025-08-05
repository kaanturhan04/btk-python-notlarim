# kosullar.py

# Kullanıcıdan yaş bilgisi alıp reşit olup olmadığını kontrol eden program
yas = int(input("Yaşınızı girin: "))

if yas >= 18:
    print("Reşitsiniz.")
else:
    print("Reşit değilsiniz.")

# Sıcaklık kontrolü
sicaklik = float(input("Sıcaklığı girin (°C): "))

if sicaklik > 30:
    print("Bugün hava sıcak.")
elif sicaklik >= 20:
    print("Bugün hava ılık.")
else:
    print("Bugün hava serin veya soğuk.")

# Sayı pozitif mi negatif mi kontrolü
sayi = float(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif bir sayı girdiniz.")
elif sayi < 0:
    print("Negatif bir sayı girdiniz.")
else:
    print("Sıfır girdiniz.")
