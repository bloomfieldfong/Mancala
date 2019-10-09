
from funciones import valid_move, print_board
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
    

    if (turn == 0):
        ##Pregunta al jugador que movimiento quiere realizar 
        move = int(input("Ingrese la posicion que desea mover (0-5): \n"))

        ##Verifica si el movimineot es valido
        if(valid_move(board[0:6], move) == True):

            ##Nos indica la cantidad de fichas que hay en esa parte del board 
            ##y lo iguala a 0 ya que se moveran las fichas
            fichas = board[move]
            board[move] = 0

            ##Mueve las fichas dependiendo de su cantidad en el board
            while fichas >0:
                ## se mueve una ficha extra
                move += 1
                 ##ultima ficha
                if fichas == 1: 
                    
                    ##verifica si hay un turno extra
                    if move == 6:
                        turn = 0
                    else: 
                        turn = 1
                        print("##########################################")
                       
                ##Si estamos en el mancala del anterior, saltala
                if move == 13:
                    move = 0 
             
                if fichas == 1 and  board[move] == 0 and move<5:
                    print("entro aqui :)")
                    fichas_robadas = board[12 - move]
                    board[12-move] = 0
                    board[6] += fichas_robadas +1
                    board[move] = 0
                    ##se agrega una ficha
                else: 
                    board[move] += 1  
                fichas -= 1

            
            ##Imprime el board con el nuevo estado
            print("Movimiento que realizo el humano")
            print_board( board[7:14], board[0:7])

            ##Nos da un update de si algunos de los dos tableros esta vacio
            
        else: 
            print("Movimiento invalido, ingrese otra vez")

            vacioAI = sum(board[0:6])
            vacioMe = sum(board[7:13])
    
    if (turn ==1):
        possible_move = [9,10,11,12,8,7]
        move = random.choice(possible_move)
        
        if(valid_move(board[7:13], move) == True):

            ##Nos indica la cantidad de fichas que hay en esa parte del board 
            ##y lo iguala a 0 ya que se moveran las fichas
            fichas = board[move]
            board[move] = 0

            ##Mueve las fichas dependiendo de su cantidad en el board
            while fichas >0:
                ## se mueve una ficha extra
                move += 1

                if move == 14:
                    move = 0
                ##Si estamos en el mancala del anterior, saltala
                if move == 6:
                    move = 8 
                
                
                ##verifica si hay un turno extra
                if fichas == 1:
                    if move == 13:
                        turn = 1
                    else: 
                        turn = 0
                        print("##########################################")
          
               
                if fichas == 1 and  board[move] == 0 and move >6:
                    fichas_robadas = board[12-move]
                    board[12-move] = 0
                    board[13] += fichas_robadas +1
                    board[move] = 0
                ##se agrega una ficha
                else: 
                    board[move] += 1

                fichas -= 1
            
            ##Imprime el board con el nuevo estado
            print("Movimiento que realizo el IA")
            print_board( board[7:14], board[0:7])

            ##Nos da un update de si algunos de los dos tableros esta vacio
            vacioAI = sum(board[0:6])
            vacioMe = sum(board[7:13])
        
        else: 
            move = random.choice(possible_move)




