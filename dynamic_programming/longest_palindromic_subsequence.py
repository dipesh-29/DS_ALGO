def longest_palindromic_subsequence(A, B):
    dp = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]

    for index in range(1,len(A)+1):
        for ind in range(1,len(B)+1):
            if A[index-1] == B[ind-1]:
                dp[index][ind] = dp[index-1][ind-1] + 1
            else:
                dp[index][ind] = max(dp[index-1][ind] , dp[index][ind-1])

    return dp[-1][-1]

if __name__=="__main__":
    A = "ABDKDSNKDHBSAH"
    B = A[::-1]
    result = longest_palindromic_subsequence(A,B)
    print(result)
