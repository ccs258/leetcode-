"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def twoSum(self, nums, target,current_idx):
        final_rst = []
        for idx,val in enumerate(nums):
            if idx == current_idx:
                continue
            if target - val in nums:
                rst = set(map(lambda x:x[0],filter(lambda x:(x[1] == val or x[1] == target - val) and x[0] != current_idx,list(enumerate(nums)))))
                if len(rst) == 2:
                    final_rst.append(rst)
        return final_rst

    def threeSum(self, nums):
        if not nums:
            return []
        if nums.count(0) == len(nums):
            if len(nums) > 2:
                return [[0,0,0]]
            else:
                return []
        final_rst_rst = []
        for idx,first in enumerate(nums):
            two_rst = self.twoSum(nums,-first,idx)
            for rst in two_rst:
                first = [idx]
                first.extend(rst)
                first = sorted(first)
                if first not in final_rst_rst:
                    final_rst_rst.append(first)
        final = set(map(lambda x:tuple(sorted((nums[x[0]],nums[x[1]],nums[x[2]]))), final_rst_rst))
        final = [list(i) for i in final]
        #final_rst_rst是返回的索引；final_rst_rst_val返回索引对应的值；
        #但题目要求的是返回不重复的元素，即不同索引但元素值一样也算重复；
        return final

if __name__ == '__main__':
    so = Solution()
    nums = [-2,0,0,2,2]
    final_rst_rst = so.threeSum(nums)
    ##
    print("final_rst_rst,final_rst_rst_val is ",final_rst_rst)


