'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
'''


def unique_paths_recursion(m, n):
    if m == 1 or n == 1 :
        return 1

    return unique_paths_recursion(m-1, n) + unique_paths_recursion(m, n-1)


def unique_paths_dp(m, n):
    dp = [[0 for i in range(n)] for j in range(m)]
    #Initialization
    for index in range(m):
        for index1 in range(n):
            if index == 0 or index1 == 0:
                dp[index][index1] = 1

    for index in range(1,m):
        for index1 in range(1,n):
            dp[index][index1] = dp[index-1][index1] + dp[index][index1-1]

    return dp[-1][-1]

if __name__=="__main__":
    m = 3
    n = 4
    result = unique_paths_recursion(m,n)
    result = unique_paths_dp(m,n)
    print(result)
