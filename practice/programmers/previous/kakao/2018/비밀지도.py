"""
Programmers Template

"""

import unittest


def solution(n, arr1, arr2):
    result_array = list()
    arr1_string = get_binary_array(n, arr1)
    arr2_string = get_binary_array(n, arr2)
    for i in range(0, n):
        result_array.append(compare_string(n, arr1_string[i], arr2_string[i]))
    return result_array


def get_binary(n, value):
    return format(value, '0' + str(n) + 'b')


def get_binary_array(n, arr):
    result_array = []
    for v in arr:
        result_array.append(get_binary(n, v))
    return result_array


def compare_string(n, str1, str2):
    result = ""
    for i in range(0, n):
        if str1[i] == "1" or str2[i] == "1":
            result = result + "#"
        else:
            result = result + " "
    return result

class ProgrammersTest(unittest.TestCase):

    def testSolution1(self):
        n = 5
        arr1 = [9, 20, 28, 18, 11]
        arr2 = [30, 1, 21, 17, 28]
        result = solution(n, arr1, arr2)
        self.assertEqual(result, ["#####", "# # #", "### #", "#  ##", "#####"])

    # def testSolution2(self):
    #     a = ""
    #     b = ""
    #     result = solution(a, b)
    #     self.assertEqual(result, "")
    #
    # def testSolution3(self):
    #     a = ""
    #     b = ""
    #     result = solution(a, b)
    #     self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
