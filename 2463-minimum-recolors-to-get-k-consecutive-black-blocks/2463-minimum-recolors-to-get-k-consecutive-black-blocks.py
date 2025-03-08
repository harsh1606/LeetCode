class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wh_cnt = blocks[:k].count('W')
        min_op = wh_cnt

        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                wh_cnt -= 1
            if blocks[i] == 'W':
                wh_cnt += 1
            
            min_op = min(min_op, wh_cnt)
        return min_op
                
        
        

            
                
