'''
Award Budget Cuts
The awards committee of your alma mater (i.e. your college/university) asked for
your assistance with a budget allocation problem they’re facing. Originally, the
committee planned to give N research grants this year. However, due to spending
cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate
the grants. The committee made a decision that they’d like to impact as few grant
recipients as possible by applying a maximum cap on all grants. Every grant initially
planned to be higher than cap will now be exactly cap dollars. Grants less or equal
to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget,
write a function findGrantsCap that finds in the most efficient manner a cap such
that the least number of recipients is impacted and that the new budget constraint
is met (i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.

Example:

input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
Constraints:

[time limit] 5000ms

[input] array.double grantsArray

0 ≤ grantsArray.length ≤ 20
0 ≤ grantsArray[i]
[input] double newBudget

[output] double



'''
from tools import timing
@timing
def find_grants_cap1(grantsArray, newBudget):
    n = len(grantsArray)
    grantsArray.sort()
    end = None
    for i in range(n-1):
      if sum(grantsArray[:i]) + grantsArray[i] * (n-i) < newBudget and sum(grantsArray[:i+1]) + grantsArray[i+1] * (n-i-1) > newBudget:
        end = i+1
    if end == None:
      return newBudget / float(n)
    if end == n:
      return grantsArray[-1]
    cap = (newBudget - sum(grantsArray[:end])) / float(n-end)
    return cap

@timing
def find_grants_cap2(grantsArray, newBudget):
    n = len(grantsArray)
    grantsArray.sort(reverse=True)
    # pad the array with a zero at the end to
    # cover the case where 0 <= cap <= grantsArray[i]
    grantsArray.append(0)

    # calculate the total amount we need to
    # cut back to meet the reduced budget
    surplus = sum(grantsArray) - newBudget

    # if there is nothing to cut, simply return
    # the highest grant as the cap. Recall that
    # the grants array is sorted in a descending
    # order, so the highest grant is positioned
    # at index 0
    if surplus <= 0:
        return grantsArray[0]

     # start subtracting from surplus the
    # differences (“deltas”) between consecutive
    # grants until surplus is less or equal to zero.
    # Basically, we are testing out, in order, each
    # of the grants as potential lower bound for
    # the cap. Once we find the first value that
    # brings us below zero we break
    for i in range(n):
        surplus -= (i+1) * (grantsArray[i] - grantsArray[i+1])
        if (surplus <= 0):
            break

    # since grantsArray[i+1] is a lower bound
    # to our cap, i.e. grantsArray[i+1] <= cap,
    # we  need to add to grantsArray[i+1] the
    # difference: (-total / float(i+1), so the
    # returned value equals exactly to cap.
    return grantsArray[i+1] + (-surplus / float(i+1))
arr = [2,4]
b = 3
print(find_grants_cap1(arr,b))
print(find_grants_cap2(arr,b))
arr = [21,100,50,120,130,110]
b = 140
print(find_grants_cap1(arr,b))
print(find_grants_cap2(arr,b))
