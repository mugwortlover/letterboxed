from scrape_sides import scrape

def contains_all_letters(word, letters):
    for letter in letters:
        if not letter in word:
            return False
    return True

def solve(letters):
    #import wordlist
    with open('./working_wordlist.txt', 'r') as file:
        words = [word[:-1] for word in file.readlines()]
    
    (l1, l2, l3, l4) = letters
    letters_all = l1 + l2 + l3 + l4

    
    #remove words that include illegal letters
    illegal_letter_index = 999
    illegal_letter = None
    to_remove = []

    for j in range(len(words)):
        word = words[j]
        if not illegal_letter_index >= len(word) and word[illegal_letter_index] == illegal_letter:
            to_remove.append(j)
            continue
        for i in range(len(word)):
            if word[i] not in letters_all:
                illegal_letter = word[i]
                illegal_letter_index = i
                to_remove.append(j)
                break

    for index in to_remove[::-1]:
        words.pop(index)

    
    #remove words that include two sequential letters in the same sublist
    rdict = {}
    for sublist in letters:
        for letter in sublist:
            rdict[letter] = sublist

    for i in range(len(words) - 1, 0, -1):
        word = words[i]
        for j in range(len(word) - 1):
            if rdict[word[j]] == rdict[word[j + 1]]:
                words.pop(i)
                break


    #remove words that are too small
    for i in range(len(words) - 1, 0, -1):
        word = words[i]
        if len(word) < 3:
            words.pop(i)

    
    #find 1 word combos
    combos1 = []
    for word1 in words:
            if contains_all_letters(word1, letters_all):
                combos1.append(word1)

    print('Single Word Solutions:')
    if len(combos1) == 0:
        print('-- no single word solutions found -- ')
    else:
        print(combos1[0])


    #find 2 word combos
    combos2 = []
    for word1 in words:
        for word2 in words:
            if word1[-1] == word2[0] and contains_all_letters(word1 + word2, letters_all):
                combos2.append((word1, word2))

    
    #sort 2 word combos by length (selection sort)
    for i in range(len(combos2) - 1):
        min_index = i
        for j in range(i + 1, len(combos2)):
            if len(combos2[j][0] + combos2[j][1]) < len(combos2[min_index][0] + combos2[min_index][1]):
                min_index = j
        if min_index != i:
            combos2[i], combos2[min_index] = combos2[min_index], combos2[i]


    #display 2 word combos
    print('\nDouble Word Solutions:')
    for combo in combos2[:10]:
        print(combo[0], combo[1], f'(l: {len(combo[0] + combo[1])})')

    

def get_input():
    inp = input('Enter letters (xxx xxx xxx xxx):')
    l = inp.split(' ')
    return [list(tri) for tri in l]
    

if __name__ == '__main__':
    #sample letters for testing
    letters1 = (('h', 'y', 'g'), ('l', 'm', 'w'), ('a', 'o', 'c'), ('r', 'n', 'i'))
    letters2 = (('p', 'n', 'b'), ('o', 'u', 'c'), ('i', 'r', 'a'), ('m', 't', 'k'))


    URL = 'https://www.nytimes.com/puzzles/letter-boxed'
    sides = scrape(URL)
    solve([list(tri.lower()) for tri in sides])
    

