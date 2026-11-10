class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            x=tuple(sorted(i))
            if x in d:
                d[x].append(i)
            else:
                d[x]=[i]
        
        ans=[]
        for k in d:
            ans.append(d[k]) 

        return ans       