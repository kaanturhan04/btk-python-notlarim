# fonksiyonlar.py

# Basit bir fonksiyon: Merhaba mesajı
def selamla():
    print("Merhaba, Python'a hoş geldin!")

selamla()


# Parametreli fonksiyon: İsimle selamla
def selamla_isimle(isim):
    print(f"Merhaba, {isim}!")

selamla_isimle("Kaan")


# Toplama yapan fonksiyon
def topla(a, b):
    return a + b

sonuc = topla(10, 5)
print(f"Toplam: {sonuc}")


# Yaş kontrolü yapan fonksiyon
def reşit_mi(yas):
    if yas >= 18:
        return "Reşit"
    else:
        return "Reşit değil"

print(reşit_mi(20))
print(reşit_mi(16))


# Bonus: Kullanıcıdan alınan değerlerle fonksiyon kullanımı
def kare_al(sayi):
    return sayi ** 2

girdi = int(input("Bir sayı girin: "))
print(f"{girdi} sayısının karesi: {kare_al(girdi)}")
