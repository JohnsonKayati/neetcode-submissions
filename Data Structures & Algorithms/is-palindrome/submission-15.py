class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for ch in s:
            if ch.isalnum():
                filtered += ch
        filtered = filtered.lower()
        p1 = 0
        p2 = len(filtered) - 1

        for _ in range(len(filtered)):
            if filtered[p1] != filtered[p2]:
                print("p1", filtered[p1], "p2", filtered[p2])
                return False
            p1 += 1
            p2 -= 1
        
        return True