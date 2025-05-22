class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # cnt = 0
        # max_cnt = 0

        # com_set = []

        # for i in s:
        #     while i in com_set:
        #         com_set.pop(0)
        #         cnt -= 1
                
        #     if i not in com_set:
        #         com_set.append(i)
        #         cnt += 1
        #     max_cnt = max(max_cnt, cnt)
        # return max_cnt 


        left = 0
        max_cnt = 0
        #cnt = 0
        com_set = set()

        for right in range(len(s)):
            while s[right] in com_set:
                com_set.remove(s[left])
                left += 1
            com_set.add(s[right])
            max_cnt = max(max_cnt, right-left + 1)
        return max_cnt 

        
        
        