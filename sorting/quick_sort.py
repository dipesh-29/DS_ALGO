def partition(A, left, right):
    pivot = A[right]
    ind = left
    for i in range(left, right):
        if A[i] <= pivot :
            A[i], A[ind] = A[ind], A[i]
            ind += 1
    A[ind], A[right] = A[right], A[ind]
    return ind


def quick_sort(A, l, r):
    if len(A) == 1:
        return A
    if l < r :
        p = partition(A,l,r)
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r)
    return A

if __name__=="__main__":
    A = [3,5,1,4,7,4,3,8,9,4,2,6]

    result = quick_sort(A, 0, len(A)-1)
    print(result)
