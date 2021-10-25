import random
x = 0
computer_score = 0
player_score = 0
print("***************************** Welcome *****************************")
print("              Stone : 1 || Paper : 2 || Scissor : 3")
print("________________________________________________________________\n\n")

while x<3:
    print("\t\t\t\t\t\tTurns left : ",x)
    choice = int(input("Enter your choice : "))
    print("                     You      ::      Computer")
    print("________________________________________________________________")
    x += 1

    if choice == 1:
        print ("                    Stone     ::     ",end="")
    elif choice == 2:
        print("                    Paper     ::     ",end="")
    elif choice ==3:
        print("                   Scissor    ::     ",end="")
    else:
        print("You've entered wrong input")
        x -=1
        continue
    cmp = random.randint(1,3)
    if cmp == 1:
        print(" Stone")
    elif cmp == 2:
        print(" Paper")
    elif cmp ==3:
        print("Scissor")

    #scoring     1 = stone 2 = paper 3=scissor
    print("                 ----------------------------")
    if choice == 1 and cmp == 2:
        print ("Result :            Lose      ::      Win")
        computer_score += 1
    elif choice == 1 and cmp == 3:
        print ("Result :            Win       ::      Lose")
        player_score += 1

    elif choice == 2 and cmp == 3:
        print ("Result :            Lose      ::      Win")
        computer_score += 1

    elif choice == 2 and cmp == 1:
        print ("Result :            Win       ::      Lose")
        player_score += 1

    elif choice == 3 and cmp == 1:
        print ("Result :            Lose      ::      Win")
        computer_score += 1
    elif choice == 3 and cmp == 2:
        print ("Result :            Win       ::      Lose")
        player_score += 1


    else:
        print ("Result :            Win       ::      Win")
        player_score += 1
        computer_score += 1


    print (f"Score :              {player_score}        ::       {computer_score}" )

print("****************************************************************")
print(f"Final Score :        {player_score}        ::       {computer_score}")
print("****************************************************************")

if computer_score > player_score:
    print("                    COMPUTER WIN")
elif computer_score < player_score:
    print("                       YOU WIN")
else:
    print("                     MATCH TIED")