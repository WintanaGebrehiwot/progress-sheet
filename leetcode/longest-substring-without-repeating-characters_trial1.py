class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=0
        new={}
        max_len=0

        for right in range(len(s)):
            new[s[right]] = new.get(s[right], 0) + 1

            while left<len(s) and len(new)!=(right-left+1):
                new[s[left]]-=1
                if new[s[left]]==0:
                    del new[s[left]]

                left+=1

            max_len=max(max_len,right-left+1)    

        return max_len 

        