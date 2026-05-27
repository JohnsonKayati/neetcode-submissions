class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        c = 0
        while l <= r:
            m = (r + l) // 2
            print(m)
            
            if nums[m] == target:
                return m
            
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
            
        return -1