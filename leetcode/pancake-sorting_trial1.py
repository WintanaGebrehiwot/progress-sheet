class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_indx = 0
        new = []

        for i in range(len(arr)-1, 0, -1):

            max_indx = 0
            for j in range(i+1):
                if arr[j] > arr[max_indx]:
                    max_indx = j

            if max_indx == i:
                continue

            if max_indx != 0:
                arr[:max_indx+1] = arr[:max_indx+1][::-1]
                new.append(max_indx+1)

            arr[:i+1] = arr[:i+1][::-1]
            new.append(i+1)

        return new
                

                
        