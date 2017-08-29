//
// Created by 周磊 on 29/08/2017.
//

#define Error 0
#define OK 1
typedef int SElemType;

typedef struct {
    SElemType data[MAXSIZE];
    int top1;
    int top2;
} SqDoubleStack;


Status Push(SqDoubleStack *s, SElemType e, int stackNumber) {
    if (s->top1 + 1 == s->top2) {
        return ERROR; //栈满
    }
    if (stackNumber == 1) {
        s->top1++;
        s->data[s->top1] = e;
    } else if (stackNumber == 2) {
        s->top2--;
        s->data[s->top2] = e;
    }
    return OK;
}


Status Pop(SqDoubleStack *s, SElemType *e, int stackNumber) {
    if (stackNumber == 1) {
        if (s->top1 == -1) {
            return Error;//栈满
        }
        *e = s->data[s->top1];
        s->top1--;
    } else if (stackNumber == 2) {
        if (s->top2 == MAXSIZE) {
            return Error;//栈满
        }
        *e = s->data[s->top2];
        s->top2++;
    }
    return OK;
}