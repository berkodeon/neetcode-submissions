class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for index2 in range(index+1, len(nums)):
                if nums[index] + nums[index2] == target:
                    return [index, index2]