"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def minDistance(self, word1, word2):
    #m,n 表示两个字符串的长度
    m=len(word1)
    n=len(word2)
    #构建二维数组来存储子问题
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    #考虑边界条件，第一行和第一列的条件
    for i in range(n+1):
        dp[0][i]=i  #对于第一行，每次操作都是前一次操作基础上增加一个单位的操作
    for j in range(m+1):
        dp[j][0]=j #对于第一列也一样，所以应该是1,2,3,4,5...
    for i in range(1,m+1):  #对其他情况进行填充
        for j in range(1,n+1):
            if word1[i-1]==word2[j-1]: #当最后一个字符相等的时候，就不会产生任何操作代价，所以与dp[i-1][j-1]一样
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1 #分别对应删除，添加和替换操作
    return dp[-1][-1] #返回最终状态就是所求最小的编辑距离
