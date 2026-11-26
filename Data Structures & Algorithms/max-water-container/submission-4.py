class Solution:
    def maxArea(self, h: List[int]) -> int:
        i=0
        j=len(h)-1
        mx=0
        while i<j:
            mx=max(mx,(j-i)*min(h[j],h[i]))
            if h[i]<=h[j]:
                    i+=1
            else:
                    j-=1

        
        
        return mx

        