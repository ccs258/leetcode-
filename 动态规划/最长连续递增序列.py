"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def solution(input):
    """
    解法有误：忽略了关联性
    """
    max_lenth = 0
    lenth = len(input)
    start  = 0
    dp = [[False for i in range(lenth)] for j in range(lenth)]
    dp[0][0] = True
    for j in range(1,lenth):
        for i in range(j):
            if input[j] > input[i]:
                if j-i == 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]  #这个忽略了相邻元素的关联性大小

            if dp[i][j]:
                lenth = j-i+1
                if lenth > max_lenth:
                    max_lenth = lenth
                    start = i

    return input[start:start+max_lenth]


def solution_2(input):
    length = len(input)
    dp = [[1 for i in range(length)] for i in range(length)]
    for  i  in range(length):
        if input[i]>input[i-1]:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = 1
    return max(dp)
"""
思路总结：
（1）数组元素设计；比较巧妙地设计了一个数组dp，其元素值即为结果，初始的连续值长度1；
（2）更新数组元素；一层循环，遍历数组，如果相邻的元素满足递增，则当前dp[i]更新为dp[i-1]+1
 (3)对所有连续的元素长度求最大，即得到结果

"""

"""


"""
if __name__ == '__main__':
    input = [1,3,5,4,7]
    rst = solution(input)
    print("rst is ",rst)