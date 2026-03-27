class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_map = {0: -1} 
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]

            if k != 0:
                rem = prefix % k
            else:
                rem = prefix 

            if rem in remainder_map:
                if i - remainder_map[rem] >= 2:
                    return True
            else:
                remainder_map[rem] = i

        return False

        