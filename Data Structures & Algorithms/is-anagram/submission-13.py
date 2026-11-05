class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert them to lists
        # then get a count of each
        # store it in a dictionary 
        # compare the two
        char_count={}
        if len(s) == len(t):
            for i in s:
                char_count[i]=char_count.get(i,0)+1
            for i in t:
                char_count[i]=char_count.get(i,0)-1
            for value in char_count.values():
                if value != 0:
                    return False
            return True
        else:
            return False
        