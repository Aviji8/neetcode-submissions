class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}
        if len(s) != len(t):
            return False
        for char in s:
            set_s[char] = set_s.get(char,0)+1
        for char in t:
            set_t[char] = set_t.get(char,0)+1
        for key in set_s:
            if set_s[key] != set_t.get(key,0):
                return False
        return True



        