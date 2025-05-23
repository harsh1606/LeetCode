class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_sorted = "".join(sorted(p))
        p_len = len(p)
        result = []
        for i in range(len(s)-p_len + 1):
            #for j in range(i, i + p_len):
            if p_sorted == (''.join(sorted(s[i:i+p_len]))):
                result.append(i)
        return result

        