//
// Created by 周磊 on 11/09/2017.
//

typedef char VertexType;
typedef int EdgeType;

typedef struct EdgeNode {
    int ajdvex;
    EdgeType weight;
    struct EdgeNode *next;
} EdgeNode;

typedef struct VertexNode {
    VertexType data;
    EdgeNode *firstedge;
} VertexNode, AdjList[MAXVEX];

typedef struct {
    AdjList adjList;
    int numVertexes, numEdges;
} GraphAdjList;

typedef int Boolean;
Boolean visited[MAXVEX];


void DFS(GraphAdjList GL, int i) {
    EdgeNode *p;
    visited[i] = true;
    printf("%c", GL.adjList[i].data);
    p = GL.adjList[i].firstedge;
    while (p) {
        if (!visited[p->ajdvex]) {
            DFS(GL, p->ajdvex);
        }
        p = p->next;
    }
}

void DFSTraverse(GraphAdjList GL) {
    int i;
    for (int j = 0; j < GL.numVertexes; ++j) {
        visited[j] = FALSE;
    }
    for (int k = 0; k < GL.numVertexes; ++k) {
        if (!visited[i]) {
            DFS(GL, i);
        }
    }
}