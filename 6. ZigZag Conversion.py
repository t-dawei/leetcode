'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		思路：
			画图 找规律
			0   4   8
			1 3 5 7 9
			2   6
		"""
		new_s = ''
		def helper(s, x1, x2, cur):
			string = ''
			if not x1 or not x2:
				x1 = x2 = x1 + x2
				if x1 == x2 == 0:
					return s
			if cur < len(s):
				string += s[cur]
				interval = x1
				while cur + interval < len(s) and interval:
					cur += interval
					string += s[cur]
					interval = (x1, x2)[interval == x1]
			print(string)
			return string

		for i in range(numRows):
			x1 = 2 * (numRows - 1 - i)
			x2 = 2 * (numRows - 1) - x1
			new_s += helper(s, x1, x2, i)
		print(new_s)
		return new_s

if __name__ == '__main__':
	Solution().convert('A', 1)