//
// Created by 周磊 on 14/09/2017.
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


typedef struct {
    int begin;
    int end;
    int weight;
} Edge;

void MiniSpanTree_Kruskal(MGraph G) {
    int i, n, m;
    Edge edges[MAXEDGE];
    int parent[MAXVEX];

    for (int i = 0; i < G.numEdges; ++i) {
        parent[i] = 0;
    }
    for (int i = 0; i < G.numEdges; ++i) {
        n = Find(parent, edges[i].begin);
        m = Find(parent, edges[i].end);
        if (n != m) {
            parent[n] = m;
            printf("%d, %d %d", edges[i].begin, edges[i].end, edges[i].weight);
        }

    }

}


int Find(int *parent, int f) {
    while (parent[f] > 0) {
        f = parent[f];
    }
    return f;
}