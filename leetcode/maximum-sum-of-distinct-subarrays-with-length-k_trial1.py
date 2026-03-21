class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            count[nums[right]] += 1

            if right - left + 1 > k:
                count[nums[left]] -= 1
                current_sum -= nums[left]
                if count[nums[left]] == 0:
                    del count[nums[left]] 
                left += 1

            if right - left + 1 == k:
                if len(count) == k: 
                    max_sum = max(max_sum, current_sum)

        return max_sum

        