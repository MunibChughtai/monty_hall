import pytest
from source_code.door import Door
from source_code.doors import Doors
from source_code.monty_hall import Monty_Hall

@pytest.mark.parametrize('input, expected',
                         [
                           (None, None),
                           ('car','car')
                          ]
                         )
def test_get_object_behind_door(input, expected):
    d1 = Door(input)
    assert d1.get_object_behind_door()== expected

def test_line_up_doors():
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=1,
                     override_user_selection_index=2)
    assert len(game_doors._doors)==3

def test_place_prize_behind_random_door():
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=1,
                     override_user_selection_index=2)
    assert game_doors._index_of_door_with_prize==1

def test_player_guessing_door_with_prize():
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=1,
                     override_user_selection_index=2)
    assert game_doors._index_of_door_user_selected==2

def test_is_user_selection_match_prize_location():
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=1,
                     override_user_selection_index=2)
    assert game_doors.is_user_selection_match_prize_location()==False

def test_number_of_simulations_to_run():
    monty_hall=Monty_Hall(80)
    monty_hall.run_simulations()
    assert monty_hall._iterations_completed==160

def get_game_result():
    monty_hall = Monty_Hall(3)

'''
def test_number_of_simulations_to_run():
    monty_hall=Monty_Hall(80)
    monty_hall.run_simulations()
    assert monty_hall._iterations_completed==160

def test_number_of_wins():
    monty_hall=Monty_Hall(2)
    game_doors = Doors()
    monty_hall.run_simulations(game_doors)
'''
#--------

