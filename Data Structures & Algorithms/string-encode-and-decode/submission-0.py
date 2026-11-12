class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        delimiter=chr(288)
        for i in strs:
            res+=delimiter+i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        x=s.split(chr(288))
        x.pop(0)
        return x

