class Solution:
    # Plot 1 between two 0 ( 000 --> 010 )
    def PlotFlowers(self, flowerbed, n):
        count = 0   # Tally with n, if count == n, return true

        for i in range(len(flowerbed)):

            # Check if current numbr is 0 or not
            if flowerbed[i] == 0:
                # Check value of current position
                # Check value of previous position
                empty_left_pos = (i == 0) or (flowerbed[i-1] == 0)   # Store this boolean

                # Check if the current position is final (nth) position
                # check if the next positon is 0 or not
                empty_right_pos =  (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if empty_left_pos and empty_right_pos:
                    flowerbed[i] = 1
                    count += 1

        return count >= n
    
if __name__ == '__main__':
    obj = Solution()
    flowerbed = [1,0,0,0,1]
    n = 3
    result = obj.PlotFlowers(flowerbed, n)
    print(result)


