class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        l = 0
        maxcount = 0
        res = 0
        win = {}

        for r in range(len(s)):
            win[s[r]] =win.get(s[r], 0) + 1
            maxcount = max(maxcount, win[s[r]])

            while (r - l + 1) - maxcount > k:
                win[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res

           

          


        