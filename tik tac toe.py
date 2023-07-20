import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1       
Win = 1    
Draw = -1    
Running = 0    
Stop = 1       
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def DrawBoard():    
    print(" %c | %c | %c | %c | %c " % (board[1],board[2],board[3],board[4],board[5]))    
        
    print(" %c | %c | %c | %c | %c " % (board[6],board[7],board[8],board[9],board[10]))    
        
    print(" %c | %c | %c | %c | %c " % (board[11],board[12],board[13],board[14],board[15]))    

    print(" %c | %c | %c | %c | %c " % (board[16],board[17],board[18],board[19],board[20]))    

    print(" %c | %c | %c | %c | %c " % (board[21],board[22],board[23],board[24],board[25]))
    
                
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
#This Function Checks player has won or not    
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[3] == board[4] and board[4] == board[5] and board[1] !=' '):    
        Game = Win    
        
    elif(board[6] == board[7] and board[7] == board[8] and board[8] == board[9] and board[9] == board[10] and board[6] !=' '):    
        Game = Win    
    elif(board[11] == board[12] and board[12] == board[13] and board[13] == board[14] and board[14] == board[15] and board[11] !=' '):
        Game = Win
    elif(board[16] == board[17] and board[17] == board[18] and board[18] == board[19] and board[19] == board[20] and board[16] !=' '):    
        Game = Win    
    elif(board[21] == board[22] and board[22] == board[23] and board[23] == board[24] and board[24] == board[25] and board[21] !=' '):    
        Game = Win    
        
    
    #Vertical Winning Condition    
    elif(board[1] == board[6] and board[6] == board[11] and board[11] == board[16] and board[16] == board[21] and board[1] != ' '):    
        Game = Win
    elif(board[2] == board[7] and board[7] == board[12] and board[12] == board[17] and board[17] == board[22] and board[2] != ' '):    
        Game = Win
    elif(board[3] == board[8] and board[8] == board[13] and board[13] == board[18] and board[18] == board[23] and board[3] != ' '):    
        Game = Win
    elif(board[4] == board[9] and board[9] == board[14] and board[14] == board[19] and board[19] == board[24] and board[4] != ' '):    
        Game = Win
    elif(board[5] == board[10] and board[10] == board[15] and board[15] == board[20] and board[20] == board[25] and board[5] != ' '):    
        Game = Win
        
    #Diagonal Winning Condition    
    elif(board[1] == board[7] and board[7] == board[13] and board[13] == board[19] and board[19] == board[25] and board[1] != ' '):    
        Game = Win
    elif(board[5] == board[9] and board[9] == board[13] and board[13] == board[17] and board[17] == board[21] and board[5] != ' '):    
        Game = Win

 
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' ' and board[10]!=' ' and board[11]!=' 'and board[12]!=' 'and board[13]!=' 'and board[14]!=' 'and board[15]!=' 'and board[16]!=' 'and board[17]!=' 'and board[18]!=' 'and board[19]!=' 'and board[20]!=' 'and board[21]!=' 'and board[22]!=' 'and board[23]!=' 'and board[24]!=' 'and board[25]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("Tic-Tac-Toe Game Designed By NARESH AND SANGEETHA")    
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(5)    
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-25] where you want to mark : "))    
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin()    
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won")    
