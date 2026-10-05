nums = [-4, -1, 0, 3, 10]

result = [0] * len(nums)

left = 0
right = len(nums) - 1
k = len(nums) - 1

while left <= right:

    if abs(nums[left]) > abs(nums[right]):
        result[k] = nums[left] ** 2
        left += 1
    else:
        result[k] = nums[right] ** 2
        right -= 1

    k -= 1

print(result)