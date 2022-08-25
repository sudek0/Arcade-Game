
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

l_ast=['*']*y
l_space=[' ']*y

game_board=[]
for i in range(x):
    game_board.append(l_ast.copy())
for i in range(g):
    game_board.append(l_space.copy())

if x > 0:
    for i in game_board:                                #GAMEBOARD
        for j in i:
            print(j, end='')
        print()

spaceship=[' ']*y
if y%2 == 0:
    ship_position= y//2-1
else:
    ship_position= y//2
spaceship[ship_position]="@"

if x>0:
    for i in spaceship:
        print(i, end='')
    print()
    print("-" * 72)

time = 0
barbunya=True

if x==0:
    print("YOU WON!")
    for i in game_board:
        for j in i:
            print(j,end='')
        print()
    for k in spaceship:
        print(k,end='')
    print()
    print("-" * 72)
    barbunya=False

while barbunya==True:
    inp_action = input('Choose your action!\n')
    action = inp_action.lower()

    if action == 'exit':                                               #EXIT
        for a in game_board:
            for b in a:
                print(b, end='')
            print()
        for a in spaceship:
            print(a, end='')
        print()
        print("-" * 72)
        break

    time+=1
                                                                        #LEFT
    if action=='left':
        spaceship = [' '] * y
        if ship_position>0:
            ship_position -= 1
        else:
            pass
        spaceship[ship_position] = '@'
                                                                        #RIGHT
    elif action == 'right':
        spaceship = [' '] * y
        if ship_position < y-1:
            ship_position += 1
        else:
            pass
        spaceship[ship_position] = '@'
                                                                         #FIRE
    elif action=='fire':
        for i in range(1,len(game_board)+1):
            if game_board[-i][ship_position] == '*':
                game_board[-i][ship_position]= ' '
                break
            else:
                game_board[-i][ship_position]='|'
                for a in game_board:
                    for b in a:
                        print(b, end='')
                    print()
                game_board[-i][ship_position] = ' '
                for a in spaceship:
                    print(a,end='')
                print()
                print('-' * 72)

    a=True
    for i in game_board:
        if '*' in i:
            a=False
    if a==True:
        print("YOU WON!")
        for i in game_board:
            for j in i:
                print(j, end="")
            print()
        for k in spaceship:
            print(k, end="")
        print()
        print("-" * 72)
        break

                                                                         #TIME
    if time % 5 == 0:

        if "*" in game_board[-1]:
            print("GAME OVER")
            for i in game_board:
                for j in i:
                    print(j, end="")
                print()
            for k in spaceship:
                print(k, end="")
            print()
            print("-" * 72)
            break

        else:
            game_board.pop(-1)
            game_board.insert(0, [' '] * y)

    for i in game_board:
        for j in i:
            print(j, end="")
        print()
    for k in spaceship:
        print(k, end="")
    print()
    print("-" * 72)


ast_left = 0
for a in game_board:
    ast_left += a.count("*")

print("YOUR SCORE: ", str(x*y-ast_left))


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
