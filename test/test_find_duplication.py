import os
from nose import with_setup
from find_duplication import split_to_lexems, calculate_final_hash, hash_tokens


def calculate_result(file_path):
    f_path = os.path.join(os.getcwd(), file_path)


    f = open(f_path, 'r')
    a = f.read()
    res_a = calculate_final_hash(a)

    return set(res_a)


def compare_2_files(f_path_first, f_path_second):
    f_res = calculate_result(f_path_first)
    s_res = calculate_result(f_path_second)
    return "first source_code contains {0}% of duplication".format(int(round(1.0*len(set(f_res)&set(s_res))/len(set(f_res))*100)))


def test_1():
    "test 1 - test of short code - remove 4 lines of imports"
    print "test 1 - test of short code - remove 4 lines of imports"
    result = compare_2_files('test/code/1_1.txt', 'test/code/1_2.txt')
    print result


def test_2():
    """
    test 2 - similar code
    """
    print "test 2 - similar code"
    result = compare_2_files('test/code/2_1.txt', 'test/code/2_2.txt')
    print result


def test_3():
    """
    test 3 - change position of 2 functions
    """
    print "test 3 - change position of 2 functions"
    result = compare_2_files('test/code/3_1.txt', 'test/code/3_2.txt')
    print result


def test_4():
    """
    test 4 - change name of one variable(7 times)
    """
    print "test 4 - change name of one variable(7 times)"
    result = compare_2_files('test/code/4_1.txt', 'test/code/4_2.txt')
    print result


def test_5():
    """
    test 5 - two different part of code (307 lines)
    """
    print " test 5 - compare two different part of code "
    result = compare_2_files('test/code/5_1.txt', 'test/code/5_2.txt')
    print result


def test_6():
    """
    test 6 - shell sort (change i -> c, j - >b) small code
    """
    print " test 6 - change variables name in short code "
    result = compare_2_files('test/code/6_1.txt', 'test/code/6_2.txt')
    print result


def test_7():
    """
    test 7 - change position of all functions and imports
    """
    print " test 7 - change position of all functions and imports"
    result = compare_2_files('test/code/7_1.txt', 'test/code/7_2.txt')
    print result


def test_8():
    """
    test 8 - one code is longer than the other one
    """
    print " test 8 - first source code is longer than the second one, code is the same"
    result = compare_2_files('test/code/8_1.txt', 'test/code/8_2.txt')
    print result


def test_9():
    """
    test 9 - in bigger code - past small part of previous code
    """
    print " test 9 - the first bigger code contains small part of the second code"
    result = compare_2_files('test/code/9_1.txt', 'test/code/9_2.txt')
    print result


def test_10():
    """
    test 10 - second code contain half of the first code
    """
    print " test 10 - second source code contain half of the first source code"
    result = compare_2_files('test/code/10_1.txt', 'test/code/10_2.txt')
    print result


def test_11():
    """
    test 11 - change variables and function position
    """
    print " test 11 - change variables and function position"
    result = compare_2_files('test/code/11_1.txt', 'test/code/11_2.txt')
    print result


def test_12():
    """
    test 12 - small code, change variable names, function position
    """
    print " test 12 - small code, change variable names, function position"
    result = compare_2_files('test/code/12_1.txt', 'test/code/12_2.txt')
    print result


def test_13():
    """
    test 13 - small code, change variable names, value of number
    """
    print " test 13 - small code, change variable names, value of number"
    result = compare_2_files('test/code/13_1.txt', 'test/code/13_2.txt')
    print result


def test_14():
    """
    test 14 - hello world - change class name, digit vale, func name
    """
    print " test 14 - hello world - change class name, digit vale, func name "
    result = compare_2_files('test/code/14_1.txt', 'test/code/14_2.txt')
    print result


def test_15():
    """
    test 15 - Changed names of variables
    """
    print " test 15 - Changed names of variables"
    result = compare_2_files('test/code/15_1.txt', 'test/code/15_2.txt')
    print result


def test_16():
    """
    test 16 - The same code
    """
    print " test 16 - The same code"
    result = compare_2_files('test/code/16_1.txt', 'test/code/16_2.txt')
    print result


def test_17():
    """
    test 17 - One is a half of another
    """
    print " test 17 - First code contains half of the second code"
    result = compare_2_files('test/code/17_1.txt', 'test/code/17_2.txt')
    print result


def test_18():
    """
    test 18 -  Removed documentation strings and comment
    """
    print " test 18 -  Removed documentation strings and comment"
    result = compare_2_files('test/code/18_1.txt', 'test/code/18_2.txt')
    print result


def test_19():
    """
    test 19 -  Shuffled functions
    """
    print " test 19 -  Shuffled functions"
    result = compare_2_files('test/code/19_1.txt', 'test/code/19_2.txt')
    print result


def test_20():
    """
    test 20 - Small part of code inside another code
    """
    print " test 20 - First code contains part of the second code"
    result = compare_2_files('test/code/20_1.txt', 'test/code/20_2.txt')
    print result


def test_21():
    """
    test 21 - Two approaches to the one problem
    """
    print " test 21 - Two approaches to the one problem. The code is similar"
    result = compare_2_files('test/code/21_1.txt', 'test/code/21_2.txt')
    print result


def test_22():
    """
    test 22 - Different code
    """
    print " test 22 - Different code"
    result = compare_2_files('test/code/22_1.txt', 'test/code/22_2.txt')
    print result


def test_23():
    """
    test 23 -
    """
    print " test 23 - Hello World - short source code with one functionality in the different way of realization"
    result = compare_2_files('test/code/23_1.txt', 'test/code/23_2.txt')
    print result


# def test_24():
#     """
#     test 24 -
#     """
#     print " test 24 - "
#     result = compare_2_files('test/code/24_1.txt', 'test/code/24_2.txt')
#     print result
#
#
# def test_25():
#     """
#     test 25 -
#     """
#     print " test 25 - "
#     result = compare_2_files('test/code/25_1.txt', 'test/code/25_2.txt')
#     print result
#
#
# def test_26():
#     """
#     test 26 -
#     """
#     print " test 26 - "
#     result = compare_2_files('test/code/26_1.txt', 'test/code/26_2.txt')
#     print result






