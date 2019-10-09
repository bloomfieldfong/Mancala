
##Valida si el movimiento es valido 
##Parametros: array: estado del jugador, pick: que 
def valid_move(array, pick):
    if array[pick] >0 :
        return True
    else: 
        return False

def clean(board):
    for i in range(6):
        board[i]= 0
    for i in range (7,13):
        board[i]= 0

##Print de board
def print_board(ia, me):
    ia.reverse()
    print('IA  12 11 10  9  8  7\n')
    print(ia[:1], ia[1:7])
    print('   ', me[0:6],me[6:])
    print('\nMe:  0  1  2  3  4  5')
    ia.reverse()

##para jugador 1  = board[0:6]
##Para jugador 2 = 

def play(turn, board, move):
     ##Verifica si el movimineot es valido
    if(valid_move(board, move) == True):
        over = True

        ##Nos indica la cantidad de fichas que hay en esa parte del board 
        ##y lo iguala a 0 ya que se moveran las fichas
        fichas = board[move]
        board[move] = 0

        ##Mueve las fichas dependiendo de su cantidad en el board
        while fichas > 0:
            move += 1

            if move == 14:
                move = 0

            ##ultima ficha
            if fichas == 1:
                if turn == 0:  
                    ##verifica si hay un turno extra
                    if move == 6:
                        turno = 0
                    else: 
                        turno = 1
                if turn == 1: 
                    if move == 13:
                        turno = 1
                    else: 
                        turno = 0

            if turn == 0: 
                    ##Si estamos en el mancala del enemigo, lo saltamos
                if move == 13:
                    move = 0 
            if turn == 1: 
                    ##Si estamos en el mancala del enemigo, lo saltamos
                if move == 7:
                    move = 0 
             

            if fichas == 1 and board[move] == 0 and turn == 0 and move < 5 and move != 6:
                fichas_robadas = board[12 - move]
                board[6] += fichas_robadas +1
                board[12-move] = 0  
                board[move] = 0
            
            
            elif fichas == 1 and board[move] == 0 and turn == 1 and move > 6 and move != 13:
                fichas_robadas = board[12 - move]
                board[13] += fichas_robadas +1
                board[12-move] = 0  
                board[move] = 0

                ##se agrega una ficha
            else: 

                board[move] += 1  
                
            fichas -= 1

            ##Suma de las primeras 6 casillas
            vacioMe = sum(board[0:6])
            vacioAI = sum(board[7:13])

     
            if vacioAI == 0 or vacioMe == 0:
                over = False 
                board[13] += vacioAI
                board[6] += vacioMe
                clean(board)


            
        return board, turno, over
