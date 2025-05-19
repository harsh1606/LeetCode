class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ## nums = [-4, -1, 1, 2]
        min_res = float('inf')
        min_value = float('inf')

        for i in range(len(nums) - 2):
            ## Repeat digit for offset
            if i > 0 and nums[i] == nums[i-1]:
                continue

            low = i + 1
            high = len(nums) - 1
            while low < high:
                sum_arr = nums[i] + nums[low] + nums[high]
                if abs(target - sum_arr) < min_res:
                    
                    min_value = sum_arr
                    min_res = abs(target - sum_arr)

                if (target - nums[i]) > (nums[low] + nums[high]):
                    low += 1
                else:
                    high -= 1
                

                # low += 1
                # high -= 1

                # while low < high and nums[low] == nums[low+1]:
                #     low += 1
                # while low < high and nums[high] == nums[high-1]:
                #     high -= 1
        return min_value    

