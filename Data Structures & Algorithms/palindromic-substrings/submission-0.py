class Solution:

    def countpndm(self,s, l, r):
        cnt = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            cnt +=1
            l -=1
            r += 1
        return cnt
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            
            cnt += self.countpndm(s, i,i)
            cnt += self.countpndm(s, i, i+1 )

        return cnt


        
