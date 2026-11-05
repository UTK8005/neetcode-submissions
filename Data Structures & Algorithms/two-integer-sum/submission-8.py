class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} 
        for index,value in enumerate(nums):
            if value in nums_dict:
                nums_dict[value].append(index)
            else:
                nums_dict[value]=[index]
        for value in nums_dict:
            if target-value in nums_dict:
                if value==target-value:
                    if len(nums_dict[value])>1:
                        return [nums_dict[value][0],nums_dict[value][1]]
                    else:
                        pass
                else:
                    return [nums_dict[value][0],nums_dict[target-value][0]]
            else:
                pass

