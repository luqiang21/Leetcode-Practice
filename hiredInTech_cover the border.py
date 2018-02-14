"""
Air traffic control of one country wants to check how well its radars are
covering the border. There are plenty of radars each covering one contiguous
strip of the border. Some radars' coverage strips overlap. Because of the numerous
overlaps it is hard for the air traffic control managers to compute the exact
length of the border that is covered. This will be your task.

The strip is represented as a line, which is L meters long.

For each radar we know the left and right end of its coverage strip relative to
the left end of the border. Hence, all such coverage strips will begin and end
somewhere in the range [0, L], which means they fall completely within the border.
They will also have an integer length of at least 1.

You will have to write a function, which receives as arguments L and a list of
pairs of integers - the radar coverage strips ends. Your function must return one
 integer - the total area of the border that is covered by at least one radar, in meters.

You can assume that 1 <= L <= 10^9 and there will be no more than 1,000 radars.

SAMPLE INPUT

L = 100
radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
SAMPLE OUTPUT

77
In the sample input the border is 100 meters long and there are 5 radars covering
parts of it. Effectively there are three areas of the border that are completely
covered by at least one radar:

3 to 25, which includes in itself the area between 5 and 10 covered by another radar
39 to 40, which is covered by a single radar
45 to 99, which is the combined coverage of two radars with coverage [45, 50] and [46, 99]
"""

from tools import timing

@timing
def cover_the_border1(l, radars):
  # merge radar ranges

  if len(radars) <= 1:
      return radars[0][1] - radars[0][0]
  merged = []
  radars.sort()
  p_left, p_right = radars[0]
  for i in range(1, len(radars)):
      c_left, c_right = radars[i]

      if c_left > p_right:
          # store last separated range
          merged.append([p_left, p_right])
          p_left, p_right = c_left, c_right
      else:
          if c_right > p_right:
              p_right = c_right

  merged.append([p_left, p_right])

  coverage = 0
  # sum ranges

  for left, right in merged:
      coverage += right - left
  return coverage

# same idea with mine, better format
@timing
def cover_the_border(l, radars):
  # Example arguments:

  # l = 100

  # radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]

  prev = None
  radars.sort()
  ans = 0
  for radar in radars:
      if not prev:
          prev = radar[:]
      elif radar[0] > prev[1]:
          # separate from previous ranges

          ans += prev[1] - prev[0]
          prev = radar[:]
      else:
          prev[1] = max(prev[1], radar[1])
  if prev:
      ans += prev[1] - prev[0]
  return ans

l = 100
radars = [[5, 10], [3, 25], [46, 99], [39, 40], [45, 50]]

assert cover_the_border1(l, radars) == 77
assert cover_the_border(l, radars) == 77
