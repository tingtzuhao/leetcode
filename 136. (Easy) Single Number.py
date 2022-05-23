class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
        
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         dup = []
#         for i in range(len(nums)):
#             if not dup:
#                 dup.append(nums[i])
#             elif nums[i] in dup:
#                 dup.remove(nums[i])
#             else:
#                 dup.append(nums[i])
#         return dup[0]