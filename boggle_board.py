import random
randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))

class Dice:
  def __init__(self):
    self.sides = [
            chr(random.randint(ord('A'), ord('Z'))),
            chr(random.randint(ord('A'), ord('Z'))),
            chr(random.randint(ord('A'), ord('Z'))),
            chr(random.randint(ord('A'), ord('Z'))),
            chr(random.randint(ord('A'), ord('Z'))),
            chr(random.randint(ord('A'), ord('Z')))
            ]
  def __str__(self):
    return f"1:{self.sides[0]}, 2:{self.sides[1]}, 3:{self.sides[2]}, 4:{self.sides[3]}, 5:{self.sides[4]}, 6:{self.sides[5]}"

  def roll(self):
    return self.sides[random.randint(0, 5)]

class Line(Dice):
  def __init__(self):
    self.die1 = Dice()
    self.die2 = Dice()
    self.die3 = Dice()
    self.die4 = Dice() 

    def roll(self):
      return self.die1.roll(), self.die2.roll(), self.die3.roll(), self.die4.roll(),

liner = Line()
print(liner.roll()) 

class BoggleBoard:
  def __init__(self):
    self.board = "____\n____\n____\n____\n"
    self.line1 = [die1=Dice(),die2 = Dice(), die3 =Dice(), die4 = Dice()]
           

  def __str__(self):
    return self.board
  
  def create_dice(self):
    
  
  def shake(self):
    new_board = []
    lines = 4
    while lines > 0:
      new_line = ""
      while len(new_line) < 4:
        new_line += chr(random.randint(ord('A'), ord('Z')))
      lines -= 1
      new_board += new_line+'\n'
    self.board = new_board

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