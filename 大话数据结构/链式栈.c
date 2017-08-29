//
// Created by 周磊 on 29/08/2017.
//

typedef int SElemType;
typedef struct StackNode {
    SElemType data;
    struct StackNode *next;
} StackNode, *LinkStackPtr;


typedef struct LinkStack {
    LinkStackPtr top;
    int count;
} LinkStack;


Status Push(LinkStack *S, SElemType e) {
    LinkStackPtr s = (LinkStackPtr) malloc(sizeof(StackNode));
    s->data = e;
    s->next = S->top;
    S->top = s;
    S->count++;
    return OK;
}


Status Pop(LinkStack *S, SElemType *e) {
    LinkStackPtr p;
    if (StackEmpty(*S))
        return Error;
    *e = S->top->data;
    p = S->top;
    S->top = p->next;
    free(p);
    S->count--;
    return OK;
}