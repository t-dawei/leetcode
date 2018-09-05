'''
从正整数 N 开始，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

 

示例 1：

输入：1
输出：true
示例 2：

输入：10
输出：false
示例 3：

输入：16
输出：true
示例 4：

输入：24
输出：false
示例 5：

输入：46
输出：true
 

提示：

1 <= N <= 10^9
'''
# 方法1：超时
class Solution:
	def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        def perm(s):
            if len(s) == 1:
                return [s]
            list_string = []
            for x in range(len(s)):
                for j in perm(s[:x] + s[x+1:]):
                    list_string.append(s[x] + j)
            return list_string
        
        def power2(data):
            res = data & (data-1)
            return res == 0
        
        list_string = list(set(perm(str(N))))
        for s in list_string:
            if not s.startwith('0') and power2(int(s)):
                return True
        else:
            return False

# 方法2：
# 既然可以任意组合 说明该算法并不注重组合的结果 而是里面元素的种类和个数
import collections
# 不用collections 也是可以
def reorderedPowerOf2(self, N):
	c = collections.Counter(str(N))
	# pow(2, 32) 为10位数
	for x in range(32):
		string = str(1 << x)
		if c == collections.Counter(string):
			return True
	else:
		return False

# 方法3：
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        all_possible = [2**i for i in range(30)]    
        for i in all_possible:
        	# 这里看时很困惑 查了下资料 原来set是无序的 不同于list 例如set(1, 2) == set(2, 1)
            if set(str(N)) == set(str(i)) and len(str(N)) == len(str(i)):
                return True
        return False