//
// Created by 周磊 on 07/09/2017.
//

typedef struct BiTNode {
    TElemType data;
    struct BiTNode *lchild, *rchild;
} BiTNode, *BiTree;