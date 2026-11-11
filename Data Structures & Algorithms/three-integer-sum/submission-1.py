from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums) # sort it
        result=[]
        for index in range(len(nums)): 
            num=nums[index]
            left=index+1
            right=len(nums)-1
            while left<right:
                total= num+nums[left]+nums[right]
                if total==0:
                    result.append([num,nums[left],nums[right]])
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                elif total>0:
                    right-=1
        collection= list(set(tuple(sorted(i)) for i in result))
        return collection
            
            
            






        