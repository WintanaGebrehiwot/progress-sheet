class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n=len(piles)
        me=0
        for i in range(n-2,n//3-1,-2):
            me+=piles[i]

        return me
        