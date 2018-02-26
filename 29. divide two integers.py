'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

# Function to divide a by b and
# return floor value it
def divide(dividend, divisor):

    # Calculate sign of divisor i.e.,
    # sign will be negative only iff
    # either one of them is negative
    # otherwise it will be positive
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1

    # Update both divisor and
    # dividend positive
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1


    return sign * quotient


def divide1(dividend, divisor):
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = temp = 0

    # test down from the highest bit and
    # accumulate the tentative value for
    # valid bit
    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient += 1 << i #  or  quotient |= 1 << i

    return sign * quotient


# Driver code
a = 10
b = 3
print(divide(a, b))
print(divide1(a, b))
print()

a = 43
b = -8
print(divide(a, b))
print(divide1(a, b))
print()s

a = 999
b = 9
print(divide(a, b))
print(divide1(a, b))
