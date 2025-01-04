import heapq

'''
heapq funtions : By default min heap is created.
1. heapq.heappush(heap_list, element)
2. heapq.heappop(heap_list)
3. heapq.heapify(heap_list)
4. heapq.heappushpop(heap_list, element) -> first push element then pop min element
5. heapq.heapreplace(heap_list, element) -> first pop smallest element and then insert new element.
6. heapq.nsmallest(n, heap_list)
7. heapq.nlargest(n, heap_list)

'''




if __name__=="__main__":
    nums = [5,3,1,4,7,2,8,5,9,6]
    heap = []
    for index in range(len(nums)):
        heapq.heappush(heap, nums[index])
    print(nums)
    print(heap)
    heapq.heapify(heap)
    print(heap)
    #   print(heapq.heappop(heap))
    heap.remove(2)
    print(heap)
    heapq.heapify(heap)
    print(heap)
