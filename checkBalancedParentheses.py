# -*- coding: utf-8 -*-

'''
Given a string of opening and closing parentheses, check whether it’s balanced.
We have 3 types of parentheses: round brackets: (), square brackets: [],
and curly brackets: {}. Assume that the string doesn’t contain any other character
than these, no spaces words or numbers.
Just to remind, balanced parentheses require every opening parenthesis to be
closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.
'''
'''This is a simple yet common interview question that demonstrates correct use of a stack.
'''

def isBalanced(expr):
    # if the number of parentheses is not even, retur false
    if len(expr)%2 != 0:
        return False

    opening = set('([{')
    match = set([ ('(',')'), ('[',']'), ('{','}') ])
    stack = []

    for char in expr:
        if char in opening:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            lastOpen = stack.pop()
            if (lastOpen, char) not in match:
                return False

    return len(stack) == 0

print(isBalanced('({[]})'))
print(isBalanced('((((((())'))
