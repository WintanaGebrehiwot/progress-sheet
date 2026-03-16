class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count=0
        first,second=0,0
        while first<len(g) and second<len(s):
            if g[first]<=s[second]:
                count+=1
                first+=1
            second+=1

        return count

        