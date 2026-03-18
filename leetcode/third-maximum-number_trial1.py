class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique= list(dict.fromkeys(nums))
        unique.sort(reverse=True)
        if len(unique)<3:
            return unique[0]
        else:
            return unique[2]
        