class Solution(object):
    from collections import Counter
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = Counter(s)
        required = n // 4
        
        if all(count[c] == required for c in "QWER"):
            return 0
        
        left = 0
        result = n
        
        for right in range(n):
            count[s[right]] -= 1
            
            while left < n and all(count[c] <= required for c in "QWER"):
                result = min(result, right - left + 1)
                count[s[left]] += 1
                left += 1
        
        return result

        