class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        new=[0]*len(s)
        for l,r,k in shifts:
            if k==1:
                new[l]+=1
                if r+1<len(s):
                    new[r+1]-=1
            else:
                new[l]-=1
                if r+1<len(s):
                    new[r+1]+=1
            
        for i in range(1,len(s)):
            new[i] += new[i-1] 
        
        result=[]
        shifted=0
        for i in range(len(new)):
            shifted = (ord(s[i]) - ord('a') + new[i]) % 26
            result.append(chr(shifted + ord('a')))

        return ''.join(result)

        