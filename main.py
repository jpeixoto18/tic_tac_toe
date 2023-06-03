from helpers import play_game
import os

# declare variables
rematch = True
game = 1
wins = [0,0]


print('Enter Player 1 name:')
player1Name = input()
print('Enter Player 1 name:')
player2Name = input()
names = [player1Name,player2Name]

while rematch:
    # instanciate the board
    spots = {1:('1','WHITE'),2:('2','WHITE'),3:('3','WHITE'),
         4:('4','WHITE'),5:('5','WHITE'),6:('6','WHITE'),
         7:('7','WHITE'),8:('8','WHITE'),9:('9','WHITE'),}
    
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # start a game
    play_game(spots,game,wins,names)

    # assess rematch
    print('Want to play again? (y/n)')
    re = input()
    if re != 'y': rematch = False
    game += 1

print('Thanks for playing!')