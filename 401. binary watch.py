"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the
6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid,
it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for
example "10:2" is not valid, it should be "10:02".
"""
from tools import timing

class Solution:
    @timing
    def readBinaryWatch1(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        if num > len(hours) + len(minutes):
            return []
        temp = [0, 0] # hours, minutes
        res = []
        self.backtrack(res, hours+minutes, 0, 0, 0, num)

        return res

    def backtrack(self, res, leds, hour, minute, idx, n):
        if n == 0:

            if minute < 10:
                res.append(str(hour) + ":0" + str(minute))
            else:
                res.append(str(hour) + ":" + str(minute))
        elif n > 0 and idx < len(leds):
            if idx < 4 and hour + leds[idx] < 12:
                self.backtrack(res, leds, hour + leds[idx], minute, idx + 1, n - 1)
            elif idx > 3 and minute + leds[idx] < 60:
                self.backtrack(res, leds, hour, minute + leds[idx], idx + 1, n - 1)

            self.backtrack(res, leds, hour, minute, idx + 1, n)

    @timing
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        timecode = [0] * 10
        self.dfs(timecode, 0, 0, res, num)

        return res

    def dfs(self, timecode, i, k, res, num):
        if k == num:
            time = self.decodetime(timecode)
            if time:
                res.append(time)
            return
        if i == len(timecode): return
        timecode[i] = 1
        self.dfs(timecode, i + 1, k + 1, res, num)
        timecode[i] = 0
        self.dfs(timecode, i + 1, k, res, num)

    def decodetime(self, timecode):
        hours, minutes = 0, 0
        for i in range(4):
            if timecode[i]:
                hours += int(pow(2, i))
        for i in range(4, 10):
            if timecode[i]:
                minutes += int(pow(2, i-4))

        m = "" + str(minutes)
        if minutes < 10:
            m = "0" + m
        if hours > 11 or minutes > 59:
            return None
        return str(hours) + ":"+m

num = 1
ans = ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
print(Solution().readBinaryWatch1(num))
assert Solution().readBinaryWatch(num) == ans
