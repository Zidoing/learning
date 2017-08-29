//
// Created by 周磊 on 29/08/2017.
//

#include <stdio.h>


int Fbi(int i) {
    if (i < 2) {
        return i == 0 ? 0 : 1;
    }
    return Fbi(i - 1) + Fbi(i - 2);
}

int main() {
    int i;
    int a[40];
    a[0] = 0;
    a[1] = 1;
    printf("%d ", a[0]);
    printf("%d ", a[1]);
    for (int j = 2; j < 40; ++j) {
        a[j] = a[j - 1] + a[j - 2];
        printf("%d ", a[j]);

    }
    printf("\n");


    for (int k = 0; k < 40; ++k) {
        printf("%d ", Fbi(k));
    }

    return 0;
}