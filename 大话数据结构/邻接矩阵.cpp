//
// Created by 周磊 on 09/09/2017.
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

void CreateMGraph(MGraph *G) {
    int i, j, k, w;
    printf("请输入顶点和边数");
    scanf("%d,%d", &G->numVertexes, &G->numEdges);
    for (i = 0; i < G->numVertexes; ++i) {
        scanf(&G->vex[i]);
    }
    for (i = 0; i < G->numVertexes; ++i) {
        for (j = 0; j < G->numVertexes; ++j) {
            G->arc[i][j] = INFINITY;
        }
    }
    for (k = 0; k < G->numEdges; k++) {
        printf("输入边vi，vj的上下标，和权值w");
        scanf("%d,%d,%d", &i, &j, &w);
        G->arc[i][j] = w;
        G->arc[j][i] = G->arc[i][j];
    }
}