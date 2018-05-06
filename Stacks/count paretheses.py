class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        temp = 0
        stack = []
        stack.append("$")
        for i in xrange(0, len(s)):
          
            if s[i] == "(" :
                stack.append(s[i])
            if s[i] == ")" and stack[len(stack)-1] == "(" :
                stack.pop()
                count = max(count, i - len(stack)-1)
        
        return count

obj = Solution()
print obj.longestValidParentheses("(((())))")