class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        res = []
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        lst = list(m)

        for _ in range(k):
            highest = lst[0]
            for i in lst:
                if m[highest] <= m[i]:
                    highest = i
                    print(m[i])
            res.append(highest)
            lst.remove(highest)
        return res



        
        