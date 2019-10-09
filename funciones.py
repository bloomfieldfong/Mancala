import random
##Valida si el movimiento es valido 
##Parametros: array: estado del jugador, pick: que 
def valid_move(array, pick):
    if array[pick] >0 :
        return True
    else: 
        return False

##Limpia el board, esto se utiliza cuando termina el juego
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
##Para jugador 2 =  board[7:13]
## return board, turno, over
## board actualizado
## turno de la persona
## si termino el juego 
def play(turn, board, move):
    
    vacioAI = sum(board[0:6])
    vacioMe = sum(board[7:13])


    if(vacioAI!= 0 and vacioMe!=0): ##Verifica si el movimineot es valido
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
                    ## verifica si esta en su mancala para darle turno extra
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
                
                ## si es ultima y board esta en 0 y es mi turno y estoy en mi rango y el movimieto no es mi mancala
                ## roba 
                if fichas == 1 and board[move] == 0 and turn == 0 and move <= 5 and move != 6:
                    ##fichas del espejo
                    fichas_robadas = board[12 - move]
                    ## fichas robadas  mas la mia 
                    board[6] += fichas_robadas +1

                    ## se quitan las fichas
                    board[12-move] = 0  
                    board[move] = 0
                
                ## mismo pero para la AI
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

                ## si hay alguien que ya termino
                if vacioAI == 0 or vacioMe == 0:
                    ## se acabo
                    over = False 
                    ## se agregan las fichas a nuestros mancalas
                    board[13] += vacioAI
                    board[6] += vacioMe
                    clean(board)
            return board, turno, over

## quien gano
def winner(board):
    ## si gana el humano retorna 0
    if board[6] > board[13]:
        return 0
    ## si gana el ia retorna 1
    if board[13] > board[6]:
        return 1
    ## si es empate
    if board[13] == board[6]:
        return 2

## corrida de un juego completo a partir un board y el primer movimiento de la IA
def corrida_juego(board, move):

    ## turno del ia
    turn = 1

    ## posibles moviminetos para cada jugador
    human_choice = [0,1,2,3,4,5]
    ia_choice = [7,8,9,10,11,12]
    
    ## verifica si el movimiento es valido sobre el board actual
    if valid_move(board, move):
        ## realiza un turno si es verdadero 
        board, turn, over = play(turn, board, move)
    else: 
        return False
    ## cuando no termina el juego aun 
    while over == True:

        ## si es turno del humano
        if turn == 0 and over == True:
            ##realiza un movimiento random sobre las opciones anteriores
            move = random.choice(human_choice)

            ## si el movimineto es valido
            if valid_move(board, move):
                ## si el movimiento esta en nuestro rango
                if move <= 5: 
                    ## realiza un turno 
                    board, turn, over = play(0, board, move)

        ## si es turno del ia
        if turn == 1 and over == True: 

            ## realiza un movimiento random sobre las opcioens anteriores
            move = random.choice(ia_choice)
            ## valida el movimineto
            if valid_move(board, move):
                if  move > 6 and move < 13:
                    ##hace movimiento
                    board, turn, over = play(1, board, move)

    ## retorna quien gano con el board terminado
    return winner(board)


## posibles movimientos
def possible_movess(board, array):
    yei = []
    if valid_move(board, array[0]) == True:
        yei.append(array[0])    
    if valid_move( board, array[1]) == True:
        yei.append(array[1])
    if valid_move( board, array[2]) == True:
        yei.append(array[2])
    if valid_move( board, array[3]) == True:
        yei.append(array[3])
    if valid_move( board, array[4]) == True:
        yei.append(array[4])
    if valid_move( board, array[5]) == True:
        yei.append(array[5])
    return yei


