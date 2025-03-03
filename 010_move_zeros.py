from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        # count zeros
        zero_count = 0
        for i in range(len(nums)):
            zero_count += (nums[i] == 0)
        
        new_list = []
        
        # append non-zero elements into new_list
        for i in range(0,len(nums)):
            print(f"nums[{i}] ==> ",nums[i])
            if nums[i] != 0:
                print(nums)
                new_list.append(nums[i])

        # append zeros to new_list
        while (zero_count):
            new_list.append(0)
            zero_count -= 1

        # copy new_list to original array
        for i in range(len(nums)):
            nums[i] = new_list[i]

        # return the original array        
        return nums
    
nums = [0,1,0,3,12]
# nums = [0,0,1]
obj = Solution()
result = obj.moveZeroes(nums)
print(nums)