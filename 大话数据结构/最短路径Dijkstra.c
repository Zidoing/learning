#define MAXVEX 9
#define INFINITY 65535
typedef int Pathmatirx[MAXVEX]; //用于存储最短路径下表的数组
typedef int ShortPathTable[MAXVEX]; //用于存储到各点最短路径的权值和
typedef char VertexType;
typedef int EdgeType;
#define MAXVEX 100
#define INFINITY 65535
typedef struct {
    VertexType vex[MAXVEX];
    EdgeType arc[MAXVEX][MAXVEX];
    int numVertexes, numEdges;
} MGraph;

void ShortestPath_Dijkstra(MGraph G, int v0, Pathmatirx *P, ShortPathTable *D) {
    int v, w, k, min;
    int final[MAXVEX];//表示求得顶点v0到vw的最短路径
    for (int v = 0; v < G.numVertexes; ++v) {
        final[v] = 0;//全部顶点初始化为未知最短路径状态
        (*D)[v] = G.arc[v0][v];//将与 v0有连线的点加上权值
        (*P)[v] = 0;//初始化路径p数组为0
    }
    (*D)[v0] = 0; //v0 - v0  为0
    final[v0] = 1; // v0 - vo0 不需要求路径

    //开始主循环，每次求得v0到某个v顶点的最短路径
    for (int v = 1; v < G.numVertexes; ++v) {
        min = INFINITY;//当前所知离v0顶点最近的距离
        for (int w = 0; w < G.numVertexes; ++w)//寻找与v0最近的距离
        {
            if (!final[w] && (*D)[w] < min) {
                k = w;
                min = (*D)[w];
            }
        }

        final[k] = 1;
        //修正当前最短路径的距离
        for (int w = 0; w < G.numVertexes; ++w) {
            //如果经过v顶点的路径比现在这条路径的长度短的话
            if (!final[w] && (min + G.arc[k][w] < (*D)[w])) {
                (*D)[w] = min + G.arc[k][w];
                (*P)[w] = k;
            }
        }
    }
}


int main(int argc, char const *argv[]) {
    /* code */
    return 0;
}
