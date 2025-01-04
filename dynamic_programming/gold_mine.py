'''
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect.

Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12
{(1,0)->(2,1)->(1,2)}
'''

# RECURSIVE NOT WORKING
def gold_mine_recursive(i,j,A):
    if i >= len(A) or j >= len(A[0]):
        return 0
    if j == 0 :
        return A[i][j]
    if i == 0 :
        return A[i][j] + max(gold_mine_recursive(i,j+1,A), gold_mine_recursive(i+1,j+1,A))
    return A[i][j] + max(gold_mine_recursive(i-1,j+1,A), gold_mine_recursive(i,j+1,A), gold_mine_recursive(i+1,j+1,A))


def gold_mine_dp(mine):
    rows = len(mine)
    cols = len(mine[0])
    dp = [[0 for _ in range(rows)] for _ in range(cols)]

    for r in range(rows):
        dp[r][0] = mine[r][0]

    for c in range(1,cols):
        for r in range(rows):
            if r == 0 :
                dp[r][c] = mine[r][c] + max(dp[r][c-1], dp[r+1][c-1])
            elif r == rows-1 :
                dp[r][c] = mine[r][c] + max(dp[r][c-1], dp[r-1][c-1])
            else:
                dp[r][c] = mine[r][c] + max(dp[r-1][c-1], dp[r][c-1], dp[r+1][c-1])
    max_gold = 0
    print(dp)
    for r in range(rows):
        if max_gold < dp[r][-1]:
            max_gold = dp[r][-1]
    return max_gold


if __name__=="__main__":
    A = [[1,3,3],[2,1,4],[0,6,4]]
    for r in range
    result = gold_mine_recursive(0,0,A)

    #A = [[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]
    #result = gold_mine_dp(A)
    print(result)
