class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        while l <= r:
            mid_point = (l+r)//2
            if nums[mid_point] < target:
                l = mid_point+1
            elif nums[mid_point] > target:
                r = mid_point-1
            else:
                return mid_point
        return -1