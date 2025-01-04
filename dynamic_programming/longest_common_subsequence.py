def longest_common_subsequence_recursion(A,B,i,j):
    if i == len(A) or j == len(B):
        return 0
    elif(A[i] == B[j]):
        return 1 + longest_common_subsequence(A,B,i+1,j+1)
    else:
        return max(longest_common_subsequence(A,B,i+1,j), longest_common_subsequence(A,B,i,j+1))


def longest_common_subsequence(A,B):
    dp = [[0 for i in range(len(A)+1)] for x in range(len(B)+1)]
    for index in range(1,len(A)+1):
        for ind in range(1,len(B)+1):
            if A[index-1] == B[ind-1] :
                dp[index][ind] = dp[index-1][ind-1] + 1
            else:
                dp[index][ind] = max(dp[index-1][ind], dp[index][ind-1])
    return dp[-1][-1]


if __name__=="__main__":
    str1 = "ABDFAKSGYDH"
    str2 = "ABDKKHSAHKJ"

    result = longest_common_subsequence(str1, str2)
    print(result)
