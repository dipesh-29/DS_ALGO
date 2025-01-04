def longest_repeating_subsequence(A):
    dp = [[0 for i in range(len(A)+1)] for x in range(len(A)+1)]
    for index in range(1,len(A)+1):
        for ind in range(1,len(A)+1):
            if A[index-1] == A[ind-1] and index != ind:
                dp[index][ind] = dp[index-1][ind-1] + 1
            else:
                dp[index][ind] = max(dp[index-1][ind], dp[index][ind-1])
    return dp[-1][-1]


if __name__=="__main__":
    str1 = "AABCEBCEDD"
    result = longest_repeating_subsequence(str1)
    print(result)
