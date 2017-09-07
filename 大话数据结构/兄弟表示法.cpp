//
// Created by 周磊 on 07/09/2017.
//孩子兄弟表示法


typedef struct CSNode {
    TElemType data;
    struct CSNode *firstchild, *rightsid;
} CSNode, *CSTree;

