//
// Created by 周磊 on 21/10/2017.
//

typedef struct BiTNode {
    int data;
    struct BiTNode *lchild, *rchild;
} BiTNode, *BiTree;


typedef int Status;

Status SearchBST(BiTree T, int key, BiTree f, BiTree *p) {
    if (!T) {
        *p = f;
        return false;
    } else if (key == T->data) {
        *p = T;
        return true;
    } else if (key < T->data) {
        return SearchBST(T->lchild, key, T, p);
    } else
        return SearchBST(T->rchild, key, T, p);
}

Status InsertBST(BiTree *T){
 BiTree p,s;
    if(!SearchBST(*T,key,NULL,&p)){
        s = (BiTree)malloc(sizeof(BiTNode));
        s->data = key;
        s->lchild = s->rchild = NULL;
        if(!p)
            *T = s;
        else if(key<p->data)
            p->lchild = s;
        else
            p->rchild =s;
        return true;
    }
    return false;
}