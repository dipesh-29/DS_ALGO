'''
Append K Integers With Minimal Sum
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.

Example :
Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
'''


#method2 Optimal solution
def minimalKSum(nums,k)
    k_sum = int(k*(k+1)/2)
    remaining_nums = 0
    for n in nums:
        if n >= 1 and n <= k :
            k_sum = k_sum - n
            remaining_nums += 1
    print(remaining_nums)
    x = k+1
    while remaining_nums:
        if x not in nums:
            remaining_nums -= 1
            k_sum = k_sum + x
        x += 1
    return k_sum



if __name__=="__main__":
    nums = [53,41,90,33,84,26,50,32,63,47,66,43,29,88,71,28,83]
    k = 76
    minimalKSum(nums,2)
