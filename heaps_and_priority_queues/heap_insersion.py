'''
Heaps and priority queues :
1. Heapify function : given an index of heap and size of heap, This function heapify the tree formed below the given index.
2. Heap Insersion : Insert an element into heap. Insersion done at the last of the heap. And then from there just check the inserted element with its parent to place it at proper position in heap.
    - insert element at the last of a heap.
    - increase size of heap by 1.
    - get the parent of the an element. check element with parent and swap if parent is smaller than child (max heap).
3. Delete element from heap : This algo deletes an element from heap. In heap root is always deleted.
    - Swap the root with last element in heap.
    - reduce the size of heap by 1.
    - run heapify function for index 0.
'''
import math

def heapify(A, size, index):
    largest = index
    left_child = 2*index+1
    right_child = 2*index+2

    if left_child < size and A[left_child] > A[largest] :
        largest = left_child

    if right_child < size and A[largest] < A[right_child] :
        largest = right_child

    if largest != index :
        #swap(A[larget],A[index])
        temp = A[largest]
        A[largest] = A[index]
        A[index] = temp
        heapify(A,size,largest)
    return A


def heap_insersion(A, element):
    A.append(element)
    size = len(A)
    index = size-1
    while index > 0 :
        parent = (index-1)/2
        if A[parent] < A[index]:
            A[parent],A[index] = A[index],A[parent]

            index = parent
        else:
            return A
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
    print(A)
    for index in range(len(A)-1, -1, -1):
        result = heapify(A,len(A), index)
    print("----- Heapified Array -----")
    print(result)
    print("----- Insert Element -----")
    result = heap_insersion(A, 65)
    print(result)
    print("----- Delete Element -----")
    result = heap_deletion(A)
    print(result)
