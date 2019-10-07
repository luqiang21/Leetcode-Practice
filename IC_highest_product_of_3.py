"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""

from tools import timing
@timing
def highest_product_of_3(list_of_ints):
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    highest_num = max(list_of_ints[:2])
    lowest_num = min(list_of_ints[:2])
    highest_so_far = highest_product_of_2 * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        # update highest_so_far
        current = list_of_ints[i]

        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_so_far= max(highest_so_far,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        # Do we have a new highest product of two?
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest_num,
                                   current * lowest_num)

        # Do we have a new lowest product of two?
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest_num,
                                  current * lowest_num)

        # Do we have a new highest?
        highest_num = max(highest_num, current)

        # Do we have a new lowest?
        lowest_num = min(lowest_num, current)

    return highest_so_far




list_of_ints = [1, 10, -5, 1, -100]
assert highest_product_of_3(list_of_ints) == 5000
a = [-10,-10,1,3,2]
assert highest_product_of_3(a) == 300
a = [-1, -2, -3]
assert highest_product_of_3(a) == -6
