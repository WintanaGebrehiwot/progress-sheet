class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        nums = [0] * n

        for l, r, k in bookings:
            nums[l - 1] += k
            if r < n:
                nums[r] -= k

        for i in range(1, n):
            nums[i] += nums[i - 1]

        return nums

        