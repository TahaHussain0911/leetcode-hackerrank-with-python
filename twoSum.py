class Solution:
    def twoSum(self,nums,target):
        seen = {}
        for index,num in enumerate(nums):
            print(seen,'seen')
            difference=target - num
            if difference in seen:
                return [seen[difference],index]
            seen[num]=index


solution=Solution()
result=solution.twoSum([2,7,11,15],9)
print(result)