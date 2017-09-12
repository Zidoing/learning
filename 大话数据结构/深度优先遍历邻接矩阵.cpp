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

void DFS(MGraph G, int i) {
    int j;
    visited[i] = TRUE;
    printf("%c ", G.vex[i]);
    for (int k = 0; k < G.numVertexes; ++k) {
        if (G.arc[i][j] == 1 && !visited[j]) {
            DFS(G, j);
        }
    }
}


void DFSTraverse(MGraph G) {
    int i;
    for (int i = 0; i < G.numVertexes; ++i) {
        visited[i] = FALSE;
    }
    for (int i = 0; i < G.numVertexes; ++i) {
        if (!visited[i]) {
            DFS(G, i);
        }
    }
}