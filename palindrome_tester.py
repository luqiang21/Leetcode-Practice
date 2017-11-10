import importlib
from tools import timing
@timing
def is_palindrome(input_string):
    if input_string == '':
        return True
    length = len(input_string)
    if length%2 == 0:
        # the string has even number of characters
        return input_string[:length/2] == input_string[length/2::-1]
    else:
        # the string has odd number of characters
        mid = (length - 1) / 2
        print (input_string[:mid], input_string[mid+1::-1])
        return input_string[:mid] == input_string[mid+1::-1]


print(is_palindrome("madam"))# -> True

print(is_palindrome("aabb"))# -> False

print(is_palindrome("race car"))# -> False

print(is_palindrome(""))# -> True

# answer from firecode.io
@timing
def is_palindrome1(input_string):
    result = True
    str_len = len(input_string)
    for i in range(0, int(str_len/2)):
        if input_string[i] != input_string[str_len-i-1]:
            result = False
            break
    return result

print(is_palindrome1("race car"))# -> False

# the shortest version
@timing
def is_palindrome2(input_string):
    return input_string == input_string[::-1]

print(is_palindrome("madam"))# -> True
print(is_palindrome1("madam"))# -> True
print(is_palindrome2("madam"))# -> True

print(is_palindrome("race car"))# -> False
print(is_palindrome1("race car"))# -> False
print(is_palindrome2("race car"))# -> False
