# Rock-paper-scissors-game
Rock paper scissors game in python using OOP with Udacity Nanodgree.

## About the game
The game has two players. In a single round of the game, each player secretly chooses one of three moves, or "throws" — rock, paper, or scissors. Then, players reveal their moves at the same time. If both players picked the same move, there is no winner. Otherwise, rock beats scissors; paper beats rock; and scissors beat paper. Players can play a single round, or "best of three", or any number of other options.

## Tools and Technology:
* python language
* Visual Studio Code

## About the project
The project has 4 class in addation to human class, each class has diffrent strartgy to play the game with a human:
1. 'Rock' Stratgy. 
2. Randomly Stratgy.
3. Reflecting Stratgy.
4. Cycle Stratgy.

- For HumanPlayer class, it's asks the human user what move to make.
- The starter RockPlayer class always plays 'rock'.
- The RandomPlayer Class it's chooses its move at random. It should return one of 'rock', 'paper', or 'scissors' at random.
- The ReflectPlayer Class it's remembers what move the opponent played last round, and plays that move this round
- The CyclePlayer Class it's remembers what move it played last round, and cycles through the different moves. (If it played 'rock' this round, it should play 'paper' in the next round.)

In addation, The game has 10 rounds, displays the outcome of each round, and keeps score for both players and at the end of the game it's announce the winner.

**#Note:** Program will choses an object rangomly from these 4 class.
