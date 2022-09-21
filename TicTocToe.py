from random import randrange

board=[[""for i in range(3)]for j in range(3)]

counter = 1
for r in range(3):
    for c in range(3):
        board[r][c]=counter #to fill playboard from 1to9
        counter += 1





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
    enter_move(board)

 
    

def enter_move(board):
    print("please make your move 1-9 :")
    me=int(input())
    for r in range(3):
        for c in range(3):
            if board[r][c]== me:
                board[r][c]="O"
                
    cp = randrange(1,10)
    for r in range(3):
        for c in range(3):
            if board[r][c]==cp:
                board[r][c]="X"
    return display_board(board)

board[1][1]="X"            
display_board(board)        


            

#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


#def draw_move(board):
    # The function draws the computer's move and updates the board.
