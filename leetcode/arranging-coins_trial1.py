class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return n

        left,right=0,int(n)

        while left<=right:
            k=(left+right)//2
            if k*(k+1)//2 <=n:
                left=k+1
            elif k*(k+1)//2 > n:
                right= k-1

        return right
        