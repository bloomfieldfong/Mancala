from funciones import valid_move, print_board, play, winner, corrida_juego
import random

##Define el board que tendremos y el turno del jugador
      #  0 1 2 3 4 5 6 7 8 9 0 1 2 3
##board = [0,0,0,1,0,0,0,4,4,4,4,4,4,0]
board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
turn = 0


# over = True
# #Inicio del juego
# print_board( board[7:14], board[0:7])
# while(over):
#     if turn == 0 and over == True:
#         move = int(input("Ingrese su movimiento (0-5)"))
#         if move > 5: 
#             print("Movimiento invaldio")

#         else: 
#             board, turn, over = play(0,board, move)
#             print("##########################################")
#             print("Movimiento nuestro", move)
#             print_board( board[7:14], board[0:7])

#     if turn == 1 and over == True: 
#         possible_move = [9,10,11,12,8,7]
#         move = int(input("Ingrese su movimiento (0-5):v "))

#         ##MONTE CARLO##
#         move = random.choice(possible_move)
#         if  move > 6 and move < 13:
#             board, turn, over = play(1,board, move)
#             print("##########################################")
#             print("Movimineto de IA", int(move))
#             print_board( board[7:14], board[0:7])
    
corrida_juego(board, 12)