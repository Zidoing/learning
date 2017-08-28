//
// Created by 周磊 on 23/08/2017.
// 单链表
//

#include <stdio.h>

#define ERROR 0
#define OK 1

typedef int Status;
typedef int ElemType;
typedef struct Node {
    ElemType data;
    struct Node *next;
} Node;

int j;

typedef struct Node *LinkList;


Status GetElem(LinkList L, int i, ElemType *e) {
    int j;
    LinkList p;
    p = L->next;  //指向第一个元素
    j = 1;
    while (p && j < i) {  //当指针为不为空，或者当前数目小于要查询的地方
        p = p->next;
        ++j;
    }
    if (!p || j > i) {
        return ERROR;
    }
    *e = p->data;
    return OK;
}

// 单链表插入
Status ListInsert(LinkList L, int i, ElemType e) {
    int j;
    LinkList p, s;
    p = L;
    j = 1;
    while (p && j < i) {
        p = p->next;
        j++;
    }
    if (!p || j > i) {
        return ERROR;
    }
    s = (LinkList) malloc(sizeof(Node));
    s->data = e;
    s->next = p->next;
    p->next = s;
    return OK;
}

// 单链表删除
Status ListDelete(LinkList L, int i, ElemType *e) {
    int j = 1;
    LinkList p, q;
    p = L;
    while (p->next && j < i) {
        p = p->next;
        j++;
    }
    if (!(p->next) || j > i) {
        return ERROR;
    }
    q = p->next;
    *e = q->data;
    p->next = q->next;
    free(q);
    return OK;
}

void CreateListHead(LinkList *L, int n) {
    LinkList p;
    int i;
    srand(time(0));
    *L = (LinkList) malloc(sizeof(Node));
    (*L)->next = NULL;
    for (int k = 0; k < n; ++k) {
        p = (LinkList) malloc(sizeof(Node));
        p->data = rand() % 100 + 1;
        p->next = (*L)->next;
        (*L)->next = p;
    }
}

void CreateListTail(LinkList *L, int n) {
    LinkList p, r;
    int i;
    srand(time(0));
    *L = (LinkList) malloc(sizeof(Node));
    r = *L;
    for (int k = 0; k < n; ++k) {
        p = (Node *) malloc(sizeof(Node));
        p->data = rand() % 100 + 1;
        r->next = p;
        r = p;
    }
    r->next = NULL;
}


Status ClearList(LinkList *L) {
    LinkList p, q;
    p = (*L)->next;
    while (p) {
        q = p->next;
        free(q);
        p = q;
    }
    (*L)->next = NULL;
    return OK;
}