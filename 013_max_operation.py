from typing import List
from collections import Counter

class Solution:

    def maxOperation(self, nums: List[int], k: int) -> int:
        n = len(nums)
        operations = 0
        left = 0
        right = n-1

        while left < right:
            if nums[left] + nums[right] == k:
                operations += 1
                left += 1
                right -= 1
            
            elif nums[left] + nums[right] < k:
                left += 1

            else:
                right -= 1
        
        return operations

    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums) # {3:3, 1:1, 4: 1, 2:1}
        nums = set(nums) # {1,2,3,4}
        num = list(nums) # [1,2,3,4]
        # nums.sort()
        # print(nums)
        res = 0
        n = len(num)
        for i in range(n):       # i=1               #### i=2               #### i=3
            if k-num[i] in nums: # k-num[i]=6-2 = 4  #### k-num[i]=6-3 = 3  #### k-num[i]=6-4 = 2
        
                            # cnt[2]=1    # cnt[4]=1 
                            # cnt[3]=3    # cnt[3]=3
                            # cnt[4]=1    # cnt[2]=1
                res += min(cnt[num[i]], cnt[k-num[i]])  # counts are takes from dictionary cnt
                # res = 1 + 3 + 1

        # the pair (2,4) and (4,2) are counted as total 2 counts in the loop 
        # but since we know we have counted them twice, we divide it by 2
        res //= 2   # 5 // 2 = 2
        return res

if __name__ == '__main__':
    obj = Solution()
    nums = [3,1,3,4,3,2]
    k = 6
    result = obj.maxOperations(nums, k)
    print(result)