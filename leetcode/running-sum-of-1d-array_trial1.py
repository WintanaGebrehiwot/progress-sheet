class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[0]*len(nums)
        for i in range(len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        return prefix

        