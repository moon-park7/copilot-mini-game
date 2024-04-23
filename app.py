# Create a game of rock paper scissors on the terminal:
# - The game should be played against the computer
# - The computer should randomly select rock, paper, or scissors
# - The game should prompt the user to select rock, paper, or scissors
# - The game should determine the winner
# - The game should ask the user if they want to continue playing
# - The game should track the number of wins and losses
# - When the user decides to stop playing, the game should print the number of wins and losses
# - The game should inform the player if the option entered is invalid


import random

def rock_paper_scissors():
    wins = 0
    losses = 0
    while True:
        computer = random.choice(['rock', 'paper', 'scissors'])
        user = input('Enter rock, paper, or scissors: ')
        if user not in ['rock', 'paper', 'scissors']:
            print('Invalid option')
            continue
        print(f'Computer: {computer}')
        if user == computer:
            print('It is a tie')
        elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again == 'no':
            print(f'Wins: {wins}, Losses: {losses}')
            break

rock_paper_scissors()

