class Solution:
    def maxArea(self, h: List[int]) -> int:
        i=0
        j=len(h)-1
        mx=0
        while i<j:
            mx=max(mx,(j-i)*min(h[j],h[i]))
            if i+1<j and j-1>i:
                if h[i]<h[j]:
                    i+=1
                else:
                    j-=1
            else:
                i+=1
                j-=1
        
        
        return mx

        