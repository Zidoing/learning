#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct Arr {
    int *pBase; //存储数组的一个地址
    int len;
    int cnt;
};

void init_arr(struct Arr *parr, int length) {
    parr->pBase = (int *) malloc(sizeof(int) * length);
    if (NULL == parr->pBase){
        return 0;
    }
}

bool append_arr();

bool insert_arr();

bool delete_arr();

int get();

bool is_empty();

bool is_full();

void sort_arr();

void show_arr();

void inversion_arr();


int main() {
    struct Arr arr;
    init_arr(&arr, 6);
    return 0;
}