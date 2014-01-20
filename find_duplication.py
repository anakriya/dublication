import os
import re
import plyplus

FILE_PATH = 'grammar/python2.7.txt'

def split_to_lexems():
    file_path = "test/code/6_1.txt"

    f_path = os.path.join(os.getcwd(), file_path)


    f = open(f_path, 'r')
    source_code = f.read()


    f_path = os.path.join(os.getcwd(), FILE_PATH)
    f = open(f_path, 'r')
    grammar = f.read()
    g = plyplus.Grammar(grammar)

    t = g.parse(source_code)
    result = [i.head for i in t.select('*') if isinstance(i, t.__class__) and i.head != 'name']
    return result


def _split_to_lexems(source_code):
    return re.split("[\s;]+", source_code)


def hash_tokens(token_list, window):
    hash_list = []
    for index, item in enumerate(token_list[:-window + 1]):
        hash_list.append(hash(tuple(token_list[index:index+window])))
    return hash_list


def winnow(window, hash_list):
    res_set = set()
    for index, item in enumerate(hash_list[:-window + 1]):
        res_set.add(min(hash_list[index:index+window]))
    return res_set


def calculate_final_hash(soucre_code):
    res = split_to_lexems(soucre_code)
    #TODO(akrish): translate lexems to tokens
    res = hash_tokens(res, 3)
    res = winnow(3, res)
    return res