# Problem: https://leetcode.com/problems/valid-parentheses/description/

from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        # s must have an even number of characters to be valid
        if len(s) % 2 == 1:
            return False

        stack = deque()
        for character in s:
            # If character is an open bracket- i.e. '(', '{' ,or '['- push it into stack
            if character == '(' or character == '{' or character == '[':
                stack.append(character)
            else: 
                # If character is a closed bracket- i.e. ')', '}', or ']', try to pop its
                # open counterpart from the stack.
                if len(stack) == 0: # if stack is empty
                    return False
                popped = stack.pop()
                if (character == ')' and not popped == '(') or (character == '}' and not popped == '{') or (character == ']' and not popped == '['):
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
