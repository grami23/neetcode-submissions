class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for p in range(len(nums)):
                if (i != p) and ((nums[i]+nums[p]) == target):
                    return [i, p]
            # if i != nums.index((target - nums[i])):
            #     # return [i, nums.index(target - nums[i])]
            #     return [nums.index(target - nums[i]), i]