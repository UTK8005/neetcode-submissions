class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_duplicate = False
        count_nums={}
        for num in nums:
            if num not in count_nums:
                count_nums[num]=1
            else:
                count_nums[num]+=1
                is_duplicate = True
                return is_duplicate
        return is_duplicate

        