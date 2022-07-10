class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 0
        rtype = [0] * len(nums)
        for i in range(len(nums)):
            tmp += nums[i]
            rtype[i] = tmp
        return rtype