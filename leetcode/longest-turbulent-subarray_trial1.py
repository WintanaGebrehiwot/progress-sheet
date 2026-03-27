class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 2:
            return n

        left = 0
        max_len = 1

        def cmp(a, b):
            if a > b:
                return -1
            elif a < b:
                return 1
            else:
                return 0

        for right in range(1, n):
            c = cmp(arr[right-1], arr[right])

            if c == 0:
                left = right  
            elif right == n-1 or c * cmp(arr[right], arr[right+1]) != -1:
                max_len = max(max_len, right - left + 1)
                left = right 

        return max_len
           

        