"""
最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution(object):
    def max_sub_array(self,nums):
        pre =0
        max_ans = nums[0]
        for part in nums:
            pre = max(pre+part,part)  #实现确定左边数组边界的效果
            max_ans = max(max_ans,pre)
        return max_ans

    def max_sub_array_out(self,nums):
        pre = 0
        max_ans = nums[0]
        left_index = 0
        for idx,part in enumerate(nums):
            if pre >= part:
                pre = pre + part
                continue
            else:
                left_index = left_index + 1
                pre = nums[left_index]


        return left_index





if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    so = Solution()
    rst = so.max_sub_array(nums)
    print("rst is ",rst)

    left = so.max_sub_array_out(nums)
    print("left,right  is ",left )