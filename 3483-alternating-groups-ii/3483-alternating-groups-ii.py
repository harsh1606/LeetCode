class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # def fn_alter_no(arr):
        #     for i in range(1,len(arr)):
        #         if arr[i-1] == arr[i]:
        #             return 0
        #     return 1
            
        # main_colors = colors+colors[0:k-1]
        # cnt = 0
        # for i in range(len(colors)):
        #     cnt += fn_alter_no(main_colors[i:i+k])
        
        # return cnt


        # main_colors = colors+colors[0:k-1]
        # cnt = 0
        # for i in range(len(colors)):
        #     flg = True
        #     for j in range(i+1,i+k):
        #         if main_colors[j-1] == main_colors[j]:
        #             flg = False
            
        #     if flg:
        #         cnt += 1
        # return cnt

        main_colors = colors + colors[:k-1]

        res = [1]
        cnt = 0
        for i in range(1,len(main_colors)):
            if main_colors[i] != main_colors[i-1]:
                res.append(res[i-1] + 1)
            else:
                res.append(1)

            if res[i] >= k:
                cnt += 1
        #print(res)
        return cnt
    
