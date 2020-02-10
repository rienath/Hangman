# Module for playing hangman in the console
import os
from random_word import RandomWords

class ConsoleHangman:

    # Drawing for each step
    step_zero = [
        "              ",
        "              ",
        "              ",
        "              ",
        "              ",
        "              ",
        "              ",
        "              "
    ]

    step_one = [
        "              ",
        "              ",
        "              ",
        "              ",
        "              ",
        "              ",
        "              ",
        "___ ___       "
    ]

    step_two = [
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "___:___       "
    ]

    step_three = [
        "    _______   ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "___:___       "
    ]
    
    step_four = [
        "    _______   ",
        "   :       :  ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "___:___       "
    ]

    step_five = [
        "    _______   ",
        "   :       :  ",
        "   :       O  ",
        "   :          ",
        "   :          ",
        "   :          ",
        "   :          ",
        "___:___       "
    ]

    step_six = [
        "    _______   ",
        "   :       :  ",
        "   :       O  ",
        "   :       :  ",
        "   :       :  ",
        "   :          ",
        "   :          ",
        "___:___       "
    ]

    step_seven = [
        "    _______   ",
        "   :       :  ",
        "   :       O  ",
        "   :       :/ ",
        "   :       :  ",
        "   :          ",
        "   :          ",
        "___:___       "
    ]
    
    step_eight = [
        "    _______   ",
        "   :       :  ",
        "   :       O  ",
        "   :      \:/ ",
        "   :       :  ",
        "   :          ",
        "   :          ",
        "___:___       "
    ]

    step_nine = [
        "    _______   ",
        "   :       :  ",
        "   :       O  ",
        "   :      \:/ ",
        "   :       :  ",
        "   :      /   ",
        "   :          ",
        "___:___       "
    ]

    step_ten = [
        "    _______   ",
        "   :       :  ",
        "   :       O  ",
        "   :      \:/ ",
        "   :       :  ",
        "   :      / \\ ",
        "   :          ",
        "___:___       "
    ]

    # All of the steps in order
    steps = [step_zero, step_one, step_two, step_three, step_four, step_five, step_six, step_seven, step_eight, step_nine, step_ten]

    def __init__(self):
        # Wrong guesses number
        self.index = 0
        # Guessed letters
        self.guessed = []
        # Word to be guessed
        self.word = RandomWords().get_random_word().upper()

    def start(self):
        # Clear console
        self.cls()
        # Print intro text
        print('\n'.join([
               "  ^   ^   ^   ^   ^   ^   ^       ^   ^   ^   ^   ^   ^   ^  ",
               " /C\ /O\ /N\ /S\ /O\ /L\ /E\     /H\ /A\ /N\ /G\ /M\ /A\ /N\ ",
               "<___X___X___X___X___X___X___>   <___X___X___X___X___X___X___>"
        ]))

    def wrong_guess(self, letter):
        if self.index < 10:
            self.index += 1

    # If you lose
    def game_over(self):
        print('')
        print("Game Over")
        print('')
        print("The word was %s"%self.word)
    
    # If you win
    def winner(self, w):
        print('')
        print("Congratulations, you guessed %s"%w)

    # Clean console
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    # Returns Hangman drawing
    def hangman_drawing(self):
        print('\n'.join(self.steps[self.index]))

    # Prints drawing of guessed letters
    def letters_drawing(self):
        drawing = ''
        for i in self.word:
            drawing += i if i in self.guessed else '_'
            drawing += ' '
        print('Word: ' + drawing)

    # Prints all guessed letters
    def all_letters(self):
        drawing = 'Guessed letters: '
        for i in self.guessed:
            drawing += i
            drawing += ' '
        print(drawing)

    # Ask user to pick a letter.
    # Check if it is a single character letter.
    def pick_a_letter(self):
        while True:
            userInput = input('Pick a letter --> ')
            if len(userInput) == 1:
                if userInput.isalpha():
                    if userInput.upper() in self.guessed:
                        print('You already guessed that letter')
                    else:
                        break
                print('Letters only')
            else:
                print('Single characters only')
        self.guessed.append(userInput.upper())

    # The game itself, which utilises all the methods above
    def game(self):
        while True:
            self.start()
            print()
            self.letters_drawing()
            print('')
            self.all_letters()
            print('')
            self.hangman_drawing()
            print('')
            self.pick_a_letter()
            # Wrong guess
            if self.guessed[-1] not in self.word:
                self.wrong_guess(self.guessed[-1])
            # All the letters guessed
            elif all(elem in self.guessed for elem in self.word):
                self.winner(self.word)
                break
            # Out of tries
            if self.index > 9:
                self.game_over()
                break
            self.cls()