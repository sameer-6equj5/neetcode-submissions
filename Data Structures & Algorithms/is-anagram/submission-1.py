class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for i in t:
            if i not in d:
                return False
            else:
                d[i]-=1
                if d[i]==0:
                    del d[i]
        
        return not d
        

        