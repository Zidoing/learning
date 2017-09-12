//
// Created by 周磊 on 11/09/2017.
//

typedef char VertexType;
typedef int EdgeType;
#define MAXVEX 100
#define INFINITY 65535
typedef struct {
    VertexType vex[MAXVEX];
    EdgeType arc[MAXVEX][MAXVEX];
    int numVertexes, numEdges;
} MGraph;

typedef int Boolean;
Boolean visited[MAX];

void BFSTraverse(MGraph G) {
    Quene Q;
    for (int i = 0; i < G.numVertexes; ++i) {
        visited[i] = false;
    }
    initQuene(&Q);
    for (int j = 0; j < G.numVertexes; ++j) {
        if (!visited[j]) {
            visited[j] = true;
            print("%c", G.vex[j]);
            EnQueue(&Q, j);
            while (!QueueEmpty(Q)) {
                DeQueue(&Q, &i);
                for (int i = 0; i < G.numVertexes; ++j) {
                    if (G.arc[j][i] == 1 && !visited[j]) {
                        visited[i] = true;
                        print("%c", G.vex[i]);
                        EnQueue(&Q, j);
                    }
                }
            }
        }

    }
}