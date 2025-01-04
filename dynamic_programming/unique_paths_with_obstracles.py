'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

obstacleGrid =
[[0,0,0],
 [0,1,0],
 [0,0,0]]
output = 2
'''

def unique_paths_with_obstracles_recursion(i, j, obstacleGrid):
    if i == len(obstacleGrid) or j== len(obstacleGrid[0]):
        return 0
    if obstacleGrid[i][j] :
        return 0
    if i == len(obstacleGrid)-1  and j == len(obstacleGrid[0])-1:
        return 1

    return unique_paths_with_obstracles_recursion(i+1, j, obstacleGrid) + unique_paths_with_obstracles_recursion(i, j+1, obstacleGrid)


def unique_paths_with_obstracles_dp(obstacleGrid):
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    if obstacleGrid[0][0]:
        return 0

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    #Initializing the table :
    flag = False
    for c in range(cols):
        if flag :
            dp[0][c] = 0
        elif obstacleGrid[0][c] == 1:
            flag = True
            dp[0][c] = 0
        else:
            dp[0][c] = 1


    flag = False
    for r in range(rows):
        if flag :
            dp[r][0] = 0
        elif obstacleGrid[r][0] == 1:
            flag = True
            dp[r][0] = 0
        else:
            dp[r][0] = 1

    for i in range(1, rows) :
        for j in range(1, cols):
            if obstacleGrid[i][j] :
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


'''
THIS IS THE BEST SOLUTION....
'''

def unique_paths_with_obstracles_dp_nice_soluion(obstacleGrid) :
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0
    dp = [[0 for i in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

if __name__=="__main__":
    A = [[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]]
    #A = [[0,0],[1,1],[0,0]]
    result = unique_paths_with_obstracles_recursion(0,0,A)
    result = unique_paths_with_obstracles_dp(A)
    #result = unique_paths_with_obstracles_dp_nice_soluion(A)
    print(result)
