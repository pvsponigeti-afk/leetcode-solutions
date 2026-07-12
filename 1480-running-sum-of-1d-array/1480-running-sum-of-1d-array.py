class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            Sum=0
            for j in range(i+1):
                Sum+=nums[j]
            result.append(Sum)
        return result
        