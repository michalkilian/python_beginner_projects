import random


class Game:
    def __init__(self):
        self.score = [0, 0]
        self.options = ["Rock", "Paper", "Scissors"]
        self.welcome_message()

    def welcome_message(self):
        print("Welcome in Rock Paper Scissors Game\n"
              "Actual score:\nComputer", self.score[0], "You", self.score[1])
        self.play_game()

    def play_game(self):
        player_choice = input("Input your choice: ").capitalize()
        computer_choice = self.options[random.randint(0, 2)]
        if player_choice not in self.options:
            print("Type Rock, Paper or Scissors")
            self.play_game()
        else:
            if player_choice == computer_choice:
                print("Computer picks", computer_choice, "it's a tie!")
                self.play_again()
            else:
                if player_choice == "Rock":
                    if computer_choice == "Paper":
                        print("Computer picks Paper and wins!")
                        self.score[0] += 1
                    else:
                        print("Computer picks Scissors and loses!")
                        self.score[1] += 1
                    self.play_again()
                elif player_choice == "Paper":
                    if computer_choice == "Scissors":
                        print("Computer picks Scissors and wins!")
                        self.score[0] += 1
                    else:
                        print("Computer picks Rock and loses!")
                        self.score[1] += 1
                    self.play_again()
                else:
                    if computer_choice == "Rock":
                        print("Computer picks Rock and wins!")
                        self.score[0] += 1
                    else:
                        print("Computer picks Paper and loses!")
                        self.score[1] += 1
                    self.play_again()

    def play_again(self):
        print("Do you want to play again?")
        while True:
            answer = input("y/n ")
            if answer == 'y':
                self.welcome_message()
            elif answer == 'n':
                exit(0)


game = Game()
