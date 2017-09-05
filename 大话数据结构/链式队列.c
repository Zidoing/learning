//
// Created by 周磊 on 04/09/2017.
//

typedef int QElemType;

typedef struct QNode {
    QElemType data;
    struct QNode *next;
} QNode, *QueuePtr;

typedef struct {
    QueuePtr front, rear;
} LinkQueue;


Status EnQueue(LinkQueue *Q, QElemType e) {
    QueuePtr s = (QueuePtr) malloc(sizeof(QNode));
    if (!s) {
        exit(OVERFLOW);
    }
    s->data = e;
    s->next = NULL;
    Q->rear->next = s;
    Q->rear = s;
    return OK;
}


Status DeQueue(LinkQueue *Q, QElemType *e) {
    QueuePtr p;
    if (Q->front == Q->rear) {
        return Error;
    }
    p = Q->front->next;
    *e = p->data;
    Q->front->next = p->next;
    if (Q->rear = p) {
        Q->rear = Q->front;
    }
    free(p);
    return OK;
}