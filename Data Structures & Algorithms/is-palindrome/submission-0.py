import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = re.sub(r'[^a-zA-Z0-9]', '',s)
        clean_text = d.lower()
        n = len(clean_text)
        l=0
        r=n-1

        while l<r:
            print(clean_text[l],clean_text[r])
            if clean_text[l]!=clean_text[r]:
                return False
            else:
                l+=1
                r-=1
        return True