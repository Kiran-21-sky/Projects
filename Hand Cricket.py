print('Welcome to handcricket!\n')

import random
    
computer_score = 0
player_score = 0
sessions = 0

def player_run():
    runs = int(input('Enter a number between 1 and 10\n'))
    if runs < 1 or runs > 10:
        print('Invalid input. Please enter a number between 1 and 10.')
        return player_run()
    else:
        return runs

def computer_run():
    return random.randint(1,10)

def decision(choice, session):
    global computer_score, player_score, sessions
    if (choice == 1 or choice == 4) and session < 2:
        print(f'You scored {player_score}')
        print('Computer is batting now.\n')
        game(2)
    elif (choice == 2 or choice == 3) and session < 2:
        print(f'Computer scored {computer_score}')
        print('You are batting now.\n')
        game(1)
    else:
        if computer_score > player_score:
            print(f'Computer won by {computer_score - player_score}')
            exit(0)
        elif player_score > computer_score:
            print(f'Congratulations!!! You won by {player_score - computer_score}')
            exit(0)
        else:
            print(f'It\'s a draw. Would you like to play again?\n')
            play_again = int(input(f'If yes, then press \'1\'.\nTo exit, press \'2\'.\n'))
            if play_again == 1:
                player_score=0
                computer_score=0
                sessions=0
                toss()
            else:
                exit(0)
                

def game(choice):
    global computer_score, player_score, sessions
    sessions += 1
    
    while True:
        playe = player_run()
        compu = computer_run()
        if playe == compu:
            print('It\'s an  out...')
            decision(choice, sessions)
            break
        else:
            if choice == 1 :
                player_score += playe
                print(f'You scored {playe} runs\n')
                print(f"Your total runs is {player_score}\n")
            elif choice == 2 :
                computer_score += compu
                print(f"Computer scored {compu} runs\n")
                print(f"Computer's total runs is {computer_score}\n")
            elif choice == 3 :
                computer_score += compu
                print(f"Computer scored {compu} runs\n")
                print(f"Computer's total runs is {computer_score}\n")
            elif choice == 4 :
                player_score += playe
                print(f"You scored {playe} runs\n")
                print(f"Your total runs is {player_score}\n")
                

        if sessions == 2:
                if choice in [1, 4] and player_score > computer_score:
                    decision(choice, sessions)
                    break
                elif choice in [2, 3] and computer_score > player_score:
                    decision(choice, sessions)
                    break

def toss():
    print('Let\'s begin with the toss.\n')
    comp = random.randint(1,2)
    player = int(input('Enter \'1\' for Heads and \'2\' for Tails\n'))
    if comp == player:
        print("You won the toss!")
        chose = int(input('\nChoose \'1\' for batting and \'2\' for bowling\n'))
        if chose == 1:
            print("You chose to bat")
            game(chose)
        else:
            print("You chose to bowl")
            game(chose)
    else:
        print("You lost the toss.")
        chose = random.randint(3,4)
        if chose == 3:
            print('Computer chose to bat.')
            game(chose)
        else:
            print('Computer chose to bowl')
            game(chose)
            
toss()