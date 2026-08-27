class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            com=target-nums[i]
            if com in nums and nums.index(com) != i:
                return [i,nums.index(com)]