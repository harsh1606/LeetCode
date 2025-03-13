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
        min_len = min(len(word1),len(word2))
        for i in range(min_len):
            s = s + word1[i] + word2[i]
    
        if len(word1) > len(word2):
            s += word1[i+1:]
        else:
            s += word2[i+1:]
        return s