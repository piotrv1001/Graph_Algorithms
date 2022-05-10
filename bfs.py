
def BFS(adj, src, dest, v, pred, dist):
 
    queue = []
  
    visited = [False for i in range(v)]
  
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1
     
    visited[src] = True
    dist[src] = 0
    queue.append(src)
  
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
  
                if (adj[u][i] == dest):
                    return True;
  
    return False;
  
def getShortestDistance(adj, s, dest, v):
     
    pred = [0 for _ in range(v)]
    dist = [0 for _ in range(v)]
  
    if (BFS(adj, s, dest, v, pred, dist) == False):
        return ()
  
    path = []
    crawl = dest
    path.append(crawl)
     
    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]
    
    shortestDistanceLength = dist[dest]
    shortestDistance = [] 
    for i in range(len(path)-1, -1, -1):
        shortestDistance.append(path[i])
    shortestDistanceString = '-'.join([str(x) for x in shortestDistance])

    return (shortestDistanceString, shortestDistanceLength)
  