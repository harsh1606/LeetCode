class Solution:
    def countSubstrings(self, s: str) -> int:
        def fn_check_pali(txt):
            if txt == txt[::-1]:
                return True
            return False


        cnt = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if fn_check_pali(s[i:j]):
                    cnt += 1
        return cnt
        