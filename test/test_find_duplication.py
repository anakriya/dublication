import os
from nose import with_setup
from find_duplication import split_to_lexems, calculate_final_hash, hash_tokens
#
#def setup_func():
#    "set up test fixtures"
#    pass
#
#def teardown_func():
#    "tear down test fixtures"
#    pass
#
#
#@with_setup(setup_func, teardown_func)
def test_1():
    "test of small part of code"
    f_path_first = os.path.join(os.getcwd(), 'test/code/1_1.txt')


    first_f = open(f_path_first, 'r')
    a = first_f.read()
    res_a = calculate_final_hash(a)

    print res_a
    print "\n"

    f_path_second = os.path.join(os.getcwd(), 'test/code/1_2.txt')
    second_f = open(f_path_second, 'r')
    b = second_f.read()

    res_b = calculate_final_hash(b)

    print res_b
    print "\n"
    print set(res_a)&set(res_b)
    #print len(a)/set(res_a)&set(res_b)
    assert 1==1