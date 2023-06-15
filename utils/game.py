from random import choice

class Hangman:
    def __init__(self):
        '''Attributes section
        self.possible_words - list with all the possible words to be guesed.
        self.word_to_find - a word will be picked randomly from the list.
        self.correctly_guessed_letters - list containing the correct letters guessed by the user.
        self.wrongly_guessed_letters - list containing the wrong letters guessed by the user.
        self.lives - total of chances to guess wrong. 5 by default.
        self.turn_count - a counter that will register all correct guesses turns.
        self.error_count - a counter that will register all wrong guesses turns.'''
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        *self.word_to_find, = choice(self.possible_words)
        self.correctly_guessed_letters = ['-'] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0
        
    def play(self):
        '''Funtion that has the core of the game. It checks the validity of the data typed by the user.
        It appends the correct and incorrect data to the correct attribute and count the turns.'''        
        letter = input('Enter a letter: ').lower()
        correct_position = []
        if letter.isalpha() and len(letter) == 1:
            if letter in self.word_to_find:
                if letter in self.correctly_guessed_letters:
                    print('You guessed correctly, but you have already typed this letter. Try another one.')
                else:                    
                    for i in range(len(self.word_to_find)):
                        if self.word_to_find[i] == letter:     
                            correct_position.append(i)
                            self.correctly_guessed_letters[i] = letter
                            self.turn_count += 1
                print(self.correctly_guessed_letters)            
            else:
                if letter not in self.wrongly_guessed_letters:
                    self.wrongly_guessed_letters.append(letter)
                    self.error_count += 1
                    self.lives -= 1
                    print(f'You still have {self.lives} chances. Be wise!')
                else:
                    print('You have already typed this letter. Try again!')
        else:
            print('Type letters and only one character!')      
    
    def game_over(self):
        '''Function that states the end of the game.'''
        print('GAME OVER!')
        print(f'You could not guess the word {"".join(self.word_to_find)}')
    
    def well_played(self):
        '''Function that states the end of the game if the user has guessed the word. It also displays a summary of the turns for all guessess needed:
        correct and incorrect.'''
        print('YOU DID IT!')
        print(f'You have guessed the word {"".join(self.word_to_find)} in {self.turn_count} turns and guessed {self.error_count} times wrongly!')
        print('Well done!')    
    
    def start_game(self):
        '''Function that initiates the game.'''
        print(f'You have {self.lives} chances to guess correctly and save the man from being hanged. Let the game begin!')
        while self.lives > 0:
            if sorted(self.correctly_guessed_letters) == sorted(self.word_to_find):
                self.well_played()
                return None
            else:
                self.play()
        self.game_over()