class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        n=len(nums)
        freq=[[] for i in range(n+1) ]
        d=Counter(nums)

        for i in d:
            f=d[i]
            freq[f].append(i)
        
        ans=[]
        j=-1
        while -j<=n and len(ans)<k:
            if freq[j]:
                ans.extend(freq[j])
            
            j-=1
        
        return ans

        
        


            

        