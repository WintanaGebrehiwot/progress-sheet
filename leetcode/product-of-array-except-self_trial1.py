class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_product=[1]*len(nums)
        accumulator=1

        for i in range(len(nums)):
            prefix_product[i]=accumulator
            accumulator*= nums[i]

        accumulator2=1
        for i in range(len(nums)-1,-1,-1):
            prefix_product[i]*=accumulator2
            accumulator2*= nums[i]

        return prefix_product
        