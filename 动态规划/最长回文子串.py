"""
题目描述：
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

回文串（palindromic string）是指这个字符串无论从左读还是从右读，所读的顺序是一样的；
"""
def solution(string):
    length = len(string)
    dp = [[False for i in range(length)] for i in  range(length)]
    if length < 2:
        return string
    max_len = 1
    start = 0
    for j in range(1,length): #原来是range(0,length-1)，这样写不对;另外注意j是外层循环，比较大的那一层
        for i in range(0,j):
            if string[i] == string[j]:
                if j-i < 3: #if j-i == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return string[start:start+max_len]
"""
###思路总结
（1）定义二维数组dp[i][j]，表示字符串string[i:j]，左闭右开的取值范围取到的子字符串是否是回文子串；
（2）更新dp[i][j]；对字符串定义两层循环，外层遍历分别作为子串的最终位置j，基于外层遍历的基础再做一层内层循环，相当于是子串的起始位置i；
设计逻辑判断回文：如果子串最终位置字符string[j]==子串起始位置字符string[i]：if j-i<3,则返回TRUE；否则返回dp[i+1][j-1],这里会起到连环更新dp的效果（因为两层循环，终会把所有最内层的子串情况全部遍历计算完）；
（3）根据所有得到的回文子串--if dp[i][j]:，计算出最大长度对应的回文子串；

"""
if __name__ == '__main__':
    string = "babad"
    so = solution(string)
    print("rst is ",so)



