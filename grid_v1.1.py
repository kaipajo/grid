import sys
import ast

def challenge():

  with open('../dictionary.txt','r') as inf:
    dict_from_file = ast.literal_eval(inf.read())

  chal1 = dict_from_file[input('Give first grid challenge: ')]
  chal2 = dict_from_file[input('Give second grid challenge: ')]
  chal3 = dict_from_file[input('Give third grid challenge: ')]

  print(chal1,chal2,chal3)
  return play_again()

def play_again():
    while True:
       answer = input('Do you want to rerun the program?:')
       if answer.lower().startswith("n"):
          print("ok, exiting")
          sys.exit()
       elif answer.lower().startswith("y"):
          print("ok, running again")
          return challenge()
		  
challenge()