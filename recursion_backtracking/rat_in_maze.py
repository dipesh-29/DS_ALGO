def rat_in_maze(maze,i,j,n,path_maze):
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    if maze[i][j] == 0 :
        return False
    if i == n-1 and j == n-1:
        path_maze[i][j] = 1
        return True
    if maze[i][j] == 1 :
        path_maze[i][j] = 1

    rat_in_maze(maze, i+1, j, n, path_maze)
    rat_in_maze(maze, i, j+1, n, path_maze)


def solveMaze(maze, n):
    path_maze = [[0 for _ in range(n)] for _ in range(n)]

    rat_in_maze(maze,0,0,n,path_maze)

    print("Maze : ")

    for index in range(n):
        print(maze[index])

    print("Rat Path : ")

    for index in range(n):
        print(path_maze[index])



if __name__ == "__main__":
    # Initialising the maze
    n = 4
    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]

    solveMaze(maze, n)
