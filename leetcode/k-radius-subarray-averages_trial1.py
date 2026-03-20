class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        avgs = [-1] * n
        window_size = 2 * k + 1
        
        if window_size > n:
            return avgs 
        
        window_sum = sum(nums[:window_size])
        avgs[k] = window_sum // window_size  # first valid index is k
        
        for i in range(k + 1, n - k):
            window_sum = window_sum - nums[i - k - 1] + nums[i + k]
            avgs[i] = window_sum // window_size
        
        return avgs
        