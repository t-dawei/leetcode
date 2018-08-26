'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        # 感觉有些写复杂了
        """
        def count_and_saying(string):
            index, count = 0, 0
            cur_s, new_str = '', ''
            
            while True:
                s = string[index]
                if not cur_s:
                    cur_s = s
                    count = 1
                else:
                    if cur_s == s:
                        count += 1
                    else:
                        new_str += str(count) + cur_s
                        cur_s = s
                        count = 1
                index += 1
                if index == len(string):
                    new_str += str(count) + cur_s
                    break
            return new_str
        
        index, string = 1, '1'
        while index < n:
            string = count_and_saying(string)
            index += 1
        return string


#简短容易理解
def countAndSay(self, n):
    result = '1'
    for _ in range(n-1):
        prev = result
        result = ''
        j = 0
        while j < len(prev):
            cur = prev[j]
            cnt = 1
            j += 1
            while j < len(prev) and prev[j] == cur:
                cnt += 1
                j += 1
            result += str(cnt) + str(cur)
    return result



# 其他简短代码 
# 利用正则 仅日后参考 
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s


# 利用groupby
# 功能刚好适合
def countAndSay(n):
    result = "1"
    for _ in range(n - 1):
        # original
        # s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        
        # decomposed
        v = '' # accumulator string
        # iterate the characters (digits) grouped by digit
        for digit, group in itertools.groupby(result):
            count = len(list(group)) # eg. the 2 in two 1s 
            v += "%i%s" % (count, digit) # create the 21 string and accumulate it
        result = v # save to result for the next for loop pass

    # return the accumulated string
    return result