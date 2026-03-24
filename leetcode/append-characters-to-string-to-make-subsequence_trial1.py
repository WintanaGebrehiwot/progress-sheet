class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        first,second=0,0
        new=[]
        while first<len(s) and second<len(t):
            if t[second] == s[first]:
                first+=1
                second+=1 
            else:
                first+=1

        new.extend(t[second:])
        return len(new)
                

        