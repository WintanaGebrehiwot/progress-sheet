class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        i = 1
        k = 1  

        while i < n:
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
            i += 1

        for j in range(k, n):
            nums[j] = "_"

        return k
        