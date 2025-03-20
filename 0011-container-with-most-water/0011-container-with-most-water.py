class Solution:
    def maxArea(self, height: List[int]) -> int:

        ## Naive Approch
        # max = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         mul = min(height[i],height[j])*(j-i)
        #         max = max(mul,max) 
                ## if mul > max :
                ##     max = mul
            
        # return max

        # max_area = 0  ## max
        # l,r = 0,len(height)-1

        # while l !=r :
        #     curr_area = min(height[l],height[r])*(r-l)
        #     max_area = max(max_area, curr_area)

        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1

        # return max_area

        max_area = 0
        l, r = 0, len(height)-1
        
        while l < r:
            max_area = max(max_area, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

