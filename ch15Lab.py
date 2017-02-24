'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''
import re
#15.1
dictionary = open("dictionary.txt")
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
alice = open("AliceInWonderLand200.txt", "r")
alice_text = []
#alice_lines = []
dictionary_list = []
wrong = []

for line in alice:
    words = split_line(line)
    for word in range(len(words)):
        alice_text.append(words[word])
alice.close()
    #alice_lines.append(line.strip())
#print(alice_lines)
for words in dictionary:
    dictionary_list.append(words.strip())
dictionary.close()
print(alice_text)
print(dictionary_list)
def spell_check(file):
    for i in file:
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False
        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2
            if dictionary_list[middle_pos] < i:
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > i:
                upper_bound = middle_pos - 1
            else:
                found = True
        if not found:
            print(i)
                #print("The word " + file[i] + " was found at position " + str(middle_pos))

        #wrong.append(file[i])

spell_check(alice_text)

