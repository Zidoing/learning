//
// Created by 周磊 on 23/08/2017.
//

#include <stdio.h>

typedef int ElemType;
typedef struct Node {
    ElemType data;
    struct Node *next;
} Node;


typedef struct Node *LinkList;