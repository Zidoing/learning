//
// Created by 周磊 on 07/09/2017.
//

typedef enum {
    Link, Thread
} PointerTag;


typedef struct BiThrNode {
    TElemType data;
    struct BiThrNode *lchild, *rchild;
    PointerTag LTag;
    PointerTag RTag;
} BiThrNode, *BiThrTree;


BiThrTree pre;

void InThreading(BiThrTree p) {  //生成线索二叉树
    if (p) {
        InThreading(p->lchild);
        if (!p->lchild) {
            p->LTag = Thread;
            p->lchild = pre;
        }
        if (!pre->rchild) {
            p->RTag = Thread;
            p->rchild = p;
        }
        pre = p;
        InThreading(p->rchild);
    }

}


Status InOrderTraverse_Thr(BiThrTree T) { //线索二叉树遍历（！！！！！）
    BiThrTree p;
    p = T->lchild;
    while (p != T) {
        while (p->LTag == Link)
            p = p->lchild;
        printf("%c", p->data);
        while (p->RTag == Thread && p->rchild != T) {
            p = p->rchild;
            printf("%c", p->data);
        }
        p = p->rchild;
    }
    return ok;
}