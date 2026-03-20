class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        count=0
        for i in range(k):
            if blocks[i]=="W":
                count+=1
        min_count = count

        for i in range(k,len(blocks)):
            if blocks[i-k]=="W":
                count-=1
            if blocks[i]=="W":
                count+=1
            min_count = min(min_count,count)

        return min_count

        

        