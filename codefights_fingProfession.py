
from tools import timing

# my naive solution
@timing
def findProfession1(level, pos):
    if level == 1:
        return "Engineer"
    i = 1
    parents = ["Engineer"]
    while i <= level:
        new_parents = []
        for p in parents:
            if p == "Engineer":
                new_parents.append("Engineer")
                new_parents.append("Doctor")
            else:
                new_parents.append("Doctor")
                new_parents.append("Engineer")
        parents = new_parents
        i += 1
    return parents[pos-1]

# after some time, I came out this better solution
import math
@timing
def findProfession2(level, pos):
    if level == 1:
        return "Engineer"

    parent_pos = math.ceil(pos / 2)
    if findProfession2(level - 1, parent_pos) == "Engineer":
        if pos % 2 == 1:
            return "Engineer"
        else:
            return "Doctor"
    else:
        if pos % 2 == 0:
            return "Engineer"
        else:
            return "Doctor"


# solution from others, using characteristics of Thue–Morse sequence
@timing
def findProfession(level, pos):
    """
    Level 1: E
    Level 2: ED
    Level 3: EDDE
    Level 4: EDDEDEED
    Level 5: EDDEDEEDDEEDEDDE

    Level input is not necessary because first elements are the same
    The result is based on the count of 1's in binary representation of position-1
    If count is even, then Engineer; Else Doctor
    """
    bits  = bin(pos-1).count('1')
    if bits%2 == 0:
        return "Engineer"
    else:
        return "Doctor"

level = 17
pos = 5921
ans = "Doctor"
assert findProfession1(level, pos) == ans
assert findProfession2(level, pos) == ans
assert findProfession(level, pos) == ans
print()

level = 30
pos = 163126329
# assert findProfession1(level, pos) == ans
assert findProfession2(level, pos) == ans
assert findProfession(level, pos) == ans
