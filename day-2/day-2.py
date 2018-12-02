# Data input
text_file = open("input", "r")
id_list = text_file.read().split('\n')

"""
--- Part One ---
"""
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

"""
--- Part Two ---
"""
