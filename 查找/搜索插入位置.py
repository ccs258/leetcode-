
"""

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
"""

"""
版本V1：
尝试性地解决，知道本题查找元素主要分两类情况：
（1）如果target在nums中，直接返回；
（2）如果target不在nums中，利用二分查找的思想查找目标target应当插入的位置；
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

"""
版本V2
在基于版本1的基础上，细化写二分查找的内容；
同时需要注意的一点是：需要单独引入一个最原始的nums数组，用以查询原始的索引值，用于二分查找的nums则是不断变化的；
版本V2的缺点：if...else...太多，避免一种情况添加一个if...else...,而是需要把相同的情况归为一类处理，增加逻辑的通用性，减少特殊对待；
class Solution:
    def find_index(self,raw_nums,nums,target):
        mid = len(nums)//2
        left = nums[0:mid]
        right = nums[mid:len(nums)]
        if left[-1] < target < right[0]:
            return nums.index(left[-1]) + 1
        if len(left) > 1:
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
            elif  target < raw_nums[0]:
                return 0
            elif target > raw_nums[-1]:
                return len(raw_nums)
            return self.find_index(raw_nums,nums,target)

"""


##最终版本V3##
"""
版本V3：

在版本1和版本V2的基础上，对于查询做了进一步逻辑梳理：分为直接出查询索引结果和二分法计算索引结果两大类；
直接查询索引结果包含三类：
    （1）target在nums中,直接返回其索引；
    （2）target小于nums[0]，则应插入到最左边，返回索引0;
    （3）target大于nums[len(nums)-1]，则应插入到最右边，返回索引len(nums);
    
二分法计算索引结果也包含三类：
     首先声明下此部分定义的变量：输入raw_nums,输入nums（会动态变化的），中间索引mid,左边数组left和右边数组right；
     二分法查找包含的3大类情况为：
    （1）target大小位于左右数组相邻的中间，则返回左数组最后一位数在raw_nums原数组中的索引+1（也可以返回右数组第一位数在raw_nums原数组中的索引-1）
     (2) target小于左数组最后一位数，二分法递归计算查找索引，数组nums更新为left
     (2) target大于右数组第一位数，二分法递归计算查找索引，数组nums更新为right
     
"""
class Solution:
    def searchInsert(self,nums,target):
        if target in nums:
            return nums.index(target)
        elif  target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            raw_nums = list(nums)
            return self.checkInsert(raw_nums,nums,target)
    def checkInsert(self,raw_nums,nums, target) -> int:

        if  len(nums) == 1:
            return raw_nums.index(nums[0]) - 1 if nums[0] > target else raw_nums.index(nums[0]) + 1
        else:
            mid = len(nums)//2
            left = nums[0:mid]
            right = nums[mid:len(nums)]
            if left[-1] < target < right[0] :
                return raw_nums.index(left[-1])+1
            elif target < left[-1]:
                return self.checkInsert(raw_nums,left,target)
            else:
                return self.checkInsert(raw_nums,right,target)




if __name__ == '__main__':
    so = Solution()
    nums = [1,3,5,6]
    target = 5
    raw_nums = list(nums)
    rst = so.searchInsert(nums,target)
    print("rst is ",rst)