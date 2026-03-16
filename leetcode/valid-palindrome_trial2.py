class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = "".join([ch for ch in s if ch.isalnum()]).lower()

        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False  # not a palindrome
            left += 1
            right -= 1

        return True 

        
        