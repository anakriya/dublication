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
    return 1.0*len(set(f_res)&set(s_res))/len(set(f_res))


def test_1():
    "test 1 - test of small part of code - remove 4 of imports (21 lines)"
    print "test 1 - test of small part of code - remove 4 of imports (21 lines)"
    result = compare_2_files('test/code/1_1.txt', 'test/code/1_2.txt')
    print result


def test_2():
    """
    test 2 - similar code (880 lines)
    """
    print "test 2 - similar code (880 lines)"
    result = compare_2_files('test/code/2_1.txt', 'test/code/2_2.txt')
    print result


def test_3():
    """
    test 3 - change position of 2 functions (880 lines)
    """
    print "test 3 - change position of 2 functions (880 lines)"
    result = compare_2_files('test/code/3_1.txt', 'test/code/3_2.txt')
    print result


def test_4():
    """
    test 4 - change name of one variable(7 times) (297 lines)
    """
    print "test 4 - change name of one variable(7 times) (297 lines)"
    result = compare_2_files('test/code/4_1.txt', 'test/code/4_2.txt')
    print result


def test_5():
    """
    test 5 - two different part of code (307 lines)
    """
    print " test 5 - two different part of code (307 lines)"
    result = compare_2_files('test/code/5_1.txt', 'test/code/5_2.txt')
    print result


def test_6():
    """
    test 6 - shell sort (change i -> c, j - >b) small code (18 lines)
    """
    print " test 6 - shell sort (change i -> c, j - >b) small code (18 lines)"
    result = compare_2_files('test/code/6_1.txt', 'test/code/6_2.txt')
    print result


def test_7():
    """
    test 7 - change position of all functions and imports (143 lines)
    """
    print " test 7 - change position of all functions and imports (143 lines)"
    result = compare_2_files('test/code/7_1.txt', 'test/code/7_2.txt')
    print result


def test_8():
    """
    test 8 - one code is longer than the other one (241)
    """
    print " test 8 - one code is longer than the other one (241)"
    result = compare_2_files('test/code/8_1.txt', 'test/code/8_2.txt')
    print result


def test_9():
    """
    test 9 - in bigger code - past small part of previous code (130 lines)
    """
    print " test 9 - in bigger code - past small part of previous code (130 lines)"
    result = compare_2_files('test/code/9_1.txt', 'test/code/9_2.txt')
    print result


def test_10():
    """
    test 10 - second code contain half of the first code (91 lines)
    """
    print " test 10 - second code contain half of the first code"
    result = compare_2_files('test/code/10_1.txt', 'test/code/10_2.txt')
    print result


def test_11():
    """
    test 11 - change variables and function position (142 lines)
    """
    print " test 11 - change variables and function position (142 lines)"
    result = compare_2_files('test/code/11_1.txt', 'test/code/11_2.txt')
    print result


def test_12():
    """
    test 12 - small code, change variable names, function position (32 lines)
    """
    print " test 12 - small code, change variable names, function position (32 lines)"
    result = compare_2_files('test/code/12_1.txt', 'test/code/12_2.txt')
    print result


def test_13():
    """
    test 13 - small code, change variable names, value of number (32 lines)
    """
    print " test 13 - small code, change variable names, value of number (32 lines)"
    result = compare_2_files('test/code/13_1.txt', 'test/code/13_2.txt')
    print result


def test_14():
    """
    test 14 - hello world - change class name, digit vale, func name
    """
    print " test 14 - hello world - change class name, digit vale, func name "
    result = compare_2_files('test/code/14_1.txt', 'test/code/14_2.txt')
    print result

#
# def test_15():
#     """
#     test 15
#     """
#     print " test 15 - "
#     result = compare_2_files('test/code/15_1.txt', 'test/code/15_2.txt')
#     print result
#
#
# def test_16():
#     """
#     test 16
#     """
#     print " test 16 - "
#     result = compare_2_files('test/code/16_1.txt', 'test/code/16_2.txt')
#     print result
#
#
# def test_17():
#     """
#     test 17
#     """
#     print " test 17 - "
#     result = compare_2_files('test/code/17_1.txt', 'test/code/17_2.txt')
#     print result
#
#
# def test_18():
#     """
#     test 18
#     """
#     print " test 18 - "
#     result = compare_2_files('test/code/18_1.txt', 'test/code/18_2.txt')
#     print result
#
#
# def test_19():
#     """
#     test 19
#     """
#     print " test 19 - "
#     result = compare_2_files('test/code/19_1.txt', 'test/code/19_2.txt')
#     print result
#
#
# def test_20():
#     """
#     test 20
#     """
#     print " test 20 - "
#     result = compare_2_files('test/code/20_1.txt', 'test/code/20_2.txt')
#     print result

