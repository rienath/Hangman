# Module for drawing Hangman drawings in the console
import os
from random_word import RandomWords

class ConsoleHangman:

    # drawing for each step
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

    # all of the steps in order
    steps = [step_zero, step_one, step_two, step_three, step_four, step_five, step_six, step_seven, step_eight, step_nine, step_ten]

    def __init__(self):
        # Wrong guesses number
        self.index = 0
        # Wrong guesses letter
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
        self.guessed.append(letter.upper())
        if self.index < 10:
            self.index += 1
        else:
            self.game_over()

    def game_over(self):
        print("Game Over")
        
    def winner(self, w):
        print("Congratulations, you guessed %s"%w)
        return -1

    # Clean console
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    # Returns Hangman drawing
    def hangman_drawing(self):
        return '\n'.join(self.steps[index])

    # Returns drawing of guessed letters
    def letters_drawing(self):
        drawing = ''
        for i in self.word:
            drawing += i if i in self.guessed else '_'
            drawing += ' '
        print(drawing)
            


    def game(self):
        self.start()


    def test(self):
        self.letters_drawing()