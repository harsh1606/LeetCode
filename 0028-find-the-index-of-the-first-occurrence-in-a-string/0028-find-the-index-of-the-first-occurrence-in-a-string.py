class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack) or len(needle) == 0 or len(haystack) == 0:
            return -1
        # if haystack == needle:
        #     return 0
        for i in range(len(haystack)-len(needle)+1):
            left = 0
            while haystack[left + i] == needle[left]:
                if left == len(needle)-1:
                    return i
                left += 1
                
        return -1
        