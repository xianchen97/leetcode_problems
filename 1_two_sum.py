class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCount = {}
        for idx, char in enumerate(nums):
            if target-char in numsCount:
                return [numsCount[target-char], idx]
            numsCount[char] = idx