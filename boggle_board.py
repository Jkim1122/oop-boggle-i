import random

randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))

class BoggleBoard:
  
  def __init__(self):
    pass
    
    # line_one = "____"
    # line_two = "____"
    # line_three = "____"
    # line_four = "____"

  # def shake(self):
  #   for ltr in self.line_one:
  #     ltr = randomUpperLetter

# print(randomUpperLetter)


welcome_message = """
----  WELCOME  ---- 
1. Start New Game
2. Quit

"""
quit = False
while quit == False:
    user_input = input(f"""{welcome_message}What would you like to do? input one of the numbers to execute command: """)
    


new_boggle_board = [["____"], ["____"], ["____"], ["____"]]
# while True:
  #  print(new_boggle_board)
print(new_boggle_board)
