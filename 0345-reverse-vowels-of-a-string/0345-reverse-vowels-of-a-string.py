class Solution:
    def reverseVowels(self, string: str) -> str:
        i = 0
        j = len(string) - 1
        str_list = set('aeiouAEIOU')

        string = list(string)
        while i < j :
            if string[i] in str_list and string[j] in str_list:
                string[i] , string[j] = string[j] , string[i]
                i += 1 
                j -= 1
            elif string[i] in str_list:
                j -= 1
            elif string[j] in str_list:
                i += 1
            else:
                i += 1
                j -= 1
        return (''.join(string))
            
        