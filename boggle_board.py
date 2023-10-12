import random
randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))

class BoggleBoard:
  def __init__(self):
    self.board = "____\n____\n____\n____\n"

  def __str__(self):
    return self.board
  
  def shake(self):
    new_board = ""
    lines = 4
    while lines > 0:
      new_line = ""
      while len(new_line) < 4:
        new_line += chr(random.randint(ord('A'), ord('Z')))
      lines -= 1
      new_board += new_line+'\n'
    self.board = new_board

boggle_board = BoggleBoard()

print(boggle_board)
boggle_board.shake()
print(boggle_board)
# welcome_message = """
# ----  WELCOME  ----
# 1. Start New Game
# 2. Quit
# """
# quit = False
# while quit == False:
#     user_input = input(f"""{welcome_message}What would you like to do? input one of the numbers to execute command: """)







# import random
# randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))

# class BoggleBoard:
  
#   def __init__(self):
#     self.board = "____\n____\n____\n____"
  
#   def __str__(self):
#     return self.board
  
#   def shake(self):
#     for i in self.board:
#       i = randomUpperLetter
#       i += 1
#       return i

# # print(randomUpperLetter)

# # welcome_message = """
# # ----  WELCOME  ---- 
# # 1. Start New Game
# # 2. Quit

# # """
# # quit = False
# # while quit == False:
# #     user_input = input(f"""{welcome_message}What would you like to do? input one of the numbers to execute command: """)
    


# boggle_board = BoggleBoard()
# # while True:
#   #  print(new_boggle_board)
# print(boggle_board.board)
# boggle_board.shake()
# print(boggle_board.board)