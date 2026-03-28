class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        for row in nums:
            row.sort()
        
        score = 0
        cols = len(nums[0])
        
        for c in range(cols):
            max_val = 0
            
            for r in range(len(nums)):
                max_val = max(max_val, nums[r][c])
            
            score += max_val
        
        return score
        