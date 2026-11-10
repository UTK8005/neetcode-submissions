class Solution:
    def isPalindrome(self, string: str) -> bool:
        cleaned_text = "".join(char for char in string if char.isalnum()).lower()
        left = 0
        right = len(cleaned_text)-1
        while left<right:
          if cleaned_text[left]!=cleaned_text[right]:
              return False
          left=left+1
          right=right-1
        return True
        