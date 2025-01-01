import unittest
from Tahmin import tahmin_et  # Tahmin.py dosyasındaki tahmin_et fonksiyonunu çağırıyor

class TestSayiTahminOyunu(unittest.TestCase):

    def test_daha_buyuk(self):
        self.assertEqual(tahmin_et(50, 30), "Daha büyük")

    def test_daha_kucuk(self):
        self.assertEqual(tahmin_et(50, 70), "Daha küçük")

    def test_dogru(self):
        self.assertEqual(tahmin_et(50, 50), "Doğru")

if __name__ == "__main__":
    unittest.main()
