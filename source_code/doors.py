from source_code.door import Door
from random import randrange

class Doors:
    def __init__(self):
        self._doors=[]
        self._index_of_door_with_prize=''
        self._index_of_door_user_selected=0
        self._index_of_door_host_opened=''

    def set_up_doors(self, number_of_doors, prize):
        self._index_of_door_with_prize = randrange(number_of_doors - 1)
        no_of_doors_with_prizes=0
        no_of_doors_without_prizes=0

        for door_no in range(number_of_doors):
            if door_no == self._index_of_door_with_prize:
                self._doors.append(Door('car'))
                no_of_doors_with_prizes += 1
            else:
                self._doors.append(Door('sheep'))
                no_of_doors_without_prizes += 1
        return (no_of_doors_with_prizes, no_of_doors_without_prizes)

    def open_door_without_prize(self):
        for index, door in enumerate(self._doors):
            if index == self._index_of_door_user_selected or door.get_object_behind_door()=='car':
                continue
            self._index_of_door_host_opened = index
            return door

    def has_user_found_prize(self):
        if self._index_of_door_with_prize == self._index_of_door_user_selected:
            return True
        else:
            return False