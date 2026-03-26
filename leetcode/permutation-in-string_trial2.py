class Solution(object):
    from collections import Counter
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        target=Counter(s1)
        window=Counter(s2[:len(s1)])

        left=0
        for right in range (len(s1),len(s2)):
            
            if window==target:
                return True

            window[s2[right]]+=1
            window[s2[left]]-=1
            if window[s2[left]]==0:
                del window[s2[left]]
            left+=1
            
        if window==target:
                return True

        return False

               



        