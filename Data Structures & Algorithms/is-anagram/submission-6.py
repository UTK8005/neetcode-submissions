class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert them to lists
        # then get a count of each
        # store it in a dictionary 
        # compare the two
        if len(list(s))==len(list(t)):
            char_count_s = {}
            char_count_t = {}
            for i in s:
                if i not in char_count_s:
                    char_count_s[i]=1
                else :
                    char_count_s[i]+=1
            
            for i in t:
                if i not in char_count_t:
                    char_count_t[i]=1
                else:
                    char_count_t[i]+=1
            return char_count_s==char_count_t
        else:
            return False
        