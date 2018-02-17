'''
An item in a list A of size n is said to be pervasive if it appears in A more than
n/2 times. For example, element 4 is pervasive in [3,2,4,3,4,4,2,4,4], whereas
[3,2,4,3,4,4,2,4] does not have a pervasive number. Your job is to design an
efficient algorithm to determine if a list has a pervasive element, and if so,
to find the element.
'''
def find_pervasive(input):
    """ Divide """
    if(len(input) == 0):
        return []
    if(len(input) == 1):
        return [[(input[0], 1)], input[0]]
    left   = find_pervasive(input[:len(input)//2])
    right  = find_pervasive(input[len(input)//2:])
    print(left, right)

    left_list, p_left = left
    right_list, p_right = right
    """ Conquer """
    result_list = []
    i=0
    j=0
    imax=len(left_list)
    jmax=len(right_list)
    while(i<imax and j<jmax):
        if(left_list[i][0] < right_list[j][0]):
            result_list.append(left_list[i])
            i = i+1
        elif(left_list[i][0] > right_list[j][0]):
            result_list.append(right_list[j])
            j = j+1
        else:
            result_list.append((left_list[i][0], left_list[i][1]+right_list[j][1]))
            i = i+1
            j = j+1
    while(i<imax):
        result_list.append(left_list[i])
        i = i+1;
    while(j<jmax):
        result_list.append(right_list[j])
        j = j+1;

    p = None
    if p_left == p_right and p_left is not None:
        p = p_left
    elif p_left != p_right and (p_left is None or p_right is None):
        # go through result_list, find p
        for n, cnt in result_list:
            if cnt > len(input) // 2:
                p = n
                break

    result = [result_list, p]
    return result
print('The pervasive number is', find_pervasive([3,2,4,3,4,4,2,4,4])[1])
print()
print('The pervasive number is', find_pervasive([3,2,4,3,4,4,2,4])[1])
