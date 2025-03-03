height = [1,8,6,2,5,4,8,3,7]
        # 0,1,2,3,4,5,6,7,8

n = len(height)
left = 0
right = n-1
max_area =  0

while left < right:

    if height[left] < height[right]:
        width = right - left
        current_height = min(height[left], height[right])
        max_area = max(max_area, current_height*width)
        left += 1
    else:
        width = right - left
        current_height = min(height[left], height[right])
        max_area = max(max_area, current_height*width)
        right -= 1

print(max_area)


