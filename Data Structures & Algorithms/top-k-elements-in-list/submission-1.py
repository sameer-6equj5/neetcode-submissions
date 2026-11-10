class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 
        d=Counter(nums)
        freq={}
        for i in d:
            f=d[i]
            if f in freq:
                freq[f].append(i)
            else:
                freq[f]=[i]
        
        x=sorted(freq.keys(),reverse=True)[:k]
        ans=[]
        #print(freq,x,k)
        for i in x:
            ans.extend(freq[i])
            if len(ans)>=k:
                return ans
        
        return ans
        
        