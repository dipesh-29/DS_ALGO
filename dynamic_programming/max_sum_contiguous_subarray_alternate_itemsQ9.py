'''
Maximum sum such that no two elements are adjacent

Given an Array of n items,return the contiguous subsequence with maximum sum. BUT THE CONDITION IS THAT YOU CAN NOT SELECT TWO CONSECUTIVE/CONTIGUOUS NUMBERS.

eg :
A = [-2,-3,4,-1,-2,1,5,-3]
o/p -> 7 by selecting [4,-2]

'''

def max_sum_contigeous_subarray(A):
    dp = [0 for _ in range(len(A))]
    dp[0] = A[0]
    dp[1] = max(dp[0],A[1])

    for index in range(2,len(A)):
        dp[index] = max(dp[index-2] + A[index], dp[index-1], A[index])
    return max(dp)


if __name__ == '__main__':
    #A = [-2,-3,4,-1,-2,1,5,-3]
    #A = [-2,11,-4,13,-5,2]
    A = [1,-3,4,-2,-1,6]
    #A = [1, 2, 9, 4, 5, 0, 4, 11, 6]
    result = max_sum_contigeous_subarray(A)
    print(result)
