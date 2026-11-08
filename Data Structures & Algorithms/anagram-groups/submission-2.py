from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            char_count = {}
            for i in string:
                char_count[i] = char_count.get(i, 0) + 1
        
            result[tuple(sorted(char_count.items()))].append(string)
        
        return list(result.values())

        

        