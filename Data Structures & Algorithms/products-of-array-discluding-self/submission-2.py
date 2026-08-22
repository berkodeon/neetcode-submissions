class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        curr_pref_product = 1
        for index in range(len(nums)):
            result[index] = curr_pref_product
            curr_pref_product *= nums[index]

        curr_post_product = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] = result[index] * curr_post_product
            curr_post_product *= nums[index]
        return result
        