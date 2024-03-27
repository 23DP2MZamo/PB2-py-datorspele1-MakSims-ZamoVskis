"""
Izveidoja: Maksims Zamovskis 
Spēle HangMan
"""
import random
from os import system
from time import sleep

print("Sveicinam jūs spēlē HangMan")
print("-------------------------------------------")

vardubiblioteka = ["scooter", "flower", "Latvia", "Program", "Yeat","Labdien", "Matematika", "Triangle", "Algoritms", "MarkDown", "Python", "Computer", "Linux", "Windows", "Stockholm"]

### Izvelēties jebkuru vārdu
vards = random.choice(vardubiblioteka)

for x in vards:
  print("_", end=" ")

def print_hangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")

def printWord(uzzinatievardi):
  counter=0
  rightLetters=0
  for char in vards:
    if(char in uzzinatievardi):
      print(vards[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in vards:
    print("\u203E", end=" ")

length_of_word_to_guess = len(vards)
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
  if(vards[current_guess_index] == letterGuessed):
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  ### User was wrong a lot of times 
  else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(letterGuessed)
    ### Update the drawing
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()

system("cls")
print("\n+---+")
print("    |")
print("    |")
print("    |")
print("   ===")
sleep(0.5)

system("cls")
print("\n+---+")
print("O   |")
print("    |")
print("    |")
print("   ===")
sleep(0.5)

system("cls")
print("\n+---+")
print("O   |")
print("|   |")
print("    |")
print("   ===")
sleep(0.5)

system("cls")
print("\n+---+")
print(" O  |")
print("/|  |")
print("    |")
print("   ===")
sleep(0.5)

system("cls")
print("\n+---+")
print(" O  |")
print("/|\ |")
print("    |")
print("   ===")
sleep(0.5)

system("cls")
print("\n+---+")
print(" O  |")
print("/|\ |")
print("/   |")
print("   ===")
sleep(0.5)

system("cls")
print("\n+---+")
print(" O   |")
print("/|\  |")
print("/ \  |")
print("    ===")
sleep(0.5)

print("GAME OVER!!")