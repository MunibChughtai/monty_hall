from source_code.doors import Doors

class Monty_Hall:
    def __init__(self, number_of_iterations):
        self._total_number_of_iterations=number_of_iterations
        self._iterations_completed=0
        self._number_of_wins=0
        self._number_of_loses=0
        self._percentage_win=0
        self._percentage_loss=0

    def update_stats(self, game_result):
        None

    def start_a_game(self, doors):
        #doors.setup()
        #result=doors.result()
        #self.update_stats(result)
        None

    def run_simulations(self):
        while self._iterations_completed < self._total_number_of_iterations*2:
            self._iterations_completed+=1
            self.start_a_game(
                                Doors(
                                        number_of_doors=3,
                                        override_prize_door_index=1,
                                        override_user_selection_index=2,
                                        override_host_selection_index=0
                                      )
                              )



