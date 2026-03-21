class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        count[0] = 1  
        
        current_odd = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                current_odd += 1

            if current_odd - k in count:
                result += count[current_odd - k]

            count[current_odd] += 1

        return result

        