class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_products = [0] * n
        postfix_products = [0] * n
        result = [0] * n

        curr_product = 1
        for index in range(len(nums)):
            curr_product *= nums[index]
            prefix_products[index]=curr_product
        
        curr_product = 1
        for index in range(len(nums)-1, -1, -1):
            curr_product *= nums[index]
            postfix_products[index]=curr_product

        for index in range(len(nums)):
            prefix_product = prefix_products[index-1] if index > 0 else 1
            postfix_product = postfix_products[index+1] if index < len(nums)-1  else 1
            result[index]=prefix_product * postfix_product
        
        return result


