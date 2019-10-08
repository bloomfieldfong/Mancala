
##Valida si el movimiento es valido 
##Parametros: array: estado del jugador, pick: que 
def valid_move(array, pick):
    if pick >= 0 and pick < 6:
        if array[pick] >0 :
            return True
        else: 
            return False
    else:
        return False
    

##Print de board
def print_board(ia, me):
    ia.reverse()
    print('IA   5  4  3  2  1  0\n')
    print(ia[:1], ia[1:7])
    print('   ', me[0:6],me[6:])
    print('\nMe:  0  1  2  3  4  5')
    ia.reverse()