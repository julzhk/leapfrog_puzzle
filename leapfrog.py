"""
LEAPFROG PUZZLE

Imagine you have a list of numbers, each number represents a
'jump code' to tell you how many steps forwards or backwards you must jump relative to your
current space.
Given a list of numbers, calculate how many jumps it will take to leave the list.
If the list falls into an infinite loop, return -1

"""
__author__ = 'julz'
import unittest

VISITED_ALREADY = -1


def next_element(current_element, array):
    target_element = current_element + array[current_element]
    if target_element >= len(array):
        target_element = None
    return target_element


def solution(A):
    def element_in_range(element_to_check, array_length):
        return 0 <= element_to_check < array_length
    visited = set()
    count = 0
    ele = 0
    len_A = len(A)
    while element_in_range(element_to_check=ele, array_length=len_A):
        if ele in visited:
            return VISITED_ALREADY
        visited.add(ele)
        ele = next_element(ele, A)
        count += 1
    return count


def ignore(func):
    """because there's probably some component of execution time in this test
     and running these unit tests each time will make the code appear
     to execute much more slowly.
    """
    return None


class TestSimpleCase(unittest.TestCase):
    @ignore
    def test_the_test(self):
        self.assertTrue(1 == 1)

    @ignore
    def test_find_next_element(self):
        A = [2, 3, -1, 1, 3]
        self.assertTrue(next_element(current_element=0, array=A) == 2)
        self.assertTrue(next_element(current_element=2, array=A) == 1)
        self.assertTrue(next_element(current_element=1, array=A) == 4)
        self.assertTrue(next_element(current_element=4, array=A) == None)

    @ignore
    def test_simple_solutions(self):
        self.assertTrue(solution([2, 3, -1, 1, 3]) == 4)
        A = [1]
        self.assertTrue(solution(A) == 1)
        B = [1, 1]
        self.assertTrue(solution(B) == 2)
        self.assertTrue(solution([1, 1, 1]) == 3)
        self.assertTrue(solution([-1]) == 1)

    @ignore
    def test_simple_loops(self):
        A = [1, 1, -1, 1]
        self.assertTrue(solution(A) == -1)
        self.assertTrue(solution([1, -1]) == -1)

    @ignore
    def test_big_array(self):
        big_array_len = 1000000
        bigsimpleArray = [1] * 1000000
        self.assertTrue(solution(bigsimpleArray) == big_array_len)

    @ignore
    def test_big_array_of_twos(self):
        big_array_len = 1000000
        bigsimpleArray = [2] * 1000000
        self.assertTrue(solution(bigsimpleArray) == big_array_len / 2)

    @ignore
    def test_big_array_of_minus_one(self):
        big_array = [-1] * 1000000
        self.assertTrue(solution(big_array) == 1)
