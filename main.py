import random
#Load Flashcards in
import json

with open('flashcards (copy).json','r') as f:
  data = json.load(f)
with open('flashcards (copy copy).json','r') as f:
  data = json.load(f)
change = 0
right = 0
number = 0
wrong = []

def activate_neuron():
  global change
  global right
  global number
  b = input("What is your name?")
  if c == b:
    d = input("What would you like study?(Simple or Semi hard math)")
    if d == "Simple":
      keys = list(data.keys())
      random.shuffle(keys)
      for key in keys:
        print(keys[change])
        a = input("What is answer?")
        if a == data[keys[change]]:
          print("Well done!")
          change += 1
          right += 1
        else:
          print("WRONG!")
          if change < len(keys):
            wrong.append(key)
          change += 1
      change = 0
      print(f"You got {right}/12 correct!!!!")
      if right < 3:
        print("You got the following questions wrong:")
        random.shuffle(wrong)
        for wrong_question in wrong:
          print(f"{wrong_question} == {data[wrong_question]}")
          number += 1
        number = 0
      else:
        right = 0
        print("Congratulations! You got all the questions right!")
  else:
    
activate_neuron()

