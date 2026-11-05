class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert them to lists
        # then get a count of each
        # store it in a dictionary 
        # compare the two
        def char_count_dict(string:str) -> dict:
            char_count_dict={}
            for i in string:
                char_count_dict[i]=char_count_dict.get(i,0)+1
            return char_count_dict

        if len(s)==len(t):
            return char_count_dict(s)==char_count_dict(t)
        else:
            return False
        