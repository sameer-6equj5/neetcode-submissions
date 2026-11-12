class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        delim='*'
        for i in strs:
            res+=str(len(i))+'*' + i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        x=[]
        j=0
        n=len(s)
        while j<n:
            len_s=''
            while s[j]!='*':
                len_s+=s[j]
                j+=1

            len_s=int(len_s)
            j+=1 
            x.append(s[j:j+len_s])
            j=j+len_s



            

        return x

