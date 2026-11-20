class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        seen=defaultdict(set)
        for i in range(n):
            s2=defaultdict(set)
            for j in range(i+1,n):
                x=nums[i]+nums[j]
                if -x in seen:
                    ans.add(tuple(sorted([nums[i],nums[j],-x]) ) )
                s2[nums[j]].add(j)
            seen[nums[i]].add(i)
        
        return list(ans)
        