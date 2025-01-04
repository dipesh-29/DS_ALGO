def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Algo : 1
        Build Min heap
        Build Max heap
        run a loop for n/2 times :
        Delete 1 element from min heap and 1 elemnet from max heap. and save the pairwise in result.

        ALgo : 2
        Build min and max heap like we do for finding median for streaming of elements
        Then delete one element from min heap and 1 element from max heap. And store pairwise result.

        Algo : 3
        run quick select algo where k = n/2.
        Then run one pointer from left and one from right and form the pairs.
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
            if p == k:
                return A
            if p > k :
                return quick_select(A,left,p-1,k)
            if p < k :
                return quick_select(A,p+1,right,k)

        nums = quick_select(nums,0,len(nums)-1,int(len(nums)/2))

        print(nums)

        left = 0
        right = len(nums)-1
        result = []
        while left <= right :
            if left == right:
                result.append(nums[left])
                nums = result
                break
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right -= 1
        nums = result
        return nums
