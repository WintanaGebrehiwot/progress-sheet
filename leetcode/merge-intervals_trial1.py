class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        new=[intervals[0]]
        for i in range(1,len(intervals)):
            if new[-1][1] >= intervals[i][0]:
                new[-1][1] = max(new[-1][1], intervals[i][1])
            else:
                new.append(intervals[i])
            
            
        return new

        