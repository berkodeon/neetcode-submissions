class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_nums = set()
        for num in nums:
            if num in uniq_nums:
                return True
            uniq_nums.add(num)
        return False