from source_code.door import Door
from source_code.doors import Doors

def test_put_car_behind_door():
    d1=Door('car')
    #d1.put_object_behind('car')
    assert d1.get_object_behind_door()=='car'

def test_doorset_created_with_1_prize():
    doors=Doors()
    no_of_doors_with_prizes, no_of_doors_without_prizes = doors.set_up_doors(3, 'car')
    assert no_of_doors_with_prizes== 1

def test_door_count_without_prize():
    doors=Doors()
    no_of_doors_with_prizes, no_of_doors_without_prizes = doors.set_up_doors(3, 'car')
    assert no_of_doors_without_prizes== 2

def test_open_door_without_prize():
    doors = Doors()
    doors.set_up_doors(3, 'car')
    door=doors.open_door_without_prize()
    assert door.get_object_behind_door()=='sheep'

def test_is_user_selection_matches_prize():
    doors = Doors()
    doors._index_of_door_with_prize=[0]
    doors._index_of_door_user_selected = [0]
    assert doors.has_user_found_prize()==True

def test_is_user_selection_matches_prize():
    doors = Doors()
    doors._index_of_door_with_prize=[0]
    doors._index_of_door_user_selected = [1]
    assert doors.has_user_found_prize()==False