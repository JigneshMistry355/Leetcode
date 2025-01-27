class Solution:
    def KidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)
        result = []
        for i in range(len(candies)):
            if (candies[i]+extraCandies) >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
    
if __name__ == '__main__':
    obj = Solution()
    candies = [12,1,12]
    extraCandies = 3
    result = obj.KidsWithCandies(candies, extraCandies)
    print(result)
                

