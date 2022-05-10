import test 

if __name__ == '__main__':

    # Floyd Warshall input
    graphFiles = ["g5.txt", "g10.txt", "g100.txt", "g200.txt", "g500.txt", "g1000.txt"]
    graphFiles = list(map(lambda filename: "Lab5_files/" + filename, graphFiles))

    # BFS input
    bfsInput = {"b10.txt" : [(3, 9), (8, 9)], "b20.txt" : [(10, 11), (5, 7)], "b50.txt" : [(5, 7), (7, 9)], "b100.txt" : [(6, 9), (99, 100)]}
    bfsInput = {"Lab5_files/" + key : value for key, value in bfsInput.items()}

    # Maze input
    mazeInput = ["m5x5.txt", "m15x15.txt"]
    mazeInput = list(map(lambda filename: "Lab5_files/" + filename, mazeInput))

    #test.runTestFloydWarshall(graphFiles)

    #test.runTestBFS(bfsInput)

    test.runTestMaze(mazeInput)