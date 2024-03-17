#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Öğrenci struct yapısı
struct Ogrenci {
    char ad[50];
    char soyad[50];
    int okul_numarasi;
    char fakulte[50];
    char bolum[50];
};

// Bağlı liste düğümü
struct Node {
    struct Ogrenci ogrenci;
    struct Node *next;
};

// Bağlı liste sınıfı
struct BagliListe {
    struct Node *bas;
    struct Node *son;
};

// Yeni bir bağlı liste oluşturma fonksiyonu
struct BagliListe *bagli_liste_olustur() {
    struct BagliListe *liste = (struct BagliListe*)malloc(sizeof(struct BagliListe));
    liste->bas = NULL;
    liste->son = NULL;
    return liste;
}

// Yeni bir öğrenci düğümü oluşturma fonksiyonu
struct Node *ogrenci_dugumu_olustur(struct Ogrenci ogrenci) {
    struct Node *dugum = (struct Node*)malloc(sizeof(struct Node));
    dugum->ogrenci = ogrenci;
    dugum->next = NULL;
    return dugum;
}

// Yeni öğrenci ekleme fonksiyonu
void yeni_ogrenci_ekle(struct BagliListe *liste) {
    struct Ogrenci yeni_ogrenci;
    printf("Ad: ");
    scanf("%s", yeni_ogrenci.ad);
    printf("Soyad: ");
    scanf("%s", yeni_ogrenci.soyad);
    printf("Okul Numarası: ");
    scanf("%d", &yeni_ogrenci.okul_numarasi);
    printf("Fakülte: ");
    scanf("%s", yeni_ogrenci.fakulte);
    printf("Bölüm: ");
    scanf("%s", yeni_ogrenci.bolum);

    struct Node *dugum = ogrenci_dugumu_olustur(yeni_ogrenci);
    if (liste->bas == NULL) {
        liste->bas = dugum;
        liste->son = dugum;
    } else {
        liste->son->next = dugum;
        liste->son = dugum;
    }
    printf("Öğrenci başarıyla eklendi.\n");
}

// Öğrenci bilgilerini görüntüleme fonksiyonu
void ogrenci_bilgilerini_goruntule(struct BagliListe *liste) {
    struct Node *gezici = liste->bas;
    while (gezici != NULL) {
        printf("Ad: %s\n", gezici->ogrenci.ad);
        printf("Soyad: %s\n", gezici->ogrenci.soyad);
        printf("Okul Numarası: %d\n", gezici->ogrenci.okul_numarasi);
        printf("Fakülte: %s\n", gezici->ogrenci.fakulte);
        printf("Bölüm: %s\n", gezici->ogrenci.bolum);
        gezici = gezici->next;
    }
}

// Öğrenci bilgilerini düzenleme fonksiyonu
void ogrenci_bilgilerini_duzenle(struct BagliListe *liste) {
    int okul_numarasi;
    printf("Düzenlemek istediğiniz öğrencinin okul numarasını girin: ");
    scanf("%d", &okul_numarasi);

    struct Node *gezici = liste->bas;
    while (gezici != NULL) {
        if (gezici->ogrenci.okul_numarasi == okul_numarasi) {
            printf("Yeni Ad: ");
            scanf("%s", gezici->ogrenci.ad);
            printf("Yeni Soyad: ");
            scanf("%s", gezici->ogrenci.soyad);
            printf("Yeni Okul Numarası: ");
            scanf("%d", &gezici->ogrenci.okul_numarasi);
            printf("Yeni Fakülte: ");
            scanf("%s", gezici->ogrenci.fakulte);
            printf("Yeni Bölüm: ");
            scanf("%s", gezici->ogrenci.bolum);
            printf("Öğrenci bilgileri başarıyla güncellendi.\n");
            return;
        }
        gezici = gezici->next;
    }
    printf("Belirtilen okul numarasına sahip bir öğrenci bulunamadı.\n");
}

// Öğrenci silme fonksiyonu
void ogrenci_sil(struct BagliListe *liste) {
    int okul_numarasi;
    printf("Silmek istediğiniz öğrencinin okul numarasını girin: ");
    scanf("%d", &okul_numarasi);

    struct Node *onceki = NULL;
    struct Node *gezici = liste->bas;
    while (gezici != NULL) {
        if (gezici->ogrenci.okul_numarasi == okul_numarasi) {
            if (onceki == NULL) {
                liste->bas = gezici->next;
            } else {
                onceki->next = gezici->next;
            }
            free(gezici);
            printf("Öğrenci başarıyla silindi.\n");
            return;
        }
        onceki = gezici;
        gezici = gezici->next;
    }
    printf("Belirtilen okul numarasına sahip bir öğrenci bulunamadı.\n");
}

// Bağlı liste hafızasını temizleme fonksiyonu
void bagli_liste_temizle(struct BagliListe *liste) {
    struct Node *gezici = liste->bas;
    while (gezici != NULL) {
        struct Node *temp = gezici;
        gezici = gezici->next;
        free(temp);
    }
    free(liste);
}

int main() {
    struct BagliListe *liste = bagli_liste_olustur();
    int secim;

    do {
        printf("\nBağlı Liste İşlemleri:\n");
        printf("1. Yeni Öğrenci Ekle\n");
        printf("2. Öğrenci Bilgilerini Görüntüle\n");
        printf("3. Öğrenci Bilgilerini Düzenle\n");
        printf("4. Öğrenci Sil\n");
        printf("5. Çıkış\n");
        printf("Seçiminizi yapın: ");
        scanf("%d", &secim);

        switch (secim) {
            case 1:
                yeni_ogrenci_ekle(liste);
                break;
            case 2:
                ogrenci_bilgilerini_goruntule(liste);
                break;
            case 3:
                ogrenci_bilgilerini_duzenle(liste);
                break;
            case 4:
                ogrenci_sil(liste);
                break;
            case 5:
                printf("Programdan çıkılıyor...\n");
                break;
            default:
                printf("Geçersiz seçim. Tekrar deneyin.\n");
        }
    } while (secim != 5);

    bagli_liste_temizle(liste);

    return 0;
}
