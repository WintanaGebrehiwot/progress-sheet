class Solution(object):
    from collections import defaultdict
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        left = 0
        pairs = 0
        result = 0

        for right in range(len(nums)):
            # Add nums[right]
            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            # Shrink window if we have enough pairs
            while pairs >= k:
                result += len(nums) - right

                # Remove nums[left]
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return result

            


        