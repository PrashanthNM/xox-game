from IPython.display import clear_output
def display_board(a):
    print('\t\t',a[0],a[1]+'|'+a[2]+'|'+a[3])
    print("\t\t  ------")                       #each time you call display board it displays the updated board
    print('\t\t',a[0],a[4]+'|'+a[5]+'|'+a[6])
    print("\t\t  ------")
    print('\t\t',a[0],a[7]+'|'+a[8]+'|'+a[9])
global board
board=['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(board)   #calling the board function
def ask():             # this ask functions asks the player_1 to select 'x' or 'o'
    global player_1,player_2,sign1,sign2
    sign1=input("hey,what do you want to choose 'x' or 'o' ")
    if sign1=='x':
        player_1=sign1
        player_2=sign2='o'
        
    else:
        player_2=sign2='x'
        player_1=sign1
    print(f"player_1 have choosen {player_1} and player_2 have choosen {player_2}")
def validity(inp1,inp2):
    if val!=1:
        if board[inp1]==" " and board[inp2]==" ":
            return True
        else:
            return False
    return True

def calculate(a,val):#to check who wins the game
    for i in range(1,8,3):
        if a[i]==a[i+1]==a[i+2]==sign1 or a[i]==a[i+1]==a[i+2]==sign2: #this part checks each row of the board
            if a[i]==sign1:
                print("player 1 won")
                return 10
                break
            elif a[i]==sign2:
                print("player 2 won")
                return 10
                break
              
        elif a[1]==a[5]==a[9]==sign1 or a[1]==a[5]==a[9]==sign2:#this checks diagnols of the board
            if a[1]==sign1:
                print("player 1 won")
                return 10
                break
            elif a[1]==sign2:
                print("player 2 won")
                return 10
                break
        elif a[3]==a[5]==a[7]==sign1 or a[3]==a[5]==a[7]==sign2:#checks diagnols of the board
            if a[3]==sign1:
                print("player 1 won")
                return 10
                break
            elif a[3]==sign2:
                print("player 2 won")
                return 10
                break

    for i in range(1,4): #this checks vertical coloumns
        if (a[i]==a[i+3]==a[i+6]==sign1) or (a[i]==a[i+3]==a[i+6]==sign2):
            if a[i]==sign1:
                print("player 1 won")
                val=10
                break
            elif a[i]==sign2:
                print("player 2 won")
                val=10
                break
    return val
                
        
            
ask()
global val
val=1
while val<=9:
    while True:
        inp1=int(input(f"player_1,enter where {player_1} should be enterd"))
        inp2=int(input(f"player_2,enter where {player_2} should be enterd"))
        avail=validity(inp1,inp2)
        if avail==True:
            board[inp1]=sign1
            board[inp2]=sign2
            break
        else:
            print("please enter the valid numbers")
    clear_output()
    val=1
    display_board(board)
    val=calculate(board,val)
    val+=1
    
    
    
    