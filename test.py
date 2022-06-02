import fileHandler
import floydWarshall
import bfs
import time

def runTestFloydWarshall(graphFiles):

    # My comment
    print("Nodes\t\tRoutes\t\tExecution time")

    for graphFile in graphFiles:

        startTime = time.time()

        graph = fileHandler.fileToGraph(graphFile)
        V = len(graph[0])
        dis = [[-1 for _ in range(floydWarshall.LIMIT)] for _ in range(floydWarshall.LIMIT)]
        Next = [[-1 for _ in range(floydWarshall.LIMIT)] for _ in range(floydWarshall.LIMIT)]

        print(str(V).ljust(len("Nodes")), end = "\t\t")
 
        floydWarshall.floydWarshall(V, graph, dis, Next)

        fileStrings = []

        for i in range(V):
            for j in range(V):
                if i == j:
                    continue
                # path = floydWarshall.printPath(floydWarshall.constructPath(i, j, Next))
                path = floydWarshall.createPath(i, j, Next)
                fileString = "d[{i},{j}] = {dis} PATH: {path}\n".format(i = i + 1, j = j + 1, dis = dis[i][j], path = path)
                if path != "":
                    fileStrings.append(fileString)

        print(str(len(fileStrings)).ljust(len("Routes")), end = "\t\t")

        graphOutputFile = graphFile.replace(".txt", "_out.txt")
        fileHandler.pathsToFile(graphOutputFile, fileStrings)

        executionTime = (time.time() - startTime) * 1000
        if executionTime > 1000:
            executionTime = executionTime / 1000
            print("{0:.2f} s".format(executionTime))
        else:
            print("{0:.2f} ms".format(executionTime))
        

def runTestBFS(bfsInput):

    print("Graph\t\tStart vertex\t\tEnd vertex\t\tShortest path\t\t\tLength\t\tExecution time")

    for key in bfsInput.keys():

        startTime = time.time()

        adj = fileHandler.fileToGraphBFS(key)
        v = len(adj)
        for vertices in bfsInput[key]:
            source = vertices[0]
            dest = vertices[1]
            result = bfs.getShortestDistance(adj, source, dest, v)
            if result:
                path, length = result
            else:
                path = "----"
                length = "----"
            print(key.replace("Lab5_files/", "").ljust(len("Graph           ")), end = "")
            print(str(source).ljust(len("Start vertex            ")), end = "")
            print(str(dest).ljust(len("End vertex              ")), end = "")
            print(path.ljust(len("Shortest path                   ")), end = "")
            print(str(length).ljust(len("Length          ")), end = "")

            executionTime = (time.time() - startTime) * 1000
            if executionTime > 1000:
                executionTime = executionTime / 1000
                print("{0:.2f} s".format(executionTime))
            else:
                print("{0:.2f} ms".format(executionTime))


def runTestMaze(mazeInput):

    for file in mazeInput:

        startTime = time.time()

        adj = fileHandler.fileToGraphMaze(file)[0]
        v = len(adj)
        source = fileHandler.fileToGraphMaze(file)[1]
        dest = fileHandler.fileToGraphMaze(file)[2]
        result = bfs.getShortestDistance(adj, source, dest, v)
        if result:
            path, length = result
        else:
            path = "----"
            length = "----"
        print("Shortest path: " + path)
        print("Length: " + str(length))
        print("Execution time: ", end = '')

        fileHandler.graphToFileMaze(file, path)
        executionTime = (time.time() - startTime) * 1000
        if executionTime > 1000:
            executionTime = executionTime / 1000
            print("{0:.2f} s".format(executionTime))
        else:
            print("{0:.2f} ms".format(executionTime))

        print("")
