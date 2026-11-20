class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for i in nums:
            x=1
            n=i-1
            while n in s:
                s.discard(n)
                n-=1
                x+=1
                
            
            n=i+1
            while n in s:
                s.discard(n)
                n+=1
                x+=1
            ans=max(ans,x)
        
        return ans
            

        