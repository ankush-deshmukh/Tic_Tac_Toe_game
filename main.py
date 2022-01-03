from src.utils import printBoard
from src.utils import get_input
from src.utils import checkWin

def run_game():
  board_dict = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
  print("This your TTC index board")
  printBoard(board_dict)
    
  player_dict=  {"p1": "X", "p2":"O"}
  player_select = "p1"
  valid_moves =0

  while valid_moves <=8:
    player_index = get_input(which_player = player_select)

    if board_dict[player_index] in player_dict.values():
      print("This position is aleardy occupied")
      continue
    board_dict[player_index]= player_dict[player_select]
    printBoard(board_dict)
    if player_select == "p1":
      player_select = "p2"
    elif player_select == "p2":
      player_select = "p1"
    valid_moves +=1

    if valid_moves >=5:
      v_list = list(board_dict.values())
      cutx =3
      h_cut_list = [v_list[x:x+cutx] for x in range(0, 9, cutx)]
      #print(h_cut_list)
      v_cut_list = [v_list[x:9:cutx] for x in range(0, cutx)]
      #print(v_cut_list)
      i=0
      cr_cut_list = []
      for x in range(0,3,3):
        cr_cut_list.append(v_list[i:9:4])
        i+=2
        cr_cut_list.append(v_list[i:8:2])
      #print(cr_cut_list)
      
      check_h_list = checkWin(h_cut_list)
      if "Player" in check_h_list:
        print(check_h_list)
        break
      check_v_list = checkWin(v_cut_list)
      if "Player" in check_v_list:
        print(check_v_list)
        break
      check_cr_list = checkWin(cr_cut_list)
      if "Player" in check_cr_list:
        print(check_cr_list)
        break
  print("Game is over, start with new")


if __name__ == "__main__":
  run_game()

