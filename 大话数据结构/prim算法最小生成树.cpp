//
// Created by 周磊 on 13/09/2017.
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




void MiniSpanTree_Prim(MGraph G) {
    int min, i, j, k;
    int adjvex[MAXVEX];
    int lowcost[MAXVEX];
    lowcost[0] = 0;
    adjvex[0] = 0;
    for (int i = 1; i < G.numVertexes; ++i) {
        lowcost[i] = G.arc[0][i];
        adjvex[i] = 0;
    }
    for (int i = 1; i < G.numVertexes; ++i) {
        min = INFINITY;
        j = 1;
        k = 0;
        while (j < G.numVertexes) {
            if (lowcost[j] != 0 && lowcost[j] < min) {
                min = lowcost[j];
                k = j;
            }
            j++;
        }
        
        printf("%d %d", adjvex[k], k);
        lowcost[k] = 0;
        for (int j = 1; j < G.numVertexes; ++j) {
            if (lowcost[j] != 0 && G.arc[k][j] < lowcost[j]) {
                lowcost[j] = G.arc[k][j];
                adjvex[j] = k;
            }
        }
    }
}