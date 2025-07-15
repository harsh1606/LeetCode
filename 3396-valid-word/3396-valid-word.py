class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        if not word.isalnum():
            return False
        
        has_vowel = False
        has_conson = False

        vowels = set('aeiouAEIOU')
        # number = set((0,1,2,3,4,5,6,7,8,9))
        for char in word:
            if char in vowels:
                has_vowel = True
            else:
                if not char.isnumeric():
                    has_conson = True
            
        return has_vowel and has_conson

        