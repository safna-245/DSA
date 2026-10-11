
target = 7
nums = [2, 3, 1, 2, 4, 3]

left = 0
total = 0
min_length = float('inf')

for right in range(len(nums)):
    total += nums[right]

    while total >= target:
        min_length = min(min_length, right - left + 1)
        total -= nums[left]
        left += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)
