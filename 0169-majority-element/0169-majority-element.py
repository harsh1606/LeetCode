class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]] += 1
                if dic[nums[i]] > n//2:
                    return nums[i]
            else:
                dic[nums[i]] = 1
        return nums[0]

        