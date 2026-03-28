class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        nums = sorted(set(nums))

        left = 0
        max_window = 0

        for right in range(len(nums)):
            
            while nums[right] - nums[left] > n - 1:
                left += 1

            max_window = max(max_window, right - left + 1)

        return n - max_window

        