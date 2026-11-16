class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        ans=1
        last=nums[0]
        temp=1
        #print(nums,last)
        for i in nums:
            if i==last+1:
                temp+=1
            else:
                ans=max(ans,temp)
                temp=1

            last=i
        
        return max(ans,temp)
                

        