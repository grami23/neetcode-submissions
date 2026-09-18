class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if not num in dict:
                dict[num] = num
            else:
                return True
        return False

            