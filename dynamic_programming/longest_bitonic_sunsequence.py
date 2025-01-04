def longest_bitonic_subsequence(A):
    lcs = [1] * len(A)
    lcsr = [1] * len(A)
    bitonic = [0] * len(A)
    for index in range(1,len(A)):
        for ind in range(0,index):
            if A[index] > A[ind] and lcs[index] < lcs[ind] + 1 :
                lcs[index] = lcs[ind] + 1


    for index in range(len(A)-2, -1, -1):
        for ind in range(len(A)-1, index, -1):
            if A[index] > A[ind] and lcsr[index] < lcsr[ind] + 1 :
                lcsr[index] = lcsr[ind] + 1


    for index in range(len(A)):
        bitonic[index] = lcs[index] + lcsr[index] - 1

    return max(bitonic)


if __name__=="__main__":
    A = [2,4,2,12,25,22,4,1]
    result = longest_bitonic_subsequence(A)
    print(result)
