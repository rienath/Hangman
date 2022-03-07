# Hangman
## Requirements
 - [Python 3](https://www.python.org/downloads/)
 - random_word library (pip3 install random_word)
 ## Objective
Guess the word/phrase before your man gets hung!
## Gameplay
Computer generates a word; the player tries to guess what it is one letter at a time. The computer draws a number of dashes equivalent to the number of letters in the word. If a guessing player suggests a letter that occurs in the word, the computer fills in the blanks with that letter in the right places. If the word does not contain the suggested letter, the computer draws one element of a hangman’s gallows. As the game progresses, a segment of the gallows and of a victim is added for every suggested letter not in the word. The number of incorrect guesses before the game ends is 10.
