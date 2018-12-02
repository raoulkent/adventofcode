text_file = open("input", "r")
id_list = text_file.read().split('\n')

# Part 1
double_char_ids = 0
triple_char_ids = 0

for id in id_list:
    duplicafe_found = False
    triple_found = False
    chars = list(id)
    char_set = set(chars)
    for char in char_set:
        if chars.count(char) == 2:
            duplicafe_found = True
        if chars.count(char) == 3:
            triple_found = True
    if duplicafe_found:
        double_char_ids += 1
    if triple_found:
        triple_char_ids += 1

checksum = double_char_ids * triple_char_ids

print('The list of checksum of the list is:')
print(checksum)

# Part 2
