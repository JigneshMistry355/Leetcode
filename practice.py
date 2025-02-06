# s = "a good   example"
# word = s.strip().split()
# print(word[::-1])

nums = [1,2,3,4]
# prefix = [1] * len(nums)
# print(prefix)

suffix = [1] * len(nums)

n = len(nums)
for i in range(n-2, -1, -1):
    suffix[i] = suffix[i+1] * nums[i+1]
    print(suffix)
