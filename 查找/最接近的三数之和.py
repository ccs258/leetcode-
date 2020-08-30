"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class SolutionV1(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()

        # 枚举 a
        delta = abs(nums[0] + nums[1] + nums[2] - target)
        for first in range(n):
            print("first is ", first)
            if abs(nums[first] + nums[first + 1] + nums[first + 2] - target) > delta:
                return nums[first - 1] + nums[first] + nums[first + 1]
            i = 0

            cur_delta = abs(nums[first] + nums[first + 1] + nums[first + 2] - target)
            while nums[first] == 0 and first > 1:
                if abs(nums[first] + nums[first + 1] + nums[first + 2] - target) < delta:
                    cur_delta = abs(nums[first - i] + nums[first + 1] + nums[first + 2] - target)
                    i = i + 1

            if cur_delta <= delta and first + 2 < len(nums) - 1 and cur_delta != 0:
                continue
            else:
                return nums[first] + nums[first + 1] + nums[first + 2]


"""
含有0的就不对了，需要特殊处理；
nums = [-3,0,1,2],这个不对，因为中间的0，其实可以跳过；

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7  # 写一个题目条件范围的最大值

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1   #左，右指针是分开的，左指针对应最开头的指针，右指针对应最右边的指针，相比我的那个连续，可以避免0带来的问题；
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:    #要么移动右指针
                    # 如果和大于 target，移动 c 对应的指针 ，对应变量k代表的，向左移动；
                    k0 = k - 1  # 临时声明k0
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:  # 移动到下一个不相等的元素！！！！！写法，如果相等则需要跳过，移动到下一个不相等的元素！！！！
                        k0 -= 1  # k0更新；
                    k = k0  # 把k0赋值给k;
                else:   #要么移动左指针
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best


"""
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

"""
总结：
官方的解法框架；
（1）首先，对数组进行升序排序，声明结果差初始值，best = 10 ** 7 
（2）其次，声明左右指针，j, k = i + 1, n - 1 ，并计算，当前元素差值： s = nums[i] + nums[j] + nums[k]；如果目标值与s，相等直接返回；如果不等：
（2-1）如果s>target,则移动右指针；移动策略为：
    声明临时变量k0 = k-1
    保证左指针小于右指针，并且相等的跳过: while j < k0 and nums[k0] == nums[k]: 
    k0更新为k0 -= 1 ；
    不满足while条件则退出，将k0赋值为k；
    备注： 为什么要声明一个临时的k0变量，因为k是要作为一个标志变量，判断当前移动的右指针与最开始的是否一致，一致则跳过；因此，是需要保持不变的；除非找到了不一样的下一个元素作为新的右指针
（2-2）如果s<target,则移动左指针；
     思路同上；


"""
if __name__ == '__main__':
    so = Solution()
    # nums = [-3,0,1,2]#
    nums = [0, 2, 1, -3]
    # nums = [-1,0,1,2]
    target = 1
    rst = so.threeSumClosest(nums, target)
    print("rst is ", rst)
