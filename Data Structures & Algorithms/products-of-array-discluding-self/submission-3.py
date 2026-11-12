class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        res=[]
        for i in nums:
            res.append(pre)
            pre*=i

        pos=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=pos
            pos*=nums[i]


        return res
        