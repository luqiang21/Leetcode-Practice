"""
Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function
getShortestUniqueSubstring that finds the smallest substring of str containing
all the characters in arr. Return "" (empty string) if such a substring doesn’t
exist.

Come up with an asymptotically optimal solution and analyze the time and space
complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
Constraints:

[time limit] 5000ms

[input] array.character arr

1 ≤ arr.length ≤ 30
[input] string str

1 ≤ str.length ≤ 500
[output] string


"""
from tools import timing
# my answer
@timing
def get_shortest_unique_substring1(arr, str):
    # O(n^2*m)
    if len(str) < len(arr):
        return ""
    res = ""
    for i in range(len(str) - len(arr)+1):
        for j in range(i+len(arr), len(str)+1):
            sub = str[i:j]
            flag = True
            # print(arr, sub)
            # since arr has unique elements
            for ch in arr:
                if ch not in sub:
                     flag = False
            if flag:
                if len(res) == 0 or len(res) > len(sub):
                    res = sub
                break
    return res

# solution from peer in the pramp interview
@timing
def get_shortest_unique_substring2(arr, str):
    if len(str) < len(arr):
            return ""
    d = dict()
    for y in arr:
        d[y] = []
    missing = list(arr)

    start = 0
    end = len(str)

    for i in range(len(str)):
        if str[i] in arr:
            if str[i] not in missing and d[str[i]] != []:
                d[str[i]].pop(0)
            elif str[i] in missing:
                missing.remove(str[i])
            d[str[i]].append(i)

        if missing == []:
            maximum = max(i[-1] for i in d.values())
            minimum = min(i[0] for i in d.values())
            if maximum - minimum + 1 < end - start + 1:
                start = minimum
                end = maximum

    if missing != []:
        return ""
    else:
        return str[start: end + 1]

# solution from pramp
@timing
def get_shortest_unique_substring(arr, string):
    head_index = 0
    result = ""
    unique_counter = 0
    count_dic = {}

    # initialize dic
    for i in range(len(arr)):
        count_dic[arr[i]] = 0
    # scan str
    for tail_index in range(len(string)):
        # handle the new tail
        tail_char = string[tail_index]

        # skip all the chars not in arr
        if tail_char not in count_dic:
            continue

        tail_count = count_dic[tail_char]
        if tail_count == 0:
            unique_counter += 1

        count_dic[tail_char] = tail_count + 1

        # push head forward
        while unique_counter == len(arr):
            temp_length = tail_index - head_index + 1
            if temp_length == len(arr):
                return string[head_index:tail_index+1]

            if result == "" or temp_length < len(result):
                result = string[head_index:tail_index+1]

            head_char = string[head_index]

            if head_char in count_dic:
                head_count = count_dic[head_char] - 1
                if head_count == 0:
                    unique_counter -= 1
                count_dic[head_char] = head_count

            head_index += 1
    return result

arr = ['x','y','z']
str = "xyyzyzyx"
ans = "zyx"
assert get_shortest_unique_substring1(arr, str) == ans
assert get_shortest_unique_substring2(arr, str) == ans
assert get_shortest_unique_substring(arr, str) == ans


arr = ["x","y","z","r"]
str = "xyyzyzyx"
ans = ""
assert get_shortest_unique_substring1(arr, str) == ans
assert get_shortest_unique_substring2(arr, str) == ans
assert get_shortest_unique_substring(arr, str) == ans
