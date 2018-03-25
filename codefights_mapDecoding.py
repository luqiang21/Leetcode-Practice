"""
A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent and you need to determine the total number of ways that the message can be decoded.

Since the answer could be very large, take it modulo 109 + 7.

Example

For message = "123", the output should be

mapDecoding(message) = 3.

"123" can be decoded as "ABC" (1 2 3), "LC" (12 3) or "AW" (1 23), so the total number of ways is 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string message

A string containing only digits.

Guaranteed constraints:

0 ≤ message.length ≤ 105.

[output] integer

The total number of ways to decode the given message.


"""

from tools import timing
@timing
def mapDecoding1(message):
    n = len(message)
    ways = [1, 1]
    if len(message) > 0 and message[0] == "0":
        return 0
    if n < 2:
        return ways[n]


    for i in range(2, n+1):
        temp = 0
        if int(message[i-1]) != 0:
            temp += ways[i-1]
        if 10 <= int(message[i-2:i]) <= 26:
            temp += ways[i-2]
        ways.append(temp)
    return ways[n] % (10**9 + 7)

@timing
def mapDecoding(message):
    n = len(message)
    a, b = [1, 1]
    if len(message) > 0 and message[0] == "0":
        return 0
    if n < 2:
        return 1

    for i in range(2, n+1):
        c = 0
        if int(message[i-1]) != 0:
            c += b
        if 10 <= int(message[i-2:i]) <= 26:
            c += a
        a = b
        b = c
    return c  % (10**9 + 7)

message = "2871221111122261"
ans = 233

assert mapDecoding1(message) == ans
assert mapDecoding(message) == ans
