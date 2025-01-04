'''
# Kaden's Algorithm
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum.

eg :
[-2,-3,4,-1,-2,1,5,-3] sum -> 7 By Considering subarray [4,-1,-2,1,5]
'''

def max_sum_contigeous_subarray(A):
    dp = [0 for _ in range(len(A))]
    dp[0] = A[0]
    for index in range(1,len(A)):
        dp[index] = max(dp[index-1] + A[index], A[index])
    return max(dp)


if __name__ == '__main__':
    #A = [-2,-3,4,-1,-2,1,5,-3]
    #A = [-2,11,-4,13,-5,2]
    A = [1,-3,4,-2,-1,6]
    result = max_sum_contigeous_subarray(A)
    print(result)
