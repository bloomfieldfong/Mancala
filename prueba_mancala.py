from funciones import valid_move, print_board, play
import random

##Define el board que tendremos y el turno del jugador
      #  0 1 2 3 4 5 6 7 8 9 0 1 2 3
board = [0,0,1,0,0,0,0,4,4,4,4,4,4,0]
turn = 0

##Suma de las primeras 6 casillas
vacioAI = sum(board[0:6])
vacioMe = sum(board[7:13])

fin = True
##Inicio del juego
print_board( board[7:14], board[0:7])
while(fin):
    if turn == 0:
        move = int(input("Ingrese su movimiento (0-5)"))
        if move > 5: 
            print("Movimiento invaldio")

        else: 
            board, turn, over = play(0,board, move)
            if over == False:
                fin = False
            print("##########################################")
            print("Movimiento nuestro", move)
            print_board( board[7:14], board[0:7])

    if turn == 1: 
        possible_move = [9,10,11,12,8,7]
        move = int(input("Ingrese su movimiento (0-5):v "))
        ##move = random.choice(possible_move)
        print(valid_move(board, move))
        if  move > 6 and move < 13:
            board, turn, over = play(1,board, move)
            if over == False:
                fin = False
            print("##########################################")
            print("Movimineto de IA", int(move))
            print_board( board[7:14], board[0:7])


    

