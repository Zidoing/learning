//
// Created by 周磊 on 07/09/2017.
//

typedef struct BiTNode {
    TElemType data;
    struct BiTNode *lchild, *rchild;
} BiTNode, *BiTree;

void CreateBiTree(BiTree *T) {
    TElemType ch;
    scanf("%c", &ch);
    if (ch == '#') {
        *T = NULL;
    } else {
        *T = (BiTree) malloc(sizeof(BiTNode))；
        if (!*T)
            exit(OVERFLOW);
        (*T)->data = ch;
        CreateBiTree(&(*T)->lchild);
        CreateBiTree(&(*T)->rchild);
    }
}