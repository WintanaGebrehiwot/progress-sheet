class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        new=[]
        score1 = sorted(score, reverse=True)
        for i in score:
            if i == score1[0]:
                new.append("Gold Medal")
            elif i == score1[1]:
                new.append("Silver Medal")
            elif i == score1[2]:
                new.append("Bronze Medal")
            else:
                index = score1.index(i) + 1
                new.append(str(index))

        return new


        