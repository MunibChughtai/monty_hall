from source_code.door import Door
from random import randrange
import random

class Doors:
    def __init__(self):
        self._doors=[]
        self._index_of_door_with_prize=''
        self._index_of_door_user_selected=False

    def _line_up_doors(self, number_of_doors):
        for door_no in range(number_of_doors):
            self._doors.append(Door())

    def _place_prize_behind_random_door(self, override_random_door=False):
        if override_random_door:
            self._index_of_door_with_prize = override_random_door
        else:
            self._index_of_door_with_prize=random.randint(0, len(self._doors)-1)

    def _player_guessing_door_with_prize(self, override_random_door=False):
        if override_random_door:
            self._index_of_door_user_selected = override_random_door
        else:
            self._index_of_door_user_selected = random.randint(0, len(self._doors) - 1)

    def setup(self, number_of_doors, override_prize_door_index=False, override_user_selection_index=False):
        self._line_up_doors(number_of_doors)
        self._place_prize_behind_random_door(override_prize_door_index)
        self._player_guessing_door_with_prize(override_user_selection_index)

    def is_user_selection_match_prize_location(self):
        return self._index_of_door_with_prize == self._index_of_door_user_selected