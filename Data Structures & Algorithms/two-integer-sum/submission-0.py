class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            target_value = target - nums[i] 
            if target_value in m:
                return sorted([i, m[target_value]])
            if nums[i] not in m:
                m[nums[i]] = i
            