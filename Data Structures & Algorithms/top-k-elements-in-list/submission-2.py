class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for element in nums:
            frequency[element]=frequency.get(element,0)+1
        return sorted(frequency,key=frequency.get,reverse=True)[:k]
        