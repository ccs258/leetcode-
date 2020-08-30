"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class SolutionFirst:
    def twoSum(self, nums, target,current_idx):
        final_rst = []
        for idx,val in enumerate(nums):
            if idx == current_idx:
                continue
            sub_rst = []
            if target - val in nums:
                rst = list(filter(lambda x:(x[1] == val or x[1] == target - val) and x[0] != current_idx,list(enumerate(nums))))
                rst_val = set(map(lambda x:x[1],rst))
                for sub in rst_val:
                    rst_cur = list(map(lambda x:x[0],filter(lambda x:x[1] == sub,rst)))
                    if len(rst_cur) > 1:
                        rst_cur_val = min(rst_cur)
                    else:
                        rst_cur_val = rst_cur[0]
                    sub_rst.append(rst_cur_val)
            print("sub_rst is ",sub_rst)
            if len(sub_rst) > 1:
                final_rst.append(sub_rst)
        return final_rst

    def threeSum(self, nums):
        if not nums:
            return []
        if nums.count(0) == len(nums) and len(nums)>2:
            return [[0,0,0]]
        final_rst_rst = []
        for idx,first in enumerate(nums):
            two_rst = self.twoSum(nums,-first,idx)
            print("two_rst is ",two_rst)
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
        if nums.count(0)>2:
            final.append([0,0,0])
        return final


"""
超出时间限制；
思路：
（1）遍历列表，取第一个元素，在第一个元素基础上，按照计算两数之和的方法计算列表与目标值的两个数；
（2）注意返回结果是返回值，而非索引；对于索引对应值相同的，只用保留其中一个索引即可（本解法取的是最小索引）；
特殊情况：[-2,0,0,2,2],最终结果输出为[-2,0,2];
先取出所有可能的组合，再处理（2）中的情况，按照值相同的取最小的索引，这样很浪费时间，感觉最好是，相同的值，取到了之后，就不用了参与计算了；


优化解法：只关心值，不关心索引；0做特殊处理，其他均去重后计算；


参考官方题解：
https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/

思路：
先考虑不重复的组合；
表达不重复，第一个元素的不重复表达；第二个和第三个元素的不重复表达，后者可以设计为并行，相互约束；N^3的复杂度可以降到N^2;

"""

class Solution:
    def twoSum(self, nums, target):
        sub_rst = []
        flag_nums = nums
        for val in nums:
            if target - val in flag_nums:
                if (target - val == val and nums.count(val)==1):
                    continue
                else:
                    sub_rst.append([val,target - val])
                    flag_nums.remove(val)
                    flag_nums.remove(target - val)

        return sub_rst

    def threeSum(self, nums):
        if not nums:
            return []
        final = []
        if nums.count(0) == len(nums):
            if len(nums)>2:
                return [[0,0,0]]
            else:
                final.append([0,0,0])

        nums = list(set(tuple(nums)))

        for first in nums:
            rst = self.twoSum(nums,-first)
            if rst:
                for sub in rst:
                    sub.append(first)
                    final.append(sub)
        return final
            # if rst:
            #     print("yes is ",list(map(lambda x:x.append(first),rst)))#在python表达式中，不太适合在lambda的表达式中写append之类的函数
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

"""
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
"""
通过官方解答：值得借鉴的两点：
（1）不重复的表达，起始元素位置表示，以及相邻重复元素的判定；
（2）双指针的利用，一方从左至右遍历，另一边从右向左遍历，注意右指针的挪动条件；
 # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
"""



if __name__ == '__main__':
    so = Solution()
    nums = [-1,0,1,2,-1,-4]
    final_rst_rst = so.threeSum(nums)
    ##
    print("final_rst_rst,final_rst_rst_val is ",final_rst_rst)
    # ts = [1,2,3,4]
    # for i in ts:
    #     print("ts is ",ts)
    #     print("i is",i)
    #     ts.remove(4-i)
    #     print("ts is ",ts)



