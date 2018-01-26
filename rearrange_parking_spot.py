"""
Rearrange parking lots

There are N+1 parking spots, numbered from 0 to N. There are N cars numbered
from 1 to N parked in various parking spots with one left empty. Reorder the
cars so that car #1 is in spot #1, car #2 is in spot #2 and so on. Spot #0
will remain empty. The only allowed operation is to take a car and move it
to the free spot.
"""

import unittest
import random

class TestParking(unittest.TestCase):
    """unit test"""
    def test(self):
        """test"""
        self.assertEqual(park_cars([0, 3, 4, 5, 2, 1], 6), [0, 1, 2, 3, 4, 5])
        self.assertEqual(park_cars([3, 1, 2, 0, 4, 5], 6), [0, 1, 2, 3, 4, 5])
        self.assertEqual(park_cars([0], 1), [0])
        self.assertEqual(park_cars([], 0), [])
        with self.assertRaises(AssertionError):
            park_cars([1], [1])
            park_cars([1, 4, 5], 3)
            park_cars([0, 0, 0], 3)
            park_cars([-1, -2, 3], 2)
            park_cars([3, 2, 1, 0], 4)
            park_cars([0, 0, 1, 4], 4)
            park_cars([0, 0], 2)


def park_cars(parking_lot, n):
    """
    Args:
        parking_lot: list of integers
        n: length of parking_lot
    Returns:
        arranged parking_lot
    """

    assert len(parking_lot) == n, "Error, n does not equal the length of parking_lot."

    if n < 2:
        return parking_lot

    assert max(parking_lot) == len(parking_lot) - 1 and min(parking_lot) == 0,\
    "Error: parking lot should be 0 -> n"
    assert len(set(parking_lot)) == n, "Error: only unique value from 0 to n allowed."+str(len(set(parking_lot)) )

    # obtain the initial index of empty spot
    es = parking_lot.index(0)
    # get the number of already ordered spots
    ordered = sum([1 for j in range(1, n) if j == parking_lot[j]])

    steps = 0
    while ordered != n - 1:
        steps += 1
        print("step:", steps)
        # if the empty spot is not at index 0
        if es:
            # find the index of the car to swap, which is the value in index es
            sc = parking_lot.index(es)
            parking_lot[sc], parking_lot[es] = parking_lot[es], parking_lot[sc]
            ordered += 1
            # now the empty spot is at sc
            es = sc

        else:
            # es = 0
            for j in range(1, n):
                if j != parking_lot[j]:
                    parking_lot[j], parking_lot[es] = parking_lot[es], parking_lot[j]
                    es = j
                    break
    return parking_lot


if __name__ == '__main__':
    # unittest.main()
    n = 10
    parking_lot = list(range(n+1))
    random.shuffle(parking_lot)
    print ('Parking lot start : %s' % ' '.join([str(i) for i in parking_lot]))
    parking_lot = park_cars(parking_lot, n + 1)
    print ('Parking lot end   : %s' % ' '.join([str(i) for i in parking_lot]))
