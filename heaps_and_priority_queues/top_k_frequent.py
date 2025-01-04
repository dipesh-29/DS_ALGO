'''
Top K Frequent Elements:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example :
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''
class Solution:
    def topKFrequent(self, nums, k):
        def heapify(A,size,index):
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < size and A[left][1] > A[largest][1]:
                largest = left
            if right < size and A[right][1] > A[largest][1]:
                largest = right
            if largest != index :
                A[largest],A[index] = A[index],A[largest]
                heapify(A,size,largest)
            return A


        def deletion(A):
            if A:
                deleted_item = A[0]
                size = len(A)-1
                A[0],A[size] = A[size],A[0]
                size = size-1
                A = heapify(A,size+1,0)
                return A[:-1] , deleted_item

        hash_map = {}
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n,0)

        A = []
        for key,value in hash_map.items():
            A.append([key,value])

        for index in range(len(A)-1,-1,-1):
            A = heapify(A,len(A),index)

        result = []
        for index in range(k):
            A , deleted_item = deletion(A)
            result.append(deleted_item[0])
        return result


    def topKFrequent_optimized(self, nums, k):
        #Method2 :
        #Use Bucket Sort :
        hash_map = {}
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n,0)

        bucket = [[] for _ in range(len(nums)+1)]
        for key,value in hash_map.items():
            bucket[value].append(key)

        result = []
        for index in range(len(bucket)-1,0,-1):
            if bucket[index]:
                for i in bucket[index]:
                    result.append(i)
                    k -= 1
                    if k == 0:
                        return result


if __name__=="__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    s = Solution()
    result = s.topKFrequent(nums,k)
    print(result)
    result = s.topKFrequent_optimized(nums,k)
    print(result)
'''
1st Runing Complexity : O(n) + O(n) + O(klogn) = O(klogn)
2nd Runing Complexity : O(n)
'''
