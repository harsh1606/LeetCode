class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        
        for i in range(1, len(nums)):
            if nums[start] != nums[i]:
                start += 1
                nums[start] = nums[i]
        #print(nums)
        print(start)
        return start + 1
