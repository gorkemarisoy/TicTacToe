from random import randrange

board=[[""for i in range(3)]for j in range(3)]

counter = 1
for r in range(3):
    for c in range(3):
        board[r][c]=counter #to fill playboard from 1to9
        counter += 1
list =[5] 



def display_board(board):
    print("""
+-------+-------+-------+
|       |       |       |
|  """,board[0][0],"""  |  """,board[0][1],"""  |  """,board[0][2],"""  |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  """,board[1][0],"""  |  """,board[1][1],"""  |  """,board[1][2],"""  |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  """,board[2][0],"""  |  """,board[2][1],"""  |  """,board[2][2],"""  |
|       |       |       |
+-------+-------+-------+
""")
    

 
    


def enter_move(board, list):
    print("please make your move 1-9 :")
    me=int(input())
    if me not in list:
        for r in range(3):
            for c in range(3):
                if board[r][c]== me:
                    list.append(me)
                    board[r][c]="O"
    else:
        print("try again")
        return enter_move(board, list)
    
    return victory_for(board,"O",list)
            
            
    
                
def draw_move(board, list):
    cp = randrange(1,10)
    
    if cp not in list:
        for r in range(3):
            for c in range(3):
                if board[r][c]==cp :
                    board[r][c]="X"
                    list.append(cp)
    else:
        return draw_move(board, list)
    return victory_for(board,"X",list)

    


            

def victory_for(board,sign,list):
    display_board(board)
    for c in range(3):
       
        if (board[c]==[sign,sign,sign] or board[0][c]==[sign,sign,sign] or
            board[0][0]==sign and board[1][1]==sign and board[2][2]==sign or
            board[0][2]==sign and board[1][1]==sign and board[2][0]==sign):
                if sign=="X":
                    return print("PC won")
                elif sign=="O":
                    return print("YOU won")
        
    if sign=="X":
        return enter_move(board, list)
    else:
        return draw_move(board, list)

board[1][1]="X"            
victory_for(board,"X",list)



    
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


