class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        con_ones = 0
        max_con_ones = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                con_ones += 1
            else:
                con_ones = 0
            max_con_ones = max(max_con_ones, con_ones)
        return max_con_ones
        