class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        for i in range(len(nums)-1):
            for n in range(i+1,len(nums)):
                guess = nums[i] + nums[n]
                if guess == target:
                    return [i,n]

print(Solution().twoSum([1,6142,8192,10239],18431))

# indexed array
'''class Solution:
    
    def findMax(self):
        base = round(self.target/2)
        if (2*base) == self.target:
            return base, base
        else:
            return base, base+1
        
    def createNumArray(self):
        bound = 0
        if max(self.nums) > abs(min(self.nums)):
            bound = max(self.nums)
        else:
            bound = abs(min(self.nums))
        num_collection = [[-1]*6 for i in range(bound+1)]
        for i in range(len(self.nums)):
            num_index = abs(self.nums[i])
            if self.nums[i] < 0:
                num_collection[num_index][3] += 1
                if num_collection[num_index][4] == -1:
                    num_collection[num_index][4] = i
                else:
                    num_collection[num_index][5] = i
            else:
                num_collection[num_index][0] += 1
                if num_collection[num_index][1] == -1:
                    num_collection[num_index][1] = i
                else:
                    num_collection[num_index][2] = i
        return num_collection
    
    def findAns(self, base_upper, base_lower, num_collection):
        find = False
        output = []
        if base_upper == base_lower:
            if (num_collection[base_upper][0] == 1) or (num_collection[base_upper][3] == 1):
                if base_upper < 0:
                    output.append(num_collection[base_upper][4])
                    output.append(num_collection[base_upper][5])
                    return output
                else:
                    output.append(num_collection[base_upper][1])
                    output.append(num_collection[base_upper][2])
                    return output
            base_upper += 1
            base_lower -= 1

        while (not find) and (base_upper < 10**9):
            output = []
            if base_lower > 0:
                if num_collection[base_lower][0] > -1:
                    output.append(num_collection[base_lower][1])
            else:
                if num_collection[abs(base_lower)][3] > -1:
                    output.append(num_collection[abs(base_lower)][4])
            if base_upper > 0:
                if num_collection[base_upper][0] > -1:
                    output.append(num_collection[base_upper][1])
            else:
                if num_collection[abs(base_upper)][3] > -1:
                    output.append(num_collection[abs(base_upper)][4])
            if len(output) == 2:
                find = True
                return output
            base_upper += 1
            base_lower -= 1
    
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        ubase, lbase = Solution.findMax(self)
        num_array = Solution.createNumArray(self)
        return Solution.findAns(self, ubase, lbase, num_array)'''
