class Solution:

    # this checks for continuous substring
    def isSubstring(self, s:str, t:str) -> bool:
        sub_len = len(s) # 3
        str_len = len(t) # 9

        for i in range(str_len):
            if t[i:sub_len] == s:
                return True

        return False
    
    # check if each char in sub_str is present in string in any order
    def isSubstringTwoPointer(self, s:str, t:str) -> bool:
        # pointer to 1st char in s
        sp = 0
        # pointer to 1st char in t
        tp = 0
    
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)


obj = Solution()
result = obj.isSubstringTwoPointer('abc', 'abcdefghi')
print(result)