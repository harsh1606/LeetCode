class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # cnt = 0
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(i, len(nums)):
        #         prod *= nums[j]
        #         if prod < k:
        #             cnt += 1
        #         else:
        #             break
        # return cnt
        left = 0
        cnt  = 0
        prod = 1

        if k <= 1:
            return 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod = prod // nums[left]
                left += 1

            cnt += (right - left + 1)
        return cnt