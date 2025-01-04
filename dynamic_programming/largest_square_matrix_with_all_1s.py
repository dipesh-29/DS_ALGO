'''
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

For example, consider the below binary matrix.

A = [
    [0,1,1,0,1],
    [1,1,0,1,0],
    [0,1,1,1,0],
    [1,1,1,1,0],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

max submatrix with all 1st is 3x3 matrix.
'''

def Largest_square_matrix_with_all_1s(A):
    rows = len(A)
    cols = len(A[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # Initialize the array
    dp[0] = A[0]
    for r in range(rows) :
        dp[r][0] = A[r][0]

    for r in range(1,rows):
        for c in range(1,cols):
            if A[r][c]:
                if A[r-1][c] and A[r][c-1] :
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = A[r][c]
            else:
                dp[r][c] = 0
    return max([max(x) for x in dp])


if __name__ == '__main__':
    A = [
        [0,1,1,0,1],
        [1,0,1,1,0],
        [0,1,1,1,0],
        [1,1,1,1,0],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]

    result = Largest_square_matrix_with_all_1s(A)
    print(result)
