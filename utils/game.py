from random import choice

class Hangman:
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = choice(self.possible_words)
        self.correctly_guessed_letters = ['-'] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0
        
    def play(self):        
        letter = input('Enter a letter: ').lower()
        if letter.isalpha() and len(letter) == 1:
            if letter in self.word_to_find:
                correctly_position = self.word_to_find.index(letter)                
                self.correctly_guessed_letters[correctly_position] = letter                
            else:
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
                self.lives - 1
        else:
            print('Type only letters and only one character!')      
    
    def game_over(self):
        print('GAME OVER!')
    
    def well_played(self):        
        if self.correctly_guessed_letters in self.word_to_find:
            print('WELL PLAYED!')    
    
    def start_game(self):
        while self.lives > 0:
            self.play()
            print(self.correctly_guessed_letters)
        if self.well_played():
            pass