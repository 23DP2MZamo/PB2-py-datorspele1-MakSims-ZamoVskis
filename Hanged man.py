"""
Izveidoja: Maksims Zamovskis 
Spēle HangMan
"""
import random
from os import system
from time import sleep

print("Sveicinam jūs spēlē HangMan")
print("-------------------------------------------")

wordDictionary = ["four", "house", "sunflower", "latvia", "Python", "hello", "music", "Heart", "espada", "algoritm", "programmmer", "RVT", "Riga", "Potato", "Apple", "Android", "Windows", "Linux", "Computer"]

### Choose a random word
randomWord = random.choice(wordDictionary)

for x in randomWord:
  print("_", end=" ")

def print_hangman(wrong):
  if(wrong == 0):
    system("cls")
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1):
    system("cls")
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    system("cls")
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    system("cls")
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    system("cls")
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    system("cls")
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    system("cls")
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")

def printWord(guessedLetters):
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
  ### Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  ### User is right
  if(randomWord[current_guess_index] == letterGuessed):
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  ### User was wrong af
  else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(letterGuessed)
    ### Update the drawing
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()


print("GAME OVER, Thanks for playing ;D!!")
