# library to randomize
import random 

# function fight
# parameter : player & computer
def fight(player, computer):
    # if player chose scissors & computer chose scissors = tie
  if player == 1 and computer == 1:
    return "tie"
    # if player chose scissors & computer chose rock = lose
  elif player == 1 and computer == 2:
    return "lose"
    # if player chose scissors & computer chose paper = win
  elif player == 1 and computer == 3:
    return "win"
    # if player chose rock & computer chose scissor = win
  elif player == 2 and computer == 1:
    return "win"
    # if player chose rock & computer chose rock = tie
  elif player == 2 and computer == 2:
    return "tie"
    # if player chose rock & computer chose paper = lose
  elif player == 2 and computer == 3:
    return "lose"
    # if player chose paper & computer chose scissor = lose
  elif player == 3 and computer == 1:
    return "lose"
    # if player chose paper & computer chose rock = win
  elif player == 3 and computer == 2:
    return "win"
    # if player chose paper & computer chose paper = tie
  elif player == 3 and computer == 3:
    return "tie"


# Class Player
class Player:

  # constructor : name, hp, history
  def __init__(self, name):
    self.name = name
    self.hp = 100      # set hp to 100
    self.history = {}  # set history with empty dictionary

  # to display player name
  def getName(self):
    return self.name

  # to display player HP
  def getHP(self):
    return self.hp

  # to add results of the fight to history
  def addHistory(self, result):
    # check first to see if the result has been registered or not

    # if not, set value to 1
    if result not in self.history.keys():
      self.history[result] = 1

    # if yes, add the 1 to the existing value
    else:
      self.history[result] += 1

print("Welcome to a simple rock, paper, scissor game created with python!")
print("Here you will play against a computer in a game of rock, paper, scissor")
print("You will have 100 HP and every time you lose against the computer, your HP will be deducted 10 points")
print("Enjoy the game!")
print("")

# ask user to input name
name = input("Enter your name : ")

# call Player class
p = Player(name)

# set value of menu with 0
menu = 0


while menu != 4:
  print("MAIN MENU")
  print("1. Fight")
  print("2. History")
  print("3. Info")
  print("4. Exit")
  menu = int(input("Enter menu : ")) # ask user to input menu
  print("")

  # if user input 1, then the program begins
  if menu == 1:
    print("1. Scissors")
    print("2. Rock")
    print("3. Paper")

    # user are asked to chose between 1, 2 and 3, with 1 represent scissor, 2 represent rock, 3 represent, paper
    player = int(input("Choose Scissor, Rock, or Paper [1,2,3] : "))

    # computer will pick 1, 2, or 3 randomly
    computer = random.choice([1, 2, 3])

    # call fight method
    result = fight(player, computer)

    # if player chose scissors & computer chose scissors = tie
    if player == 1 and computer == 1:
        print("Player chose scissor & computer chose scissor, it's a tie!") 
    # if player chose scissors & computer chose rock = lose
    elif player == 1 and computer == 2:
        print("player chose scissors & computer chose rock, you lose!") 
    # if player chose scissors & computer chose paper = win
    elif player == 1 and computer == 3:
        print("player chose scissors & computer chose paper, you win!") 
    # if player chose rock & computer chose scissor = win
    elif player == 2 and computer == 1:
        print("player chose rock & computer chose scissor, you win!") 
    # if player chose rock & computer chose rock = tie
    elif player == 2 and computer == 2:
        print("player chose rock & computer chose rock, it's a tie") 
    # if player chose rock & computer chose paper = lose
    elif player == 2 and computer == 3:
        print("player chose rock & computer chose paper, you lose") 
    # if player chose paper & computer chose scissor = lose
    elif player == 3 and computer == 1:
        print("player chose paper & computer chose scissor, you lose!") 
    # if player chose paper & computer chose rock = win
    elif player == 3 and computer == 2:
        print("player chose paper & computer chose rock, you win!")
    # if player chose paper & computer chose paper = tie
    elif player == 3 and computer == 3:
        print("player chose paper & computer chose paper, it's a tie") 
        
    print("")

    # if player lose then the calculation of HP begins
    if result == "lose":
      p.hp -= 10      # player HP will be deducted by 10
      # if player hp is already at 0, than the game is over
      if p.hp == 0:
        print("Your HP is already at zero.")
        print("GAME OVER !")
        break

    # call addHistory method to add the result of the game
    p.addHistory(result)


  # if user chose 2, then show all history
  elif menu == 2:
    print("--------------")
    for result in p.history.items():
      print("|", result[0], " : ", result[1], "|")
    print("--------------")

  # if user chose 3, then show HP
  elif menu == 3:
    print("INFO")
    print("HP : ", p.hp)

# additional note: 
# because of value of menu is set to 0, if player chose a number beside 1-4,
# the program will just begin from the beginning, without deleting the history of the game because it hasn't end the game yet