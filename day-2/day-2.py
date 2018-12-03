from difflib import SequenceMatcher

# Data input
text_file = open("input", "r")
id_list = text_file.read().split('\n')

# --- Part One ---
double_char_ids = 0
triple_char_ids = 0

for chars in id_list:
    char_count = {chars.count(char) for char in set(chars)}
    if 2 in char_count:
        double_char_ids += 1
    if 3 in char_count:
        triple_char_ids += 1

checksum = double_char_ids * triple_char_ids

print('The list of checksum of the list is:')
print(checksum)


# --- Part Two ---
def part2(id_list):
    for _id in id_list:
        id_list.remove(_id)
        for compared_id in id_list:
            zipped_list = zip(_id, compared_id)
            number_of_same_chars = 0
            for tuple_ in zipped_list:
                if tuple_[0] == tuple_[1]:
                    number_of_same_chars += 1
                if number_of_same_chars == compared_id.__len__()-1:
                    return strip_differing_chars(_id, compared_id)


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def strip_differing_chars(_str1, _str2):
    matcher = SequenceMatcher(None, _str1, _str2)
    blocks = matcher.get_matching_blocks()
    _str = ''.join([_str2[a:a + n] for a, _, n in blocks])
    return _str


print(part2(id_list))
