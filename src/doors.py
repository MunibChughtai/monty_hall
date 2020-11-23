from door import Door

import random


class Doors:

    @staticmethod
    def setup(number_of_doors=3):
        prize_index = random.randint(0, number_of_doors - 1)
        user_door_selection = random.randint(0, number_of_doors - 1)

        doors = []

        for number in range(0, number_of_doors):
            if number == prize_index:
                doors.append(Door(True))
            else:
                doors.append(Door())

        doors[user_door_selection].is_user_selection = True
        
        return Doors(doors)

    def __init__(self, doors):
        self.doors = doors

    def remove_door_with_no_prize(self):
        for index, door in enumerate(self.doors):
            if not door.is_prize and not door.is_user_selection:
                self.doors.pop(index)
                return

    def did_user_select_door_with_prize(self):
        user_selected_door = [
            door for door in self.doors if door.is_user_selection][0]

        return user_selected_door.is_prize
