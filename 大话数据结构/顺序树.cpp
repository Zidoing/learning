//
// Created by 周磊 on 06/09/2017.
// 双亲表示法
//

#define MAXSIZE 100
typedef int TElemType;
typedef struct PTNode{
    TElemType data;
    int parent;
}PTNode;

typedef struct {
    PTNode nodes[MAXSIZE];
    int r,n ; //根的位置和节点数
}PTree;