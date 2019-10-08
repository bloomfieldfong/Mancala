
from funciones import valid_move, print_board

##Define el board que tendremos y el turno del jugador

board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
turn = 0

##Suma de las primeras 6 casillas
vacioAI = sum(board[0:6])
vacioMe = sum(board[7:13])


##Inicio del juego
print_board( board[7:14], board[0:7])
while(vacioAI!= 0 and vacioMe!=0):
    print(vacioAI)
    print(vacioMe)
    move = int(input("Ingrese la posicion que desea mover (0-5): \n"))
    if(valid_move(board[0:6], move) == True):
        fichas = board[move]
        board[move] = 0
        for i in range(fichas):
            move = move+1
            board[move] += 1
            
        print_board( board[7:14], board[0:7])

        vacioAI = sum(board[0:6])
        vacioMe = sum(board[7:13])
    else: 
        print("Movimiento invalido, ingrese otra vez")





