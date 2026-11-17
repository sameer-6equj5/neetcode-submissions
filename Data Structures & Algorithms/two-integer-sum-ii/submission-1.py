class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index,num in enumerate(numbers):
            key=target-num
            if key<num:
                left=0
                right=index-1
            
            else:
                left=index+1
                right=len(numbers)-1
            
            while left<=right:
                mid=(left+right)//2
                if numbers[mid]==key:
                    return [min(mid+1,index+1),max(mid+1,index+1) ]
                elif numbers[mid]>key:
                    right=mid-1
                else:
                    left=mid+1


        