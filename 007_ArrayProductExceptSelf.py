def productExceptSelf(nums): # Huge time complexity
    product = 1
    result = []
    for i in range(len(nums)):
        for j in range(0, len(nums)):
            # if both index i & j are same, they are multiplying to itself
            if i != j:
                product = product * nums[j]
            # print(product)
        result.append(product)
        product = 1
    return result

def productExceptSelfOptimized(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    ans = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    for i in range(n):
        ans[i] = prefix[i] * suffix[i]

    return ans


# nums = [0,0]
nums=[1,2,3,4]
result = productExceptSelfOptimized(nums)
print(result)