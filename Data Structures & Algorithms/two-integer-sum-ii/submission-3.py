class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for index,num in enumerate(numbers):
            key=target-num
            if key in d:
                return [d[key]+1,index+1]
            else:
                d[num]=index
        
        return []
            


        