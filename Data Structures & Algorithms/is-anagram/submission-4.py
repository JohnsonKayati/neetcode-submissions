class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in s_set:
                s_set[s[i]] = 1
            else:
                s_set[s[i]] += 1
            if t[i] not in t_set:
                t_set[t[i]] = 1
            else:
                t_set[t[i]] += 1
        if s_set == t_set:
            return True
        return False