class Solution:
    def twoSum(self, nums, target):
        intmap = dict()
        for i in range(len(nums)):
            n = nums[i]
            if (target - n) in intmap:
                return [intmap[target - n], i]
            else:
                intmap[n] = i

print(Solution().twoSum([1,6142,8192,10239],18431))

# violent
'''
class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        for i in range(len(nums)-1):
            for n in range(i+1,len(nums)):
                guess = nums[i] + nums[n]
                if guess == target:
                    return [i,n]
'''