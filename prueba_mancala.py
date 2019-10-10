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
contador= [0,0,0,0,0,0]
iteracion = 60000
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

      
    if turn == 1 and over == True: 
        prueba = [9,10,11,12,8,7]
        #move = int(input("Ingrese su movimiento (0-5):v "))
        boardTry = copy.deepcopy(board)
        ##regresa los posibles movimiento para el board actual
        possible_move = possible_movess(boardTry, prueba)
        

        contador = [0, 0, 0, 0, 0, 0]
        porcentaje = []

        ##MONTE CARLO##
        for i in range(0, iteracion):
          
            try: 
                move = random.choice(possible_move)
                ## si el movimiento es valido
                if (corrida_juego != False ):

                    ## quien fue el ganador de todo el juego que se esta simulando
                    winner = corrida_juego(boardTry, move)
                        ##AQUI
                    if move == 7:
                        contador[0] = contador[0] + 1
                    if move == 8:
                        contador[1] = contador[1] + 1
                    if move == 9:
                        contador[2] = contador[2] + 1
                    if move == 10:
                        contador[3] = contador[3] + 1
                    if move == 11:
                        contador[4] = contador[4] + 1
                    if move == 12:
                        contador[5] = contador[5] + 1
            except:
                a = 0

        
        movimiento = max(contador)

        for j in range(len(contador)):
            porcentaje.append( contador[j] * 100 / iteracion)


        if contador.index(movimiento) == 0:
            board, turn, over = play(1,board, 7)
            print("##########################################")
            porcentaje.reverse()
            print(porcentaje)
            print("##########################################")
            print("Movimineto de IA: 7" )
            print_board( board[7:14], board[0:7])
      
        if contador.index(movimiento) == 1:
            board, turn, over = play(1,board, 8)
            print("##########################################")
            porcentaje.reverse()
            print(porcentaje)
            print("##########################################")
            print("Movimineto de IA: 8")
            print_board( board[7:14], board[0:7])
        if contador.index(movimiento) == 2:
            board, turn, over = play(1,board, 9)
            print("##########################################")
            porcentaje.reverse()
            print(porcentaje)
            print("##########################################")
            print("Movimineto de IA: 9",)
            print_board( board[7:14], board[0:7])
      
        if contador.index(movimiento) == 3:
            board, turn, over = play(1,board, 10)
            print("##########################################")
            porcentaje.reverse()
            print(porcentaje)
            print("##########################################")
            print("Movimineto de IA: 10")
            print_board( board[7:14], board[0:7])
        if contador.index(movimiento) == 4:
            board, turn, over = play(1,board, 11)
            print("##########################################")
            porcentaje.reverse()
            print(porcentaje)
            print("##########################################")
            print("Movimineto de IA: 11")
            print_board( board[7:14], board[0:7])

        if contador.index(movimiento) == 5:
            board, turn, over = play(1,board, 12)
            print("##########################################")
            porcentaje.reverse()
            print(porcentaje)
            print("##########################################")
            print("Movimineto de IA: 12")
            print_board( board[7:14], board[0:7])
            
    
            
      
   
      

#valid_move(board,12)
#print(corrida_juego(board, 12))