def containsDuplicate(nums):

        nums_set = set()
        
        for n in nums:

            if n in nums_set:

                return True
            
            nums_set.add(n)
        
        return False

nums = [2,3,4,5,7]

print(containsDuplicate(nums))