class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = defaultdict(int)
        total = 0
        left = 0
        max_sum = 0

        for right in range(len(nums)):
            window[nums[right]] += 1
            total += nums[right]

            while window[nums[right]] > 1:
                window[nums[left]] -= 1
                total -= nums[left]

                if window[nums[left]] == 0:
                    del window[nums[left]]

                left += 1

            max_sum = max(max_sum, total)

        return max_sum
        