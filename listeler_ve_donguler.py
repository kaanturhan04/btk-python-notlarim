# Listeler ve Döngüler - BTK Python Eğitimi Notları

# Liste oluşturma
meyveler = ["elma", "armut", "muz", "çilek"]
print("Meyveler listesi:", meyveler)

# Liste elemanlarına erişim
print("İlk meyve:", meyveler[0])
print("Son meyve:", meyveler[-1])

# Listeye eleman ekleme
meyveler.append("kivi")
print("Yeni meyveler listesi:", meyveler)

# Liste döngüsü
print("Tüm meyveler:")
for meyve in meyveler:
    print("-", meyve)

# Sayılar listesi ve toplama
sayılar = [1, 2, 3, 4, 5]
toplam = 0
for sayı in sayılar:
    toplam += sayı
print("Sayıların toplamı:", toplam)
