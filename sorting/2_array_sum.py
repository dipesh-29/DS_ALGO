'''
Given an array give the pair of element whose sum is equal to K.
'''

def sum_k_pair(A,k):
    result = []
    map = {}
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]+A[j] == k :
                if A[i] not in map:
                    result.append([A[i],A[j]])
                    map[A[i]] = A[j]
    return result


if __name__=='__main__':
    A = [-4,-1,-1,0,1,2]
    k = -2
    result = sum_k_pair(A, k)
    print(result)
