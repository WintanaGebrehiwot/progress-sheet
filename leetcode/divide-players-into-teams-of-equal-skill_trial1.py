class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        left=1
        right=len(skill)-2
        add=skill[0]+skill[len(skill)-1]
        chemistry=skill[0]*skill[len(skill)-1]

        while left<right:
            if skill[left]+skill[right]!= add:
                return -1
            else:
                chemistry+=skill[left]*skill[right]
                left+=1
                right-=1

        return chemistry
