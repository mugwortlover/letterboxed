#helper file to remove double letters and words less than len 3

with open('NWL2020.txt', 'r') as file:
    words = [word[:word.find(' ')] for word in file.readlines()]


for i in range(len(words) - 1, -1, -1):
    word = words[i]
    if len(word) < 3:
        words.pop(i)
        continue
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            rm_i = words.pop(i)
            break

with open('working_wordlist2.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')
      


