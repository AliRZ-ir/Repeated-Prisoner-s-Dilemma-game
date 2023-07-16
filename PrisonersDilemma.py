import random
import matplotlib.pyplot as plt

class Strategy:
    def __init__(self):
        self.history = []

    def choose(self, opponent_history):
        pass

class Random(Strategy):
    def choose(self, opponent_history):
        return random.choice(['C', 'D'])

class TitForTat_C(Strategy):
    def choose(self, opponent_history):
        if opponent_history:
            return opponent_history[-1]
        else:
            return 'C'
class TitForTat_D(Strategy):
    def choose(self, opponent_history):
        if opponent_history:
            return opponent_history[-1]
        else:
            return 'D'

class AlwaysCooperate(Strategy):
    def choose(self, opponent_history):
        return 'C'

class AlwaysDefect(Strategy):
    def choose(self, opponent_history):
        return 'D'

class Periodic(Strategy):
    def __init__(self,Pattern,NumberOfRounds):
        super().__init__()
        self.period = [*Pattern]
        self.Num = NumberOfRounds + 1

    def choose(self, opponent_history):
        self.Num -= 1
        return self.period[self.Num % len(self.period)]

class MyChoice(Strategy):
    def choose(self, opponent_history):
        return input(" please write your choice \"D\"(Defect) or \"C\"(Cooperate) ? ")
    
class Trigger(Strategy):
    def __init__(self):
        super().__init__()
        self.i = 1
    
    def choose(self, opponent_history):
        if opponent_history:
            if self.i == 1:

                if opponent_history[-1] == "D":
                    self.i = 0
                    return "D"
                else:
                    return "C"
            else:
                return "D"
        else:
            return "C"

class Trigger_patience(Strategy):
    def __init__(self):
        super().__init__()
        self.i = 2
    
    def choose(self, opponent_history):
        if opponent_history:
            if self.i > 0:

                if opponent_history[-1] == "D":
                    self.i -= 1
                return "C"

            else:
                return "D"
        else:
            return "C"

class PrisonersDilemma:
    def __init__(self, player1, player2, rounds):
        self.player1 = player1
        self.player2 = player2
        self.rounds = rounds
        self.payoffs = {'CC': (-3, -3), 'CD': (-5, 0), 'DC': (0, -5), 'DD': (-1,-1)}
        self.scores = {'player1': [], 'player2': []}

    def run_game(self):
        for _ in range(self.rounds):
            player1_choice = self.player1.choose(self.player2.history)
            player2_choice = self.player2.choose(self.player1.history)
            if player2_choice == "Exit" or player1_choice == "Exit":
                break
            self.player1.history.append(player1_choice)
            self.player2.history.append(player2_choice)
            score1, score2 = self.payoffs[player1_choice + player2_choice]
            self.scores['player1'].append(score1)
            self.scores['player2'].append(score2)

    def AllocateStrategies(PlayerStrategy):
        if PlayerStrategy == "Random":
            return Random()
        elif PlayerStrategy == "TitForTat_C":
            return TitForTat_C()
        elif PlayerStrategy == "TitForTat_D":
            return TitForTat_D()
        elif PlayerStrategy == "AlwaysDefect":
            return AlwaysDefect()
        elif PlayerStrategy == "AlwaysCooperate":
            return AlwaysCooperate()
        elif PlayerStrategy == "Periodic":
            pattern = input("Please input your patter")
            return Periodic(pattern,NumberOfRounds)
        elif PlayerStrategy == "MyChoice":
            return MyChoice()
        elif PlayerStrategy == "Trigger":
            return Trigger()
        elif PlayerStrategy == "Trigger_patience":
            return Trigger_patience()
        else:
            return MyChoice()
        
    def Help():
        
        print("""
            Strategies
            Random = Choose a Random aciton
            TitForTat_C = repeat the last opponent action and start with Cooperate
            TitForTat_D = repeat the last opponent action and start with Defect
            AlwaysDefect = always play Defect action
            AlwaysCooperate = always play Cooperate action 
            Periodic = play the input pattern repeatedly
            MyChoice = play the input action
            Trigger = play cooperate until the opponent play cooperate when
                      opponent play defect it will play until end Defect
        """)
        

class Analysis:
    def expected_payoff(scores):
        return sum(scores) / len(scores)
    def plot_scores(prisoners_dilemma):
        fig, axs = plt.subplots(2)

        axs[0].plot(prisoners_dilemma.scores['player1'], label='Player 1')
        axs[0].set(ylabel='Score')
        axs[0].legend()

        axs[1].plot(prisoners_dilemma.scores['player2'], label='Player 2')
        axs[1].set(xlabel='Round', ylabel='Score')
        axs[1].legend()

        plt.show()
        
    def plot_history(Prisoners_dilemma):
        fig,axs = plt.subplots(2)

        axs[0].plot(Player1.history, label='Player 1')
        axs[0].set(ylabel='action   ')
        axs[0].legend()

        axs[1].plot(Player2.history, label='Player 2')
        axs[1].set(xlabel='action', ylabel='Score')
        axs[1].legend()

        plt.show()

# Run game
# Player1 = TitForTat_D()
# Player2 = Trigger_Patient()
# NumberOfRounds = 100


print(" Welcome to Prison   esr Dillema Game")
if input("For help write \"Help\":  ") == "Help":
    PrisonersDilemma.Help()

NumberOfRounds = int(input("The number of rounds to play the game: "))
Player1Strategy = input("Please Write player 1 strategy : ")
Player2Strategy = input("Please Write plyaer 2 strategy : ")

Player1 = PrisonersDilemma.AllocateStrategies(Player1Strategy)
Player2 = PrisonersDilemma.AllocateStrategies(Player2Strategy)


game = PrisonersDilemma(Player1, Player2, NumberOfRounds)
game.run_game()


print("Expected payoff player 1:", Analysis.expected_payoff(game.scores['player1']))
print("Expected payoff player 2:", Analysis.expected_payoff(game.scores['player2']))
#Analysis.plot_scores(game)

Analysis.plot_scores(game)
Analysis.plot_history(game)

#print(Player1.history)
#print(Player2.history)
