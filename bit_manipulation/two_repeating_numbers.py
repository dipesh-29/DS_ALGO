'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

'''

def singleNumber(self, nums: List[int]) -> List[int]:
        temp = 0
        for index in range(len(nums)):
            temp ^= nums[index]

        #Now find the least significant digit which is 1.
        j = 1
        while not temp & j:
            j = j << 1

        x = 0
        y = 0
        for n in nums :
            if n & j :
                x = x ^ n
            else:
                y = y ^ n
        return [x,y]
