class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        psum=1
        ssum=1
        p=[]
        s=[]
        j=-1
        for i in nums:
            psum*=i
            p.append(psum)
            ssum*=nums[j]
            s.append(ssum)
            j-=1

        s=s[::-1]
        ans=[]
        j=0
        n=len(nums)
        #print(p)
        #print(s)
        #print(nums)
        while j<n:
            prev=j-1
            nxt=j+1
            res=1
            if prev>=0:
                res*=p[prev]
            if nxt<n:
                res*=s[nxt]
            
            ans.append(res)
            j+=1


        return ans
            
        