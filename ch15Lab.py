# Need to open alice again to read through 2nd time.

'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''
import re
dictionary = open("dictionary.txt")
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
alice = open("AliceInWonderLand200.txt", "r")
dictionary_list = []
for words in dictionary:
    dictionary_list.append(words.strip())
dictionary.close()

### LINEAR SEARCH ###
line_number = 0
for line in alice:
    words = split_line(line)
    line_number += 1
    for word in words:
        for i in range(len(dictionary_list)):
            if dictionary_list[i] == word.upper():
                break
        else:
            print(word, "in line", line_number, "is not found.")

alice.close()
alice = open("AliceInWonderLand200.txt", "r")

### BINARY SEARCH ###
line_number = 0
for line in alice:
    words = split_line(line)
    line_number += 1
    for word in words:
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False
        while upper_bound >= lower_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2
            if dictionary_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True
        if not found:
            print(word, "in line", line_number, "is not in the dictionary.")

alice.close()
