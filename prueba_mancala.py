from funciones import valid_move, print_board, play, winner, corrida_juego
import random

##Define el board que tendremos y el turno del jugador
      #  0 1 2 3 4 5 6 7 8 9 0 1 2 3
#board = [0,0,0,1,0,0,0,4,4,4,4,4,4,0]
board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
turn = 0
contador= [0,0,0,0,0,0]

over = True
#Inicio del juego
print_board( board[7:14], board[0:7])
while(over):
    if turn == 0 and over == True:
        move = int(input("Ingrese su movimiento (0-5)"))
        if move <5 and  valid_move(board, move): 
            
            board, turn, over = play(0,board, move)
            print("##########################################")
            print("Movimiento nuestro", move)
            print_board( board[7:14], board[0:7])

      
    if turn == 1 and over == True: 
        possible_move = [9,10,11,12,8,7]
        #move = int(input("Ingrese su movimiento (0-5):v "))



        ##MONTE CARLO##
        for i in range(0, 60000):
            move = random.choice(possible_move)
            if valid_move(board, move):
                winner = corrida_juego(board, move)
                print(winner)
                if move == 7 and winner == 1:
                    contador[0]+= 1
                if move == 8  and winner == 1:
                    contador[1]+= 1
                if move == 9  and winner == 1:
                    contador[2]+= 1
                if move == 10  and winner == 1:
                    contador[3]+= 1
                if move == 11  and winner == 1:
                    contador[4]+= 1
                if move == 12  and winner == 1:
                    contador[5]+= 1
      

        print(contador)
        movimiento = max(contador)
        if contador.index(movimiento) == 0:
            board, turn, over = play(1,board, 7)
            print("##########################################")
            print("Movimineto de IA", int(move))
            print_board( board[7:14], board[0:7])
      
        if contador.index(movimiento) == 1:
            board, turn, over = play(1,board, 8)
            print("##########################################")
            print("Movimineto de IA", int(move))
            print_board( board[7:14], board[0:7])
        if contador.index(movimiento) == 2:
            board, turn, over = play(1,board, 9)
            print("##########################################")
            print("Movimineto de IA", int(move))
            print_board( board[7:14], board[0:7])
      
        if contador.index(movimiento) == 3:
            board, turn, over = play(1,board, 10)
            print("##########################################")
            print("Movimineto de IA", int(move))
            print_board( board[7:14], board[0:7])
        if contador.index(movimiento) == 4:
            board, turn, over = play(1,board, 11)
            print("##########################################")
            print("Movimineto de IA", int(move))
            print_board( board[7:14], board[0:7])

        if contador.index(movimiento) == 5:
            board, turn, over = play(1,board, 12)
            print("##########################################")
            print("Movimineto de IA", int(move))
            print_board( board[7:14], board[0:7])
      
   
      

#valid_move(board,12)
#print(corrida_juego(board, 12))