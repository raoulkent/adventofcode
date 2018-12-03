from difflib import SequenceMatcher

# Data input
text_file = open("input", "r")
id_list = text_file.read().split('\n')


# --- Part One ---
def part1(string_list):
    double_char_ids = 0
    triple_char_ids = 0

    for chars in string_list:
        char_count = {chars.count(char) for char in set(chars)}
        if 2 in char_count:
            double_char_ids += 1
        if 3 in char_count:
            triple_char_ids += 1

    return double_char_ids * triple_char_ids


print('The list of checksum of the list is:')
print(part1(id_list))


# --- Part Two ---
def part2(_list):
    for _id in _list:
        _list.remove(_id)
        for _id_compared in _list:
            if hamming_distance(_id, _id_compared) == 1:
                return strip_differing_chars(_id, _id_compared)


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def strip_differing_chars(s1, s2):
    matcher = SequenceMatcher(None, s1, s2)
    blocks = matcher.get_matching_blocks()
    _str = ''.join([s2[a:a + n] for a, _, n in blocks])
    return _str


print(part2(id_list))
