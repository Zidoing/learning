//
// Created by 周磊 on 09/09/2017.
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


void CreateALGraph(GraphAdjList *G) {
    int i, j, k;
    EdgeNode *e;
    printf("请输入顶点和边数");
    scanf("%d,%d", &G->numVertexes, &G->numEdges);
    for (i = 0; i < G->numVertexes; ++i) {
        scanf(&G->adjList[i].data);
        G->adjList[i].firstedge = NULL;
    }
    for (int k = 0; k < G->numEdges; ++k) {
        printf("输入边vi，vj上的顶点序号");
        scanf("%d,%d", &i, &j);
        e = (EdgeNode *) malloc(sizeof(EdgeNode));
        e->ajdvex = j;
        e->next = G->adjList[i].firstedge;
        G->adjList[i].firstedge = e;

        e = (EdgeNode *) malloc(sizeof(EdgeNode));
        e->ajdvex = i;
        e->next = G->adjList[j].firstedge;
        G->adjList[j].firstedge = e;

    }
}