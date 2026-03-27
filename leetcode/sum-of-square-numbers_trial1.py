class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(c ** 0.5)

        while left <= right:
            curr = left**2 + right**2
            if curr == c:
                return True
            elif curr < c:
                left += 1
            else:
                right -= 1

        return False
        