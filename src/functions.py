import json
import random

WORD_LENGTH = 5

def getRandomWord():
  # TODO: Implement this function.
  # Read words from targets.json file and return a random word.

  f = open('targets.json', 'r', encoding='utf-8')
  targets = json.load(f) #φορτώνει το json σαν λεξικό της python
  targets_size = len(targets)
  index = random.randint(0, targets_size) #τυχαιος αριθμός εντός του λεξιλογίου
  target = targets[index]
  while len(target)!=WORD_LENGTH: #εξασφαλίζεται οτι η λέξη είναι 5 χαρακτήρες
    index = random.randint(0, targets_size)
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
  results = [-1,-1,-1,-1,-1]
  
  target_ls = []               #list that contains the letters of the target word
  word_ls= []                  #list that contains the letters of the entry word
  index_of_same = []           #list that contains the index numbers of the same letters between the target list and the word list this will be usefull later when deleting letters from the lists
  index_of_diff = []           #list that contains the index numbers of the different letters between the target and word list

  for i in range(0,WORD_LENGTH):  
    target_ls.append(target[i])
    word_ls.append(word[i])
    if word_ls[i] == target_ls[i]:   
      results[i] = 1
      index_of_same.append(i)
    else:
      index_of_diff.append(i)

  if results == [1,1,1,1,1]:
    return results
  
  
  if index_of_same:
    for j in range (0, len(index_of_same)):
      del word_ls[index_of_same[j]-j]
      del target_ls[index_of_same[j]-j]
      print(word_ls)
    for index in range (0,len(word_ls)):
      if word_ls[index] in target_ls:
        target_ls.remove(word_ls[index])
        results[index_of_diff[index]] = 0
  else:
    for index in range (0,len(word_ls)):
      if word_ls[index] in target_ls:
        target_ls.remove(word_ls[index])
        results[index] = 0    
  
  return(results)