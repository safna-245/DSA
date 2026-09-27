def singleNumber(nums):

        for num in nums:

            if nums.count(num) == 1:

                return num

nums = [2,4,3,1,2,3,4]

print(singleNumber(nums))

