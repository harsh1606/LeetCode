class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ele = 0
        left = 0
        min_cnt = float('inf')

        for right in range(len(nums)):
            sum_ele += nums[right]
            while sum_ele >= target:
                min_cnt = min(min_cnt, right - left + 1)
                sum_ele -= nums[left]
                left += 1
        
        if min_cnt == float('inf'):
            return 0
        return min_cnt
        