import json
import random

def getRandomWord():
  # TODO: Implement this function.
  # Read words from targets.json file and return a random word.

  f = open('targets.json', 'r', encoding='utf-8')
  targets = json.load(f) #φορτώνει το json σαν λεξικό της python
  targets_size = len(targets)
  index = random.randint(0, targets_size-1) #τυχαιος αριθμός εντός του λεξιλογίου
  target = targets[index]
  
  while len(target)!=5: #εξασφαλίζεται οτι η λέξη είναι 5 χαρακτήρες
    index = random.randint(0, targets_size-1)
    target = targets[index]

  target = target.upper()

  return target


def dictionaryCheck(word: str):
  # TODO: Implement this function.
  # Check if the word is in the dictionary.json file.
  # Return True or False.

  f = open('dictionary.json', 'r', encoding='utf-8')
  dictionary = json.load(f)
  
  
  for dictionary_word in dictionary:
    if word.upper() == dictionary_word.upper(): return True

  return False


def validateWord(target: str, word: str):
  # TODO: Implement this function.
  # Compare [target] and [word] and return a list of numbers.
  # If the number is -1, the letter is not in the target word.
  # If the number is 0, the letter is in the target word but not in the correct position.
  # If the number is 1, the letter is in the target word and in the correct position.
  # Lets say the target word is "apple" and the user enters "alpha"
  # The function should return [1, 0, 1, -1, -1]  
  
  #αφου το a στο τελος του alpha που εβαλε ο χρήστης υπάρχει στο apple, κανονικα ετσι οπως εχεις εξηγησει πάνω θα πρέπει να επιστρέφει [1, 0, 1, -1, 0]

  results = [-1,-1,-1,-1,-1]

  for i in range(0,len(target)): 
    for j in range(0,len(word)): # συγκρίνει ολα τα γράμματα των συναρτήσεων ένα ένα και αν ταυτίζονται κανει το αντιστοιχο results 0
      if word[j]==target[i]:results[j]=0
      
  
  for i in range(0,5):           # συγκρίνει τα γράμματα των λέξεων στις ίδιες θέσεις και όταν ταυτίζονται κανει το results 1
    if word[i]==target[i]:results[i]=1


  return(results)


