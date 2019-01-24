#если можем сделать выигрышный ход - делаем
def pc_win_move(board, pc_token):
    #выигрышные комбинации
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == pc_token:
            if str(board[each[2]]) not in "XO":
                board[each[2]] = pc_token
                return True
        if board[each[0]] == board[each[2]] == pc_token:
            if str(board[each[1]]) not in "XO":
                board[each[1]] = pc_token
                return True
        if board[each[1]] == board[each[2]] == pc_token:
            if str(board[each[0]]) not in "XO":
                board[each[0]] = pc_token
                return True
    return False

#проверяем, чтобы жалкий человечишка не выиграл скайнет
def pc_not_lose_move(board, player_token, pc_token):
    #выигрышные комбинации
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == player_token:
            if str(board[each[2]]) not in "XO":
                board[each[2]] = pc_token
                return True
        if board[each[0]] == board[each[2]] == player_token:
            if str(board[each[1]]) not in "XO":
                board[each[1]] = pc_token
                return True
        if board[each[1]] == board[each[2]] == player_token:
            if str(board[each[0]]) not in "XO":
                board[each[0]] = pc_token
                return True
    return False

#ход по углам    
def pc_d_turn(board, pc_token):
    diag_coord = (0, 2, 6, 8)
    for each in diag_coord:
        if str(board[each]) not in "XO":
            board[each] = pc_token
            return True
    return False

#ход вокруг центра
def pc_v_turn(board, pc_token):
    v_coord = (1, 3, 5, 7)
    for each in v_coord:
        if str(board[each]) not in "XO":
                    board[each] = pc_token
                    return True
    return False

#ход компьютера
def pc_turn(pc_token, player_token):
    valid = False
    while not valid:
        #сперва смотрим, можем ли мы выиграть
        if pc_win_move(board, pc_token):
            break
        #проверяем, не проиграем ли мы следующим ходом
        if pc_not_lose_move(board, player_token, pc_token):
            break
        #занимаем концы диагонали
        if pc_d_turn(board, pc_token):
            break
        #если центр еще не занят, ступаем туда
        if (str(board[4])) not in "XO":
            board[4] = pc_token
            break
        #ходим вокруг центра
        if pc_v_turn(board, pc_token):
            break
    
#проверяем победу
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

#отрисовка игровой доски
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

#игрок выбирает сторону
def player_side(player_token):
    print("Choose your side: Sith Lord(X), or Jedi Knight(O)")
    valid = False
    while not valid:
        player_token = input()
        if (player_token not in "XO"):
            print("It's 'X' or 'O'")
        else:
            print("You are ", player_token)
            valid = True
    return player_token

#ход человека
def player_turn(player_token):
    valid = False
    while not valid:
        player_answer = input("Choose your next move: ")
        try:
            player_answer = int(player_answer)
        except:
            print ("It's number only")
            continue
        if player_answer >=1 and player_answer <=9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("The target is unavailable")
        else:
            print ("Choose number from 1 to 9.")
            
        
board = list(range(1,10))

#ход в игре
def take_turn(token, player_token, pc_token):
    if token == player_token:
        player_turn(player_token)
        draw_board(board)
    else:
        pc_turn(pc_token, player_token)
        draw_board(board)

def main(board):
    
    player_token = "P"
    player_token = player_side(player_token)
    pc_token = "P"
    if(player_token == "X"):
        pc_token = "O"
    else: pc_token = "X"
    print("Your enemy is: ", pc_token)
    counter = 0;
    win = False
    draw_board(board)
    while not win:
        if counter % 2 == 0:
            take_turn("X", player_token, pc_token)
        else:
            take_turn("O", player_token, pc_token)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "win!")
                draw_board(board)
                win = True
                break
        if counter == 9:
            print ("draw!")
            break

main(board)
