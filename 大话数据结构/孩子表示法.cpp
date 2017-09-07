//
// Created by 周磊 on 07/09/2017.
//

#define MAX_TREE_SIZE 100
typedef struct CTNode {
    int child;
    struct CTNode *next;
} *ChildPtr;


typedef struct {
    TElemtype data;
    ChildPtr firstchild;
} CTBox;


typedef struct {
    CTBox nodes[MAX_TREE_SIZE];
    int r,n;
}CTree;

