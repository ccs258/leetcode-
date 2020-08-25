"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
"""

"""
class Solution:
    def find_index(self,raw_nums,nums,target):
        mid = len(nums)//2
        left = nums[0:mid]
        right = nums[mid:len(nums)]
        if len(nums) > 2:
            if target < left[-1]:
                return self.find_index(raw_nums,left,target)
            else:
                return self.find_index(raw_nums,right,target)
        else:
            if left[0] > target:
                return nums.index(right[0])-1
            else:
                if
                 if len(nums) > 2 else (nums.index(right[0])-1 if right[0] > target else nums.index(right[0]) )

    def searchInsert(self, nums, target) -> int:
        raw_nums = list(nums)
        if target in nums:
            return nums.index(target)
        else:
            return self.find_index(raw_nums,nums,target)

"""

class Solution:
    def find_index(self,raw_nums,nums,target):
        mid = len(nums)//2
        left = nums[0:mid]
        right = nums[mid:len(nums)]
        if len(nums) > 2:
            if target < left[-1]:
                return self.find_index(raw_nums,left,target)
            else:
                return self.find_index(raw_nums,right,target)
        else:
            if left[0] < target < right[0] :
                return raw_nums.index(left[0])+1
            elif  target < left[0]:
                return raw_nums.index(left[0])-1  if  raw_nums.index(left[0]) != 0 else 0
            else:
                return raw_nums.index(right[0])+1

    def searchInsert(self, nums, target) -> int:
        raw_nums = list(nums)
        if target in nums:
            return nums.index(target)
        else:
            if len(raw_nums) == 1:
                return 0 if raw_nums[0] > target else 1
            return self.find_index(raw_nums,nums,target)




if __name__ == '__main__':
    so = Solution()
    nums = [1,3,5,6]
    target = 0
    rst = so.searchInsert(nums,target)
    print("rst is ",rst)