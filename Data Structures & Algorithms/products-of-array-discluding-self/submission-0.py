class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        x=1
        zero=0
        for n in nums:
            if n==0:
                zero+=1
            else:
                x*=n
        
        if zero>1:
            return [0 for i in nums]
        
        ans=[]
        for n in nums:
            if n==0:
                ans.append(int(x))
            elif zero==0:
                ans.append(int(x/n))
            else:
                ans.append(0)
        
        return ans
        