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
    for id_ in id_list:
        id_list.remove(id_)
        for compared_id in id_list:
            zipped_list = zip(id_, compared_id)
            number_of_same_chars = 0
            for tuple_ in zipped_list:
                if tuple_[0] == tuple_[1]:
                    number_of_same_chars += 1
                if number_of_same_chars == compared_id.__len__()-1:
                    matcher = SequenceMatcher(None, id_, compared_id)
                    blocks = matcher.get_matching_blocks()
                    string_ = ''.join([id_[a:a+n] for a, _, n in blocks])
                    return string_


print(part2(id_list))
