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
        self.index = 0
        self.word = ''

    def start(self):
        self.index = 0
        self.word = RandomWords().get_random_word()

    def wrongGuess(self):
        if self.index < 10:
            self.index += 1

    def gameOver(self):
        print("Game Over")
        
    def winner(self, w):
        print("Congratulations, you guessed %s"%w)

    # Clean console
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

    def get_drawing(self):
        return '\n'.join(self.steps[index])

    def test(self):
        return word