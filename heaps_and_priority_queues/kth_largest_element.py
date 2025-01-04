def heapify(A, size, index):
    largest = index
    left_child = 2*index+1
    right_child = 2*index+2

    if left_child <= size and A[left_child] > A[largest] :
        largest = left_child

    if right_child <= size and A[largest] < A[right_child] :
        largest = right_child

    if largest != index :
        #swap(A[larget],A[index])
        temp = A[largest]
        A[largest] = A[index]
        A[index] = temp
        heapify(A,size,largest)
    return A


def heap_deletion(A) :
    if A :
        size = len(A) - 1
        #Swap root element with last element. Remember indexing starts from 1 so root is present on A[1] not A[0].
        temp = A[0]
        A[0] = A[size]
        A[size] = temp

        size = size-1

        A = heapify(A,size,0)
        return A[:-1]

if __name__=="__main__":
    A = [30,10,20,60,40,35,50,25,45]
    k = 5
    print(A)
    for index in range(len(A)-1, -1, -1):
        A = heapify(A, len(A)-1, index)
    print(A)

    for index in range(5):
        A = heap_deletion(A)
    print("Kth smallest element is : ")
    print(A)
    print(A[0])
