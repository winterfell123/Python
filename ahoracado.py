import random

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        ==========''','''
    
    +---+
    |   |
    O   |
        |
        |
        |
        ==========''','''
   
    +---+
    |   |
    O   |
    |   |
        |
        |
        ==========''','''
    
    +---+
    |   |
    O   |
   /|   |
        |
        |
        ==========''','''
    
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ==========''','''
    
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ==========''','''
    
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ==========''','''
    
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ==========''','''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado',
    'ted bundy'
]

def display_board(hidden_word, tries, letter_used):
    print(IMAGES[tries])
    print('')
    print(hidden_word)        
    print('---*---*---*---*---*---*---*---*---*---*---*---')
    print('Letras Usadas: {}'.format(letter_used))
    print('---*---*---*---*---*---*---*---*---*---*---*---')  

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def new_letter(hidden_word):
    letter = str(input('Escoge una letra: ')) 
    return letter     

def used_letter(current_letter, letter_used):
    try:
        letter_used.index(current_letter)
        return letter_used
    except ValueError:
        letter_used.append(current_letter)
        return letter_used

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    letter_used = [] 
    tries = 0

    while True:
        display_board(hidden_word, tries, letter_used)
        current_letter = new_letter(hidden_word) 

        used_letter(current_letter, letter_used)
        
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries, letter_used)
                print('')
                print('Lo sentimos! habeis perdido! la palabra era: {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            
            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Habeis ganado! Felicidades! En Hora Buena!')
            print('La palabra es: {}'.format(word))
            break
    
if __name__ == '__main__':
    print('B I E N V E N I D O S   A   A H O R C A D O S ')
    run()



    
