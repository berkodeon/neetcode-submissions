class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        A = []
        for index, num in enumerate(nums):
            A.append([num, index])
        A.sort()
        while i<j:
            num_i, curr_i = A[i]
            num_j, curr_j = A[j]
            curr_sum = num_i + num_j
            if curr_sum == target:
                return [min(curr_i, curr_j), max(curr_i, curr_j)]
            elif curr_sum > target:
                j = j-1
            elif curr_sum < target:
                i = i+1

