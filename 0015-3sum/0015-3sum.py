class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            comp = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == comp:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < comp:
                    left += 1
                else:
                    right -=1
        return [list(i) for i in res]
        