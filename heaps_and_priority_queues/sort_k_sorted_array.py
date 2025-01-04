'''
Sort a k-sorted array

Given a k-sorted array that is almost sorted such that each if the n elements may be misplaced by no more than k positions from the correct soretd order. Find the space and time efficient algorithm to sort the array.

Input:

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2

Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

import heapq

def sort_k_sorted_array(nums,k):
    heap = []
    result = []
    for index in range(k+1):
        heapq.heappush(heap,nums[index])

    for index in range(k+1,len(nums)):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap,nums[index])

    while heap:
        result.append(heapq.heappop(heap))

    return result

if __name__ == '__main__':
    nums = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    result = sort_k_sorted_array(nums,k)
    print(result)
