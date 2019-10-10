from funciones import valid_move, print_board, play, winner, corrida_juego, possible_movess
import random
import copy

# Funciona porque el random es uniforme y esto hace que en muchas 
# iteraciones el valor esperado sea aproximado a 1/6 de la cantidad de iteraciones

##Define el board que tendremos y el turno del jugador
      #  0 1 2 3 4 5 6 7 8 9 0 1 2 3
#board = [0,0,0,1,0,0,0,4,4,4,4,4,4,0]
board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
turn = 0
prueba = [9,10,11,12,8,7]
contador= [0,0,0,0,0,0]
iteracion = 10000
porcentaje = []

over = True
#Inicio del juego
print_board( board[7:14], board[0:7])
while(over):
    
    if turn == 0 and over == True:
        move = int(input("Ingrese su movimiento (0-5): "))
        if move <6 and  valid_move(board, move): 

            ## nos indica quien es el turno
            board, turn, over = play(0,board, move)
            print("##########################################")
            print("Movimiento nuestro", move)
            print_board( board[7:14], board[0:7])

      
    elif turn == 1 and over == True: 
        
        #move = int(input("Ingrese su movimiento (0-5):v "))
        
        ##regresa los posibles movimiento para el board actual
        contador = [0, 0, 0, 0, 0, 0]
        porcentaje = []

        ##MONTE CARLO##
        for i in range(0, iteracion):
                    ## quien fue el ganador de todo el juego que se esta simulando

            try: 
                boardTry = copy.deepcopy(board)
                possible_move = possible_movess(boardTry, prueba)  
                move = random.choice(possible_move)
            
                if move in possible_move:
                    if valid_move(boardTry, move):
                        winner = corrida_juego(boardTry, move)
                                    ##AQUI
                        if move == 7 and winner == 1:
                            contador[0] = contador[0] + winner
                        elif move == 8  and winner == 1:
                            contador[1] = contador[1] + winner
                        elif move == 9  and winner == 1:
                            contador[2] = contador[2] + winner
                        elif move == 10 and winner == 1:
                            contador[3] = contador[3] + winner
                        elif move == 11 and winner == 1:
                            contador[4] = contador[4] + winner
                        elif move == 12 and winner == 1:
                            contador[5] = contador[5] + winner
            except: 
                a =1
        
        

        movimiento = max(contador)
        if valid_move(board, (contador.index(movimiento) + 7)) and turn == 1:
            if contador.index(movimiento) == 0:
                board, turn, over = play(1,board, 7)
                print(turn)
                print("##########################################")
                contador.reverse()
                print(contador)
                print("##########################################")
                print("Movimineto de IA: 7" )
                print_board( board[7:14], board[0:7])

        
            elif contador.index(movimiento) == 1:
                board, turn, over = play(1,board, 8)
                print(turn)
                print("##########################################")
                contador.reverse()
                print(contador)
                print("##########################################")
                print("Movimineto de IA: 8")
                print_board( board[7:14], board[0:7])

            elif contador.index(movimiento) == 2:
                board, turn, over = play(1,board, 9)
                print(turn)
                print("##########################################")
                contador.reverse()
                print(contador)
                print("##########################################")
                print("Movimineto de IA: 9",)
                print_board( board[7:14], board[0:7])

            elif contador.index(movimiento) == 3:
                
                board, turn, over = play(1,board, 10)
                print(turn)
                print("##########################################")
                contador.reverse()
                print(contador)
                print("##########################################")
                print("Movimineto de IA: 10")
                print_board( board[7:14], board[0:7])


            elif contador.index(movimiento) == 4:
                board, turn, over = play(1,board, 11)
                print(turn)
                print("##########################################")
                contador.reverse()
                print(contador)
                print("##########################################")
                print("Movimineto de IA: 11")
                print_board( board[7:14], board[0:7])


            elif contador.index(movimiento) == 5:
                board, turn, over = play(1,board, 12)
                print(turn)
                print("##########################################")
                contador.reverse()
                print(contador)
                print("##########################################")
                print("Movimineto de IA: 12")
                print_board( board[7:14], board[0:7])

    
              
   
      

#valid_move(board,12)
#print(corrida_juego(board, 12))