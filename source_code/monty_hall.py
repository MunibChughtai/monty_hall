from source_code.doors import Doors

class Monty_Hall:
    def __init__(self, number_of_iterations = 5):
        self._total_number_of_iterations=number_of_iterations
        self._iterations_completed=0
        self._number_of_wins=0
        self._number_of_losses=0
        self._percentage_win=0
        self._percentage_loss=0

    def update_stats(self):
        self._percentage_win = round(self._number_of_wins/self._iterations_completed*100,2)
        self._percentage_loss = round(self._number_of_losses / self._iterations_completed * 100, 2)


    def simulate_game(self, game_doors, number_of_locations, override_prize_index=False, override_user_selection_index=False ):
        game_doors.setup(number_of_locations, override_prize_index, override_user_selection_index )
        if game_doors.has_user_won():
            self._number_of_wins +=1
        else:
            self._number_of_losses +=1
        self._iterations_completed +=1
        self.update_stats()

    def run_simulations(self):
        for iteration_number in range(self._total_number_of_iterations):
            #self._iterations_completed+=1
            self.simulate_game(Doors(), 3)

        print(f'Iterations Completed: {self._iterations_completed}')
        print(f'Number of Wins: {self._number_of_wins}')
        print(f'Number of losses: {self._number_of_losses}')
        print(f'Percentage Win: {self._percentage_win}')
        print(f'Percentage Loss: {self._percentage_loss}')


