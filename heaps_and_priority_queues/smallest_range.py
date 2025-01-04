'''
Find the smallest range with at least one element from each of the given lists



Input:  4 sorted lists of variable length

[ 3, 6, 8, 10, 15 ]
[ 1, 5, 12 ]
[ 4, 8, 15, 16 ]
[ 2, 6 ]

Output:

The minimum range is 4-6
'''
import heapq

def smallest_range(lists):
    m = len(lists)
    heap = []
    max_element = -1
    min_range = 100000000

    # Maintain Heap of M element. One from each list.
    for index in range(m):
        if lists[index]:
            if max_element < lists[index][0]:
                max_element = lists[index][0]
            heapq.heappush(heap,[lists[index][0],index])
        else:
            return -1

    while heap :
        val, index = heapq.heappop(heap)
        lists[index].pop(0)
        if min_range > max_element - val:
            min_range = max_element - val

        if lists[index]:
            if max_element < lists[index][0]:
                max_element = lists[index][0]
            heapq.heappush(heap,[lists[index][0],index])
        else:
            return min_range+1
    return min_range+1



if __name__ == '__main__':
    lists = [[ 3, 6, 8, 10, 15 ], [ 1, 5, 12 ], [ 4, 8, 15, 16 ], [ 2, 7 ]]
    result = smallest_range(lists)
    print(result)
