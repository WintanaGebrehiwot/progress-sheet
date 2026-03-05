class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        second = len(numbers) - 1

        while first < second:
            s = numbers[first] + numbers[second]

            if s == target:
                return [first + 1, second + 1]
            elif s < target:
                first += 1
            else:
                second -= 1
        