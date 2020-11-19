from source_code.door import Door
from random import randrange
import random

class Doors:
    def __init__(self):
        self._doors=[]
        self._index_of_door_monty_opened=''
        self._index_of_door_user_selected=False

    def setup(self, number_of_doors, override_prize_door_index=False, override_user_selection_index=False):
        door_index_with_prize = self._select_random_door_for_prize(number_of_doors, override_prize_door_index)
        self._line_up_doors(number_of_doors, door_index_with_prize)
        self._select_random_door_player_selected(override_user_selection_index)
        self.get_monty_door()

    def _select_random_door_for_prize(self, number_of_doors, override_random_door=False):
        if override_random_door:
            return override_random_door
        else:
            return random.randint(1, number_of_doors)

    def _line_up_doors(self, number_of_doors, door_index_with_prize):
        for door_no in range(1,number_of_doors+1):
            if door_no == door_index_with_prize:
                self._doors.append(Door('car'))
            else:
                self._doors.append(Door())

    def _select_random_door_player_selected(self, override_random_door=False):
        if override_random_door:
            self._index_of_door_user_selected = override_random_door
        else:
            self._index_of_door_user_selected = random.randint(1, len(self._doors))


    def get_monty_door(self):
        for door in range(1, len(self._doors)+1):
            if door == self._index_of_door_user_selected or self._doors[door-1].get_object_behind_door()=='car':
                continue
            else:
                self._index_of_door_monty_opened = door
                return door

    def has_user_won(self):
        if self._doors[self._index_of_door_user_selected-1].get_object_behind_door()=='car':
            return True
        else:
            return False