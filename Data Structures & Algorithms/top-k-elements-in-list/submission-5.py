class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d=Counter(nums)
        n=len(nums)
        ans=[[] for i in range(n+1)]
        for i in d:   
            freq=d[i]
            ans[freq].append(i)

        j=-1
        x=[]
        while -j<=n:
            x.extend(ans[j])
            if len(x)>=k:
                return x[:k]
            j-=1
