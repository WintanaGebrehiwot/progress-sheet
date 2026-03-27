class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        rotated = nums[-k:] + nums[:-k]

        for i in range(n):
            nums[i] = rotated[i]

        return nums 