//
// Created by 周磊 on 29/08/2017.
//
#define MAXSIZE 5

typedef int SElemType;
typedef struct {
    SElemType data[MAXSIZE];
    int top;
} SqStack;


Status Push(SqStack *S, SElemType e) {
    if (S->top == MAXSIZE - 1) {
        return Error; //栈满
    }
    S->top++;
    S->data[S->top] = e;
    return OK;
}


Status Pop(SqStack *s, SElemType *e) {
    if (s->top == -1) {
        return Error; //空栈
    }
    *e = s->data[s->top];
    s->top--;
    return OK;
}