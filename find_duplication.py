import re


def split_to_lexems(source_code):
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