class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        vowel = ['a', 'e', 'i', 'o', 'u']

        for i in range(k):
            if s[i] in vowel:
                count += 1

        max_count = count
        left = 0

        for right in range(k, len(s)):
            if s[right] in vowel:
                count += 1
            if s[left] in vowel:
                count -= 1
            left += 1
            max_count = max(max_count, count)

        return max_count
            
            
        