class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = s.strip()
        for i in s:
            if(ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122):
                pass
            else:
                s = s.replace(i,"")
        l = 0
        r = len(s) - 1
        while(l < r):
            if(s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return False
        return True
