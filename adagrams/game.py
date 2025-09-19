from random import randint
#wave 01
def draw_letters():
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
    }
    letter_list = []
    hand_of_letters = []

    for letter, quantity in LETTER_POOL.items():
        for qty in range(quantity):
            letter_list.append(letter)

    for draw in range(10):
        rand_index = randint(0, len(letter_list) -1)
        hand_of_letters.append(letter_list.pop(rand_index))

    return hand_of_letters
#wave 02
def uses_available_letters(word, letter_bank):
    letter_count = {}
    for letter in letter_bank:
        if letter_count.get(letter.upper()) is None :
            letter_count[letter.upper()] = 0
        letter_count[letter.upper()] += 1
    
    for char in word:
        if letter_count.get(char.upper()) is None:
            return False
        letter_count[char.upper()] -= 1
        if letter_count.get(char.upper()) < 0:
            return False

    return True
#wave 03
def score_word(word):
    letter_values = {
    'A': 1,
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
    }
    score = 8 if len(word) >= 7 and len(word) <= 10 else 0
    
    for char in word:
        score += letter_values[char.upper()]

    return score  
#wave 04
def get_highest_word_score(word_list):
    high_score = ("", 0)

    for word in word_list:
        score = score_word(word)
        if high_score[1] <= score:
            if len(high_score[0]) != 10 and len(word) == 10:
                high_score = (word, score)
            elif len(high_score[0]) != 10 and (high_score[1] == 0 or len(word) < len(high_score[0]) or high_score[1] < score):
                high_score = (word, score)

    return high_score