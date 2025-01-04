'''
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the integers in the subsequence are sorted in increasing order.
For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10
'''

def increasing_subsequence_with_max_sum(A):
    dp = [0] * len(A)
    dp[0] = A[0]
    for index in range(1,len(A)):
        for j in range(0,index):
            if A[index] > A[j]:
                dp[index] = max(dp[index], dp[j]+A[index])
    return max(dp)





if __name__ == '__main__':
    #A = [1, 101, 2, 3, 100, 4, 5]
    #A = [3, 4, 5, 10]
    A = [10, 5, 4, 3]
    result = increasing_subsequence_with_max_sum(A)
    print(result)
