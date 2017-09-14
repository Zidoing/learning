//
// Created by 周磊 on 13/09/2017.
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


void BFSTraverse(GraphAdjList GL) {
    int i;
    EdgeNode *p;
    Queue Q;
    for (int i = 0; i < GL.numVertexes; ++i) {
        visited[i] = false;
    }
    InitQueue(&Q);
    for (int i = 0; i < GL.numVertexes; ++i) {
        if (!visited[i]) {
            visited[i] = true;
            printf("%c ", GL.adjList[i].data);
            EnQueue(&Q, i);
            while (!QueueEmpty(Q)) {
                DeQueue(&Q, &i);
                p = GL.adjList[i].firstedge;
                while (p) {
                    if (!visited[p->ajdvex]) {
                        visited[p->ajdvex] = true;
                        printf("%c ", GL.adjList[p->ajdvex].data);
                        EnQueue(&Q, p->ajdvex);
                    }
                    p = p->next;
                }

            }
        }
    }
}