"""
Izveidoja: Maksims Zamovskis 
Spēle HangMan
"""
import random
from os import system
from time import sleep

print("Sveicinam jūs spēlē HangMan")
print("Rakstiet pa vienu burtu, lai uzminētu vārdu, visi vārdi ir angļu valodā")
print("-----------------------------------------------------------------------")

# vārdu bibliotēka
wordDictionary = ["four", "house", "flower", "latvia", "python", "hello", "music", "heart", "rvt", "riga", "potato", "apple", "android", "windows", "linux", "computer"]

# Izvelējās jebkuru vārdu
randomWord = random.choice(wordDictionary)

for x in randomWord:
  print("_", end=" ")

# print hang man
def print_hangman(wrong):
  if(wrong == 0):
    system("cls")
    print()
    print()
    print()
    print()
    print("   ===")

  elif(wrong == 1):
    system("cls")
    print()
    print()
    print("    |")
    print("   ===")
  elif(wrong == 2):
    system("cls")
    print()
    print()
    print("    |")
    print("    |")
    print("   ===")        
  elif(wrong == 3):
    system("cls")
    print()
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    system("cls")
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    system("cls")
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 6):
    system("cls")
    print("\n+---+")
    print(" O  |")
    print(" |  |")
    print("    |")
    print("   ===")
  elif(wrong == 7):
    system("cls")
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 8):
    system("cls")
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 9):
    system("cls")
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/    |")
    print("    ===")
  elif(wrong == 10):
    system("cls")
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")

# Ja ujzminēja 
def printWord(guessedLetters):
  counter = 0
  rightLetters = 0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

# līnijas zem vārdiem
def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 10 and current_letters_right != length_of_word_to_guess):
  print("\nTik tālu uzminētie burti: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
  # Lai user varētu ievādīt burtu
  letterGuessed = input("\nUzmini burtu: ")
  # User uzminēja burtu
  if(randomWord[current_guess_index] == letterGuessed):
    print_hangman(amount_of_times_wrong)
    # Raksta  vardu
    current_guess_index+=1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  # User izdarīja daudz kļūdus
  else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(letterGuessed)
    # atjauno bildi
    print_hangman(amount_of_times_wrong)
    # Raksta vardu
    current_letters_right = printWord(current_letters_guessed)
    printLines()
# Programma analīzē
if amount_of_times_wrong == 10:
  print("""
  ▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▄▄▄█████▓ ▐██▌ 
   ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ ▐██▌ 
    ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░ ▐██▌ 
    ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒░ ▓██▓ ░  ▓██▒ 
    ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒  ▒██▒ ░  ▒▄▄  
     ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░    ░▀▀▒ 
   ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░     ░  ░ 
   ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░    ░          ░ 
   ░ ░         ░ ░     ░            ░  ░    ░ ░        ░            ░    
   ░ ░                                                                   """)
  sleep(2)
  print("Vards bija - ", randomWord)

else:
  print("""
   __   __  _______  __   __    _     _  ___   __    _  __  
  |  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  | 
  |  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  | 
  |       ||  | |  ||  |_|  |  |       ||   | |       ||  | 
  |_     _||  |_|  ||       |  |       ||   | |  _    ||__| 
    |   |  |       ||       |  |   _   ||   | | | |   | __  
    |___|  |_______||_______|  |__| |__||___| |_|  |__||__| """)



print("Paldies, par spēlēšanu manu spēli!")
