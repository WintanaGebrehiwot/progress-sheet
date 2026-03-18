class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        new={}
        for i in range(len(s)):
            new[s[i]]=new.get(s[i],0)+1

        result=[]    

        s1=sorted(new.items(), key=lambda item: item[1], reverse=True)
        result = []

        for char, freq in s1:
            result.append(char * freq)

        return ''.join(result)

      


        