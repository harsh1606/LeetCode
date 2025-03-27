class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # l = len(nums)
        # arr = []
        # for i in range(l-2):
        #     for j in range(i+1, l-1):
        #         for k in range(j+1, l):
        #             if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in arr:
        #                 arr.append(sorted([nums[i], nums[j], nums[k]]))
        # return arr

        # def two_sum(nums, tar):
        #     l, r = 0, len(nums) - 1
        #     while l < r:
        #         if nums[l] + nums[r] == tar:
        #             return [nums[l],nums[r]]
        #         elif nums[l] + nums[r] < tar:
        #             l += 1
        #         else:
        #             r -= 1
        #     return []

        # result = []
        # nums = sorted(nums)

        # for i in range(len(nums)-2):
        #     tar = 0 - nums[i]
        #     arr = two_sum(nums[i+1:], tar)
        #     if arr:
        #         result.append([nums[i], arr[0], arr[1]])
        # return result

        result = []
        nums.sort()
        for i in range(len(nums)-2):
            total = -nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == total:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif nums[l] + nums[r] < total :
                    l += 1
                else:
                    r -= 1
        return result