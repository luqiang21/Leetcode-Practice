def rotate(string, n):
    '''Rotate characters in a string. Expects string and n (int) for
       number of characters to move.

       if n is positive move characters from beginning to end, e.g.:
            rotate('hello', 2) would return 'llohe'

       if n is negative move characters to the start of the string, e.g:
            rotate('hello', -2) would return 'lohel'

       There are many ways to solve this. Which one is most elegant and
       has the best performance (hint: check stdlib)
    '''
    return string[n:] + string[:n]

from collections import deque


def rotate1(string, n):
    '''You can use slicing or collections' deque
       See our article:
       https://pybit.es/collections-deque.html
    '''
    # 1. using slicing
    # return string[n:] + string[:n]

    # 2.  stdlib + better performance
    # Note deque's direction: it rotates n steps to the right.
    # If n is negative, it rotates to the left.
    deq = deque(string)
    deq.rotate(-n)
    return ''.join(deq)



def test_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'

    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) == expected

    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) == expected

def test_rotate1():
    assert rotate1('hello', 2) == 'llohe'
    assert rotate1('hello', -2) == 'lohel'

    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate1(string, 15) == expected

    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate1(string, -15) == expected
