
def twoSum(nums, target):

    arr = [(nums[i],i) for i in range(len(nums))]

    arr.sort()


    left = 0

    right = len(nums)-1

    while(left < right):

        curr_sum = arr[left][0]+arr[right][0]

        if curr_sum == target:

            return [arr[left][1],arr[right][1]]


        elif curr_sum > target:

            right = right - 1

        elif curr_sum < target:

            left = left + 1

nums = [2,7,4,6,8]

target = 9

print(twoSum(nums,target))

        