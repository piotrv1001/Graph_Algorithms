def fileToGraph(filename):

    with open(filename, 'r') as f:

        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

        data = [line.split() for line in lines]

        INF = 10**7
        nodes = int(data[0][0])
        graph = [[0 if i == j else INF for j in range(nodes)]for i in range(nodes)]

        for item in data[1:]:
            i = int(item[0]) - 1
            j = int(item[1]) - 1
            graph[i][j] = int(item[2])
                
        return graph

def pathsToFile(filename, fileStrings):

    with open(filename, 'w') as f:

        f.writelines(fileStrings)

def fileToGraphBFS(filename):

    with open(filename, 'r') as f:

        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

        data = [line.split() for line in lines]

        nodes = int(data[0][0])
        graph = [[] for _ in range(nodes + 1)]

        for item in data[1:]:
            graph[int(item[0])].append(int(item[1]))
            # graph[int(item[1]) - 1].append(int(item[0]))

        return graph

def fileToGraphMaze(filename):

    with open(filename, 'r') as f:

        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

        firstLine = lines[0]
        firstLineList = firstLine.split()
        n = int(firstLineList[0])
        nodes = int(firstLineList[0]) * int(firstLineList[1])
        maze = [[] for _ in range(nodes)]

        data = lines[1:]

        sourceVertex = 0
        destinationVertex = 0

        mazeString = ''.join(data)
        mazeList = []

        for i in range(nodes):

            if mazeString[i] != 'x':

                mazeList.append(i)

                if mazeString[i] == 'I':

                    sourceVertex = i

                elif mazeString[i] == 'O':

                    destinationVertex = i

        for vertex in mazeList:

            if (vertex - n) in mazeList:

                maze[vertex].append(vertex - n)

            if (vertex + n) in mazeList:

                maze[vertex].append(vertex + n)

            if (vertex - 1) in mazeList:

                maze[vertex].append(vertex - 1)

            if (vertex + 1) in mazeList:

                maze[vertex].append(vertex + 1)

        maze = [sorted(item) for item in maze]
        
        return (maze, sourceVertex, destinationVertex)


def graphToFileMaze(filename, path):

    path = path.split('-')
    vertices = [int(index) for index in path]

    with open(filename, 'r') as f:

        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        firstLine = lines[0]
        firstLineList = firstLine.split()
        n = int(firstLineList[0])
        data = lines[1:]
        mazeString = ''.join(data)
        mazeList = list(mazeString)

    for vertex in vertices:

        if mazeString[vertex] not in ['O', 'I']:

            mazeList[vertex] = '*'

    outputMazeString = ''.join(mazeList)
    outputMazeList = [outputMazeString[i:i + n] for i in range(0, len(outputMazeString), n)]
    outputMazeList = list(map(lambda x : x + '\n', outputMazeList))

    outputMazeFile = filename.replace('.txt', '_out.txt')

    with open(outputMazeFile, 'w') as f:

        f.writelines(outputMazeList)

