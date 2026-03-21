class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        total=0
        window_sum=0
        n=len(cardPoints)

        for i in range(n-k):
            window_sum+=cardPoints[i]

        min_value=window_sum

        left=0
        for right in range(n-k, n):
            window_sum-=cardPoints[left]
            window_sum+=cardPoints[right]
            left+=1

            min_value=min(min_value,window_sum)

        for num in cardPoints:
            total+=num

        result=total-min_value
        return result



       