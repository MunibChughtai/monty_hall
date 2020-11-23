from doors import Doors

class MontyHall:

    def simulate(self, number_of_simulations):

        win_if_stay = 0

        for simulation in range(0, number_of_simulations):

            game = Doors.setup()
            game.remove_door_with_no_prize()
            
            if game.did_user_select_door_with_prize():
                win_if_stay += 1
        
        print(f"""
              {number_of_simulations} simulations completed:
                if user maintained initial selection they would have won {win_if_stay} times or {round((win_if_stay / number_of_simulations)*100,2)}%,
                if user would have changed their initial selection they would have won {number_of_simulations - win_if_stay} times or {round(((number_of_simulations - win_if_stay) / number_of_simulations)*100,2)}%
              """)
