def longest_decresing_subsequence(A):
    result = [1] * len(A)
    for index in range(1,len(A)):
        for ind in range(0,index):
            if A[index] < a[ind] :
                if result[index] < result[ind] + 1 :
                    result[index] = result[ind] + 1
    return max(result)


if __name__=="__main__":
    a = [2,4,2,12,25,22,4,1]
    result = longest_decresing_subsequence(a)
    print(result)
