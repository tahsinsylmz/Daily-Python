#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int iterativeArraySum(int *arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int recursiveArraySum(int *arr, int size) {
    if (size == 0) {
        return 0;
    } else {
        return arr[size - 1] + recursiveArraySum(arr, size - 1);
    }
}

int main() {
    int size;
    printf("Dizinin boyutunu girin: ");
    scanf("%d", &size);

    int arr[size];

    // Diziyi rastgele sayılarla doldur
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100; // 0 ile 99 arasında rasgele sayılar
    }

    // Iteratif toplama süresini hesapla
    clock_t startIterative = clock();
    int sumIterative = iterativeArraySum(arr, size);
    clock_t endIterative = clock();
    double timeIterative = ((double)(endIterative - startIterative)) / CLOCKS_PER_SEC;

    // Recursive toplama süresini hesapla
    clock_t startRecursive = clock();
    int sumRecursive = recursiveArraySum(arr, size);
    clock_t endRecursive = clock();
    double timeRecursive = ((double)(endRecursive - startRecursive)) / CLOCKS_PER_SEC;

    // Diziyi ekrana yazdır
    printf("Dizi Elemanlari: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Sonuçları ekrana yazdır
    printf("Iteratif Toplam: %d\n", sumIterative);
    printf("Iteratif Zaman: %f saniye\n", timeIterative);
    printf("Recursive Toplam: %d\n", sumRecursive);
    printf("Recursive Zaman: %f saniye\n", timeRecursive);

    return 0;
}
