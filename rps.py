#!/usr/bin/env python3
import random

moves = ['rock', 'paper', 'scissors']


class Player:  # we have two classes #1 is Player #2 is  Game

    def __init__(self):
        self.my_move = Player.move(self)
        """To store the move method of class player in the my_move.
        To be accessible by Cycle class.
        It's store Rock at first time."""
        self.their_move = Player.move(self)
        """This will be the same move of
        class at the first time when initlze it."""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RefelctPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Rock, Paper or scissors? ")
            if human_move.lower() in moves:
                return (human_move.lower())
            elif human_move.lower() == 'exit'.lower():
                print("Ok, game stopped")
                exit()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1   # This is the fisrt obj which is HumanPlayer
        self.p2 = p2   # This is the second obj which is RandomPlayer
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        """**Rock** This is move method of HumanPlayer
        class which is self.p1"""
        move2 = self.p2.move()
        """ ALWYES will be the same move of human
        in RefelctPlayer.Because thier_move = Player.move(self)"""

        # This is move method of Computer Player class which is p2
        print(f"You Played {move1}\nOpponent played {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("** TIE **")
        elif move1 == 'rock' and move2 == 'paper':
            self.p2_score += 1
            print("** PLAYER TWO WINS **")
        elif move1 == 'rock' and move2 == 'scissors':
            self.p1_score += 1
            print("** PLAYER ONE WINS **")
        elif move1 == 'paper' and move2 == 'rock':
            self.p1_score += 1
            print("** PLAYER ONE WINS **")
        elif move1 == 'paper' and move2 == 'scissors':
            self.p2_score += 1
            print("** PLAYER TWO WINS **")
        elif move1 == 'scissors' and move2 == 'rock':
            self.p2_score += 1
            print("** PLAYER TWO WINS **")
        elif move1 == 'scissors' and move2 == 'paper':
            self.p1_score += 1
            print("** PLAYER ONE WINS **")

        print(f"Score: Player One {self.p1_score} , Plyer Two {self.p2_score}")

    def play_game(self):  # The game starts from Here!
        print("Game start!")
        for round in range(11):
            print(f"Round {round}:")
            self.play_round()

        if self.p1_score > self.p2_score:
            print(f"The winner is --PLAYER ONE-- with score {self.p1_score}")
        elif self.p1_score < self.p2_score:
            print(f"The winner is --PLAYER TWO-- with score of{self.p2_score}")
        elif self.p1_score == self.p2_score:
            print(f" The score is ** TIE ** ")
        else:
            print(f"No one win :(")

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([Player(), RandomPlayer(),
                                             RefelctPlayer(), CyclePlayer()]))
    game.play_game()
