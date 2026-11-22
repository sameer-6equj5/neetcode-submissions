class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len=len(nums)
        ans=set()
        for ind,n in enumerate(nums):
            left=0
            right=nums_len-1
            while left<right:
                x=nums[left]+nums[right]+n
                if x==0:
                    if ind!=left and ind!=right:
                        ans.add(tuple(sorted([n,nums[left],nums[right]])))

                    left+=1
                    right-=1
                elif x>0:
                    right-=1
                else:
                    left+=1
            
        return list(ans)

            
        