class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum=float(0)
        max_value=float('-inf')

        for i in range(k):
            window_sum+=nums[i]

        max_value=window_sum
        left=0
        for right in range(k,len(nums)):
                window_sum+=nums[right]
                window_sum-=nums[left]

                max_value=max(max_value,window_sum)

                left+=1

        return max_value/k

        

        