class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # carry = 0
        # len_digits = len(digits)-1
        # for i in range(len_digits, -1, -1):
        #     if i == len_digits:
        #         if digits[i] + 1 > 9:
        #             digits[i] = 0
        #             carry = 1
        #         else:
        #             digits[i] = digits[i] + 1
        #     else:
        #         digits[i] += carry
        #         carry = 0
        # return digits

        
        s = ''
        for i in digits:
            s += str(i)
        a = int(s) + 1
        res = []
        for i in str(a):
            res.append(int(i))
        return res