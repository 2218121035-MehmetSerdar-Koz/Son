import random

def tahmin_et(sayi, tahmin):
    """Rastgele seçilen bir sayı ile tahmini karşılaştırır."""
    if tahmin < sayi:
        return "Daha büyük"
    elif tahmin > sayi:
        return "Daha küçük"
    else:
        return "Doğru"

def sayi_tahmin_oyunu(tahminler=None):
    """Sayı tahmin oyununu çalıştırır."""
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım kaç tahminde bileceksiniz.")

    rastgele_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    if tahminler is None:
        tahminler = []

    for tahmin in tahminler:
        tahmin_sayisi += 1
        print(f"Tahmininiz: {tahmin}")

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı deneyin.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı deneyin.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} tahminde doğru sayıyı buldunuz.")
            return

    print("Maalesef doğru sayıyı bulamadınız.")
    print(f"Tuttuğum sayı: {rastgele_sayi}")

if __name__ == "__main__":
    # Komut satırında manuel test etmek için varsayılan tahminler:
    test_tahminler = [10, 50, 75, 63]
    sayi_tahmin_oyunu(test_tahminler)
