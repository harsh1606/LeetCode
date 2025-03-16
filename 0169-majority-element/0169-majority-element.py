class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dic = {}
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] in dic:
        #         dic[nums[i]] += 1
        #         if dic[nums[i]] > n//2:
        #             return nums[i]
        #     else:
        #         dic[nums[i]] = 1
        # return nums[0]


        res = nums[0]
        cnt = 0

        for i in nums:
            if i == res:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt < 0:
                res = i
                cnt = 1
        return res
        


        