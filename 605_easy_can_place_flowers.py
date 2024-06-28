class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        index = 0

        while index < len(flowerbed):
            if flowerbed[index] == 0:
                left_empty = (index == 0 or flowerbed[index-1] == 0 )
                right_empty = (index == len(flowerbed)-1 or flowerbed[index + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[index] = 1
                    count += 1
                    index += 1
            index += 1
        
        return count >= n


 
