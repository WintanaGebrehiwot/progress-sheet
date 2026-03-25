class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff=0
        total=0

        for i in range(len(nums)):
            total+=nums[i]

            min_diff=abs(total-target)
            left=0
            while total>min_diff:
                total-=nums[left]
                left+=1

                min_diff=min(min_diff,total)

        return min_diff
                


        