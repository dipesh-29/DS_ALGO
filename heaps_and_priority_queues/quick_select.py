'''
- Quick Select algorithm is used to find the Kth smallest or Kth largest element in an array.
- It uses partion function which is used in quick sort.
- find the partition
'''


def partition(A, left, right):
    pivot = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= pivot :
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i


def quick_select(A, left, right, k):
    p = partition(A, left, right)
    if p == len(A) - k:
        return A[p]
    if p > len(A) - k :
        return quick_select(A,left,p-1,k)
    if p < len(A) - k :
        return quick_select(A,p+1,right,k)

#A = [30,10,40,20,60,35,50,25,45]
A = [3,2,1,7,5,6,4]
k = 2
result = quick_select(A, 0, len(A)-1, k)
print(result)
