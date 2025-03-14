class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if (flowerbed[0] == 0 and flowerbed[1] == 0 ) or \
        #         (flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0):
        #     n-=1

        # if (flowerbed[0] == 0 and flowerbed[1] == 0 ) :
        #     n-=1
        #     flowerbed[0] = 1
    
        # if (flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0):
        #     n-=1
        #     flowerbed[len(flowerbed)-1] = 1

        # for i in range(1,len(flowerbed)-1):
        #     if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
        #         n -= 1
        #         flowerbed[i] = 1
        #     if n == 0 :
        #         return True
        # if n == 0 :
        #     return True
        # return False

        cnt = 0
        end = len(flowerbed)
        for i in range(end):
            left = False
            right = False
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i-1] == 0:
                    left = True
                
                if i == end-1 or flowerbed[i+1] == 0:
                    right = True
                
                if left and right:
                    cnt += 1
                    flowerbed[i] = 1
                    if cnt >= n:
                        return True
            
        return cnt >= n
            
        
        
