'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
import re
file = open("dictionary.txt", "r")
current_biggest = 0

for word in file:
    if (len(word)) >= current_biggest:
        current_biggest = len(word)
        total_biggest = word
print(total_biggest)

#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

import re
#Number of words in text
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
file = open("AliceInWonderLand.txt", "r")
text = []

for line in file:
    words = split_line(line)
    for word in range(len(words)):
        text.append(words[word])
print("There are", len(text), "words in Alice In Wonderland.")

#Average length of words in text
average = 0

for i in range(len(text)):
    average += len(text[i])
average_length = average / len(text)
print("The average word in Alice in Wonderland is", round(average_length, 2), "letters long.")

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does

# "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("AliceInWonderLand.txt")
text_list = []
cat = 0
cheshire = 0
cheshire_cat = 0
for line in file:
    words = split_line(line)
    for word in range(len(words)):
        text_list.append(words[word])
        if words[word].upper() == "CAT":
            cat += 1
        elif words[word].upper() == "CHESHIRE":
            cheshire += 1
        if words[word-1].upper() == "CHESHIRE" and words[word].upper() == "CAT":
            cheshire_cat +=1


print("The word cat appears", cat, "times in Alice In Wonderland!")
print("The word chesire appears", cheshire, "times in Alice In Wonderland!")
print("The word cheshire cat appears", cheshire_cat, "times in Alice In Wonderland!")