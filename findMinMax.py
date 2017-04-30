'''Recursion Solution for finding minimum and maximum problem'''
from random import randint

def getLarger(a, b):
	if b > a:
		return b
	else:
		return a


def getSmaller(a, b):
	if b < a:
		return b
	else:
		return a


def findMinMax(array, length):
	Min = array[0]
	Max = array[0]

	return findMinMaxHelper(array, 0, length, Min, Max)

def findMinMaxHelper(array, start, end, Min, Max):
	# base cases
	if start == end:
		Min = array[start]
		Max = Min
		return Min, Max

	elif start == end - 1:
		Min = getSmaller(array[start], array[end])
		Max = getLarger(array[start], array[end])
		return Min, Max
	
	else:
	# general cases
		mid = (start + end) // 2
		MinL, MaxL = findMinMaxHelper(array, start, mid, Min, Max)
		MinR, MaxR = findMinMaxHelper(array, mid+1, end, Min, Max)
		
		Min = getSmaller(MinL, MinR)
		Max = getLarger(MaxL, MaxR)
		return Min, Max

def main():
	array = list()
	length = 10
	for x in range(0, length):
		array.append(randint(0, length))
	print array

	Min, Max = findMinMax(array, length-1)
	print Min, Max

if __name__ == "__main__":
	main()
