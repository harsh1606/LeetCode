from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # try:
        #     prod = reduce(lambda x,y : x*y, (i for i in nums if i!=0))
        # except :
        #     prod = 0

        # zero_cnt = nums.count(0)

        # result = []
        # for i in nums:
        #     if zero_cnt > 1 :
        #         result.append(0)
        #     elif zero_cnt == 1:
        #         if i == 0 :
        #             result.append(prod)
        #         else:
        #             result.append(0)
        #     else:
        #         result.append(prod//i)
        # return result

        cnt_zero = 0
        mul = 1
        for i in nums:
            if i == 0:
                cnt_zero += 1
            else:
                mul *= i
        
        answer = []
        for i in nums:
            if cnt_zero == 0:
                answer.append(mul//i)
            elif cnt_zero == 1:
                if i == 0:
                    answer.append(mul)
                else:
                    answer.append(0)
            else:
                answer.append(0)

        return answer