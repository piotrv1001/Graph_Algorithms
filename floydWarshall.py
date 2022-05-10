LIMIT = 2000
INF = 10**7

def floydWarshall(V, graph, dis, Next):

    for i in range(V):
        for j in range(V):
            dis[i][j] = graph[i][j]
 
            if (graph[i][j] == INF):
                Next[i][j] = INF
            else:
                Next[i][j] = j

    for k in range(V):
        for i in range(V):
            for j in range(V):
                 
                if (dis[i][k] == INF or dis[k][j] == INF):
                    continue
                if (dis[i][j] > dis[i][k] + dis[k][j]):
                    dis[i][j] = dis[i][k] + dis[k][j]
                    Next[i][j] = Next[i][k]
 

def createPath(u, v, Next):

    if (Next[u][v] == INF):
        return ""
    stringPath = str(u)
    while u != v:
        u = Next[u][v]
        stringPath += str(u)

    return stringPath
