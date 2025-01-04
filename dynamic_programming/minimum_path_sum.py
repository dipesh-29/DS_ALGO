'''
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

def minPathSum_recursive(i,j,grid):
    if i >= len(grid) or j >= len(grid[0]):
        return 100000
    if i == len(grid) - 1 and j == len(grid[0])-1 :
        return grid[i][j]

    right = minPathSum_recursive(i+1,j,grid)
    down = minPathSum_recursive(i,j+1,grid)
    return grid[i][j] + min(right, down)


def minPathSum_dp(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0 :
                dp[r][c] = grid[r][c]
            elif r == 0 :
                dp[r][c] = grid[r][c] + dp[r][c-1]
            elif c == 0 :
                dp[r][c] = grid[r][c] + dp[r-1][c]
            else:
                dp[r][c] = grid[r][c] + min(dp[r-1][c],dp[r][c-1])
    return dp[-1][-1]


if __name__=="__main__":
    A = [[1,3,1],[1,5,1],[4,2,1]]
    A = [[1,2,3],[4,5,6]]
    result = minPathSum_recursive(0,0,A)
    #result = minPathSum_dp(A)
    print(result)
