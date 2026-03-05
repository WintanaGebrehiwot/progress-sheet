class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_num=0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_num = max(max_num, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_num

        