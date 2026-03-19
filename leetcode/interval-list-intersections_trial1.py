class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if firstList==[] or secondList==[]:
            return []

        first = 0
        second = 0
        thirdList = []

        while first < len(firstList) and second < len(secondList):
            s = max(firstList[first][0], secondList[second][0])
            t = min(firstList[first][1], secondList[second][1])

            if s <= t:
                thirdList.append([s, t])

            if firstList[first][1] <= secondList[second][1]:
                first += 1
            else:
                second += 1

        return thirdList

           
           
                


        