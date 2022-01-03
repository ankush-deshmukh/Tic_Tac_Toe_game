def printBoard(my_dict):
  v_list = list(my_dict.values())
  a= 0
  for i in range(3):
    print([v_list[a], v_list[a+1], v_list[a+2]])
    a+=3

def get_input(which_player):
  print("{} input turn Please enter your choice of index".format(which_player))

  while True:
    choice = input()
    if type(choice) != int:
      try:
        choice = int(choice)
      except:
        print("Please enetr the valid integer number as a choice between 1 to 9 only")
        continue
    if choice >9 or choice <=0:
      print("Please enetr the valid integer number as a choice between 1 to 9 only")
      continue
    else:
      break
  return choice

def checkWin(cut_list):
  for lst in cut_list:
    p1_c =0
    p2_c= 0
    for ls in lst:
      if ls == "X":
        p1_c +=1
      elif ls == "O":
        p2_c +=1
    if p1_c ==3:
      return "Player 1 win"
    elif p2_c == 3:
      return "Player 2 win"
  return "continue"
