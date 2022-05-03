#ASSIGNMENT 3
#Name: Priyal Gulati
#Student ID: 101185010



import connect4
#main function definition
def main():
    size = ''
    while size!='quit':
        size = input("Enter size of game you want to play or quit : ")
        if size.lower()=="quit":
            print("Thanks for playing.")
            break
        else:
            rows, columns = size.split(',')
            rows = int(rows)
            columns = int(columns)
            grid = connect4.makeGrid(rows,columns)
            valid = True
            moves = 0
            while valid:
                if moves == rows*columns:
                    print("The game is a tie.")
                    break
                else:
                    column = int(input("Where does red (X) want to play? "))
                    valid = connect4.play(grid,column,'red')
                    while not valid:
                        if moves == rows*columns:
                            print("The game is a tie.")
                            break
                        else:
                            print("This was an invalid move.")
                            column = int(input("Where does red (X) want to play? "))
                            valid = connect4.play(grid,column,'red')                                      
                    if valid:
                        moves+=1
                        print(connect4.toString(grid))
                        checker = connect4.win(grid,column)
                        if checker == 'empty':
                            if moves == rows*columns:
                                print("The game is a tie.")
                                break
                            else:
                                column = int(input("Where does black (O) want to play? "))
                                valid = connect4.play(grid,column,'black')
                                while not valid :
                                    if moves == rows*columns:
                                        print("The game is a tie.")
                                        break
                                    else:
                                        print("This was an invalid move.")
                                        column = int(input("Where does black (O) want to play? "))
                                        valid = connect4.play(grid,column,'black')                                                           
                                if valid:
                                    moves+=1
                                    print(connect4.toString(grid))
                                    checker = connect4.win(grid,column)
                                    if checker!= 'empty':
                                        print(f'black wins the game after {moves} moves.')
                                    else:
                                        continue
                        else:
                            print(f'red wins the game after {moves} moves.')
                    
#main guard
if __name__=='__main__':
    main()