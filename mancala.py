
from funciones import valid_move, print_board

##Define el board que tendremos y el turno del jugador
boardIA = [4,4,4,4,4,4,0]
boardNotIA = [4,4,4,4,4,4,0]
turn = 0

##Suma de las primeras 6 casillas
vacioAI = sum(boardIA[:6])
vacioMe = sum(boardNotIA[:6])


##Inicio del juego
while(vacioAI!= 0 and vacioMe!=0):
    print_board(boardIA, boardNotIA)
    move = input("Ingrese la posicion que desea mover (0-5): \n")
    if(valid_move(boardNotIA, int(move)) == True):
        print("")
    else: 
        print("Movimiento invalido, ingrese otra vez")

    



