def majorityElement(nums):
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

nums = [2, 2, 1, 1, 1, 2, 2]

print(majorityElement(nums))