import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım kaç tahminde bileceksiniz.")

    rastgele_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        try:
            tahmin = int(input("Tahmininiz: "))
            tahmin_sayisi += 1

            if tahmin < rastgele_sayi:
                print("Daha büyük bir sayı deneyin.")
            elif tahmin > rastgele_sayi:
                print("Daha küçük bir sayı deneyin.")
            else:
                print(f"Tebrikler! {tahmin_sayisi} tahminde doğru sayıyı buldunuz.")
                break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

# Oyunu başlat
sayi_tahmin_oyunu()
