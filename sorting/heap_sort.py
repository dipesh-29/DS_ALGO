def heapify(A,n,index):
    if A:
        largest = index
        left = 2*index + 1
        right = 2*index + 2
        print(index)
        print(left)
        exit(0)

        if left < n and A[left] > A[largest]:
            largest = left
        if right < n and A[right] > A[largest]:
            largest = right

        if largest != index:
            A[largest], A[index] = A[index], A[largest]
            heapify(A,n,largest)


def heap_sort(A):
    n = len(A)
    for ind in range(n-1,-1,-1):
        heapify(A, n-1, ind)

    for i in range(n-1, 0, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp

        heapify(A, i, 0)
    return A

A = [3,5,1,4,7,4,3,8,9,4,2,6]
result = heap_sort(A)
print(result)
