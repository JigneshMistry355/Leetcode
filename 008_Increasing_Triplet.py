from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool: # Finds triplet subsequence of contigious locations
        if len(nums) < 3:
            return False
        for i in range(1,len(nums)-1):
            check_left = nums[i-1] < nums[i] # store bool
            check_right = nums[i+1] > nums[i] # store bool
            # print(nums[i-1],nums[i], nums[i+1])
            if check_left and check_right:
                return True
        return False
    
    def increasingTripletNonContigious(self, nums: List[int]) -> bool: 
        first = second = third = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            elif i <= third:
                return True
        return False
    
    def optimalSolution(self, nums: List[int]) -> bool:
        left = right = float('inf')
        for num in nums:
            if num <= left:
                left = num
            elif num <= right:
                right = num
            else:
                return True
        return False


if __name__ == '__main__':
    nums =  [20,100,10,12,5,13]
    obj = Solution()
    result = obj.optimalSolution(nums)
    print(result)