import os
import colorama
from colorama import Fore, Style

# helper fuction to draw the board
def draw_board(spots,game,wins,names):
    
    board = (f"|{getattr(Fore, spots[1][1])}{spots[1][0]}{Style.RESET_ALL}|{getattr(Fore, spots[2][1])}{spots[2][0]}{Style.RESET_ALL}|{getattr(Fore, spots[3][1])}{spots[3][0]}{Style.RESET_ALL}|\n"
             f"|{getattr(Fore, spots[4][1])}{spots[4][0]}{Style.RESET_ALL}|{getattr(Fore, spots[5][1])}{spots[5][0]}{Style.RESET_ALL}|{getattr(Fore, spots[6][1])}{spots[6][0]}{Style.RESET_ALL}|\n"
             f"|{getattr(Fore, spots[7][1])}{spots[7][0]}{Style.RESET_ALL}|{getattr(Fore, spots[8][1])}{spots[8][0]}{Style.RESET_ALL}|{getattr(Fore, spots[9][1])}{spots[9][0]}{Style.RESET_ALL}|")

    print(board)
    print(f"Game: {game} | {names[0]}: {wins[0]} | {names[1]}: {wins[1]}")
    

def check_turn(turn):
    if turn % 2 == 0: return ('O','BLUE')
    else: return ('X','RED')

def check_for_win(spots):
  # Handle Horizontal Cases
  if (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True
  # Handle Vertical Cases
  elif   (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True
  # Diagonal Cases
  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True
    
  else: return False

def play_game(spots,game,wins,names):
    playing = True
    complete = False # complete will be True if there is a winner
    turn = 0
    prev_turn = -1    

    while playing:
        # reset the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # update the board
        draw_board(spots,game,wins,names)
        # if an invalid choice occurred, let the player know
        if prev_turn == turn:
            print("Invalid choice, please pick another.")
        prev_turn = turn
        print(f"{names[(turn % 2)]}'s turn: Pick your spot or press q to quit")
        choice = input()
        if choice == 'q': # force quit the game
            playing = False
        elif str.isdigit(choice) and int(choice) in spots:
            if not spots[int(choice)][0] in {"X",'O'}:
                turn +=1
                spots[int(choice)] = check_turn(turn)

        if check_for_win(spots): playing, complete = False, True
        if turn > 8: playing = False # drawn game

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots,game,wins,names)
    if complete:
        if check_turn(turn)[0] == "X": print(f"{names[0]} Wins!"); wins[0] += 1
        else: print(f"{names[1]} Wins!"); wins[1] += 1
    elif choice == 'q':
        print('Quitter')
        quit()
    else:
        print("It's a draw")