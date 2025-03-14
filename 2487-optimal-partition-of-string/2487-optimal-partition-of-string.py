class Solution:
    def partitionString(self, s: str) -> int:
        cnt = 1
        word_list = []
        for i in s:
            if i not in word_list:
                word_list.append(i)
            else:
                cnt += 1
                word_list = [i]
        return cnt