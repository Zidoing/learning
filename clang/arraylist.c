//
// Created by 周磊 on 08/08/2017.
//
#include <stdbool.h>


struct Arr {
    int *pBase; //存储数组的一个地址
    int len;
    int cnt;
};

void init_arr();

bool append_arr();

bool insert_arr();

bool delete_arr();

int get();

bool is_empty();

bool is_full();

void sort_arr();

void show_arr();

void inversion_arr();