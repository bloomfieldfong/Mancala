from funciones import valid_move, print_board, play
import random

##Define el board que tendremos y el turno del jugador
      #  0 1 2 3 4 5 6 7 8 9 0 1 2 3
board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
turn = 0

##Suma de las primeras 6 casillas
vacioAI = sum(board[0:6])
vacioMe = sum(board[7:13])


##Inicio del juego
print_board( board[7:14], board[0:7])
while(vacioAI!= 0 and vacioMe!=0):

    if turn == 0:
        move = int(input("Ingrese su movimiento (0-5)"))
        if move > 5: 
            print("Movimiento invaldio")

        else: 
            board, turn = play(0,board, move)
            print(board)
            print(turn)
