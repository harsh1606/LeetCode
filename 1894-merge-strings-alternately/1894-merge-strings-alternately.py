class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        # if len(word1) > len(word2):
        #     word1 , word2 = word2 , word1
        
        # for i in range(max(len(word1),len(word2))):
        #     try :
        #         s = s + word1[i] + word2[i]
        #     except:
        #         try:
        #             s = s + word2[i:]
        #         except :
        #             s = s + word1[i:]
        #         break
        # return s
        # min_len = min(len(word1),len(word2))
        # for i in range(min_len):
        #     s = s + word1[i] + word2[i]
    
        # if len(word1) > len(word2):
        #     s += word1[i+1:]
        # else:
        #     s += word2[i+1:]
        # return s

        i = j = 0
        s = ''
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                s += word1[i]
                i += 1
            if j < len(word2):
                s += word2[j]
                j += 1
        return s