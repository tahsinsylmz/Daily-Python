import pickle
import os
from prettytable import PrettyTable

def dosya_yolu_olustur(dosya_adi):
    return os.path.join(os.getcwd(), dosya_adi)

def kayit_ekle():
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    numara = input("Numara: ")
    bolum = input("Bölüm: ")
    cinsiyet = input("Cinsiyet: ")
    dogum_yeri = input("Doğum Yeri: ")
    yas = input("Yaş: ")
    telefon = input("Telefon Numarası: ")

    ogrenci = {
        'ad': ad,
        'soyad': soyad,
        'numara': numara,
        'bolum': bolum,
        'cinsiyet': cinsiyet,
        'dogum_yeri': dogum_yeri,
        'yas': yas,
        'telefon': telefon
    }

    dosya_adi = "ogrenciler.dat"
    dosya_yolu = dosya_yolu_olustur(dosya_adi)

    try:
        with open(dosya_yolu, 'a+b') as dosya:
            dosya.seek(0, 2)  # Dosyanın sonuna git
            pickle.dump(ogrenci, dosya)
        print("Kayıt başarıyla eklendi.")
    except Exception as e:
        print("Hata:", str(e))

def kayitlari_listele():
    dosya_adi = "ogrenciler.dat"
    dosya_yolu = dosya_yolu_olustur(dosya_adi)

    try:
        with open(dosya_yolu, 'rb') as dosya:
            tablo = PrettyTable()
            tablo.field_names = ["Ad", "Soyad", "Numara", "Bölüm", "Cinsiyet", "Doğum Yeri", "Yaş", "Telefon"]

            while True:
                try:
                    ogrenci = pickle.load(dosya)
                    tablo.add_row([ogrenci['ad'], ogrenci['soyad'], ogrenci['numara'], ogrenci['bolum'],
                                   ogrenci['cinsiyet'], ogrenci['dogum_yeri'], ogrenci['yas'], ogrenci['telefon']])
                except EOFError:
                    break

            print(tablo)
    except Exception as e:
        print("Hata:", str(e))

def kayit_ara():
    dosya_adi = "ogrenciler.dat"
    dosya_yolu = dosya_yolu_olustur(dosya_adi)

    try:
        with open(dosya_yolu, 'rb') as dosya:
            kriter = input("Arama kriteri girin (ad, soyad, numara, bolum, cinsiyet, dogum_yeri, yas, telefon): ")
            deger = input(f"{kriter.capitalize()} girin: ")

            while True:
                try:
                    ogrenci = pickle.load(dosya)
                    if ogrenci.get(kriter) == deger:
                        print(ogrenci)
                except EOFError:
                    break
    except Exception as e:
        print("Hata:", str(e))

def kayit_duzenle():
    dosya_adi = "ogrenciler.dat"
    dosya_yolu = dosya_yolu_olustur(dosya_adi)

    try:
        kriter = input("Düzenleme yapılacak öğrencinin numarasını girin: ")

        with open(dosya_yolu, 'rb') as dosya:
            ogrenciler = []

            try:
                while True:
                    ogrenci = pickle.load(dosya)
                    ogrenciler.append(ogrenci)
            except EOFError:
                pass

        bulunan_ogrenci = None
        for ogrenci in ogrenciler:
            if ogrenci['numara'] == kriter:
                bulunan_ogrenci = ogrenci
                break

        if bulunan_ogrenci:
            print("Bulunan Öğrenci Bilgileri:")
            print(bulunan_ogrenci)

            yeni_ad = input("Yeni Ad (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['ad']
            yeni_soyad = input("Yeni Soyad (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['soyad']
            yeni_numara = input("Yeni Numara (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['numara']
            yeni_bolum = input("Yeni Bölüm (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['bolum']
            yeni_cinsiyet = input("Yeni Cinsiyet (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['cinsiyet']
            yeni_dogum_yeri = input("Yeni Doğum Yeri (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['dogum_yeri']
            yeni_yas = input("Yeni Yaş (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['yas']
            yeni_telefon = input("Yeni Telefon Numarası (Enter'e basarak eski değeri koruyabilirsiniz): ").strip() or bulunan_ogrenci['telefon']

            yeni_ogrenci = {
                'ad': yeni_ad,
                'soyad': yeni_soyad,
                'numara': yeni_numara,
                'bolum': yeni_bolum,
                'cinsiyet': yeni_cinsiyet,
                'dogum_yeri': yeni_dogum_yeri,
                'yas': yeni_yas,
                'telefon': yeni_telefon
            }

            ogrenciler.remove(bulunan_ogrenci)
            ogrenciler.append(yeni_ogrenci)

            with open(dosya_yolu, 'wb') as dosya:
                for ogrenci in ogrenciler:
                    pickle.dump(ogrenci, dosya)

            print("Öğrenci bilgileri başarıyla güncellendi.")
        else:
            print(f"Numara '{kriter}' ile eşleşen öğrenci bulunamadı.")
            
    except Exception as e:
        print("Hata:", str(e))

while True:
    print("\n***********************************************")
    print("1-Kayıt Ekle\n2-Kayıtları Listele\n3-Kayıt Ara\n4-Kayıt Düzenle\n5-Çıkış")

    secim = input("Lütfen bir seçenek girin (1-5): ")

    if secim == '1':
        kayit_ekle()
    elif secim == '2':
        kayitlari_listele()
    elif secim == '3':
        kayit_ara()
        pass
    elif secim == '4':
        kayit_duzenle()
        pass
    elif secim == '5':
        print("Çıkış yapılıyor. İyi günler!")
        break
    else:
        print("Geçersiz seçenek. Lütfen 1-5 arasında bir seçenek girin.")
