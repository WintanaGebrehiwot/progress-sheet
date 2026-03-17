class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n = len(fruits)
        window = {}
        left = 0
        ans = 0

        for right in range(n):
            window[fruits[right]] = window.get(fruits[right], 0) + 1

            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans
        