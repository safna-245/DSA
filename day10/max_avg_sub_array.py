nums = [1, 12, -5, -6, 50, 3]
k = 4

# Find sum of first k elements
window_sum = sum(nums[:k])

# Store the maximum sum
max_sum = window_sum

# Slide the window
for i in range(k, len(nums)):
    window_sum = window_sum - nums[i - k] + nums[i]

    if window_sum > max_sum:
        max_sum = window_sum

# Calculate maximum average
answer = max_sum / k

print("Maximum average:", answer)