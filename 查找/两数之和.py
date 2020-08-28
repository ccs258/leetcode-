"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def twoSum(self, nums, target):
        for val in nums:
            if target - val in nums:
                rst = list(map(lambda x:x[0],filter(lambda x:x[1] == val or x[1] == target - val,list(enumerate(nums)))))
                if len(rst) == 2:
                    return rst
                # if target - val == val:


if __name__ == '__main__':
    so = Solution()
    nums = [3,3]
    target = 6
    rst = so.twoSum(nums,target)
    print("rst is",rst)
