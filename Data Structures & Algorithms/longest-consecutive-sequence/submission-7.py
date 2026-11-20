class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for i in s:
            if i-1 in s:
                continue
            x=1
            while i+1 in s:
                i+=1
                x+=1
            ans=max(ans,x)
        
        return ans
        
        