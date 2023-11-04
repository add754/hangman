import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has. This defaults to 5.
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    __check_guess(letter)
        Checks if the letter is in the word.
    __ask_for_input()
        Asks the user for a letter.
    play_game
        Initiates game.
    '''
    def __init__(self, word_list: list, num_lives: int = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = '_' * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def __check_guess(self, guess: str):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        guess = guess.lower()
        word_guessed_as_list = list(self.word_guessed)
        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    word_guessed_as_list[i] = guess
            self.word_guessed = ''.join(word_guessed_as_list)
            print(f'Good guess! {guess} is in the word. So far, your word looks like:\n{self.word_guessed}')
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def __ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            print("Please select a letter:\n")
            guess = input()
            if len(guess) != 1 or (not guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.__check_guess(guess)
                self.list_of_guesses.append(guess)
                break


    @staticmethod
    def play_game(word_list: list, num_lives: int = 5):
        '''
        Begins game play - including creating a new instance of the game.

        Parameters:
        ----------
        word_list: list
            List of words to be used in the game
        num_lives: int
            Number of lives the player has. This defaults to 5.
        '''
        print('Welcome to Handgman!\nEnjoy the game!\n')
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print('You lost!')
                break
            if game.num_letters == 0:
                print(f'Congratulations. You correctly identified the word as \"{game.word}\", You won the game!')
                break
            if game.num_letters > 0:
                game.__ask_for_input()
            
        
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'grapes', 'mango', 'strawberry']
    Hangman.play_game(word_list)
