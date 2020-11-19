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

@pytest.mark.parametrize('input, expected',
                         [
                           (1,'car'),
                           (2, None)
                          ]
                         )
def test_prize_placed_behind_a_door(input, expected):
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=1
                     )
    assert game_doors._doors[input-1].get_object_behind_door()== expected

def test_number_of_doors_created():
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=1,
                     override_user_selection_index=2)
    assert len(game_doors._doors)==3

@pytest.mark.parametrize('input, expected',
                         [
                           (1,1),
                           (2,2)
                          ]
                         )
def test_player_selection_saved_in_internal_variables(input, expected):
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_user_selection_index=input)
    assert game_doors._index_of_door_user_selected==expected


@pytest.mark.parametrize('input1, input2, expected',
                         [
                           (1,1,2),
                           (1,2,3),
                           (1,3,2),
                           (2,1,3)
                          ]
                         )
def test_door_opened_by_monty(input1, input2, expected):
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=input1,
                     override_user_selection_index=input2)
    assert game_doors._index_of_door_monty_opened==expected

@pytest.mark.parametrize('input, expected',
                         [
                           (1,True),
                           (2,False)
                          ]
                         )
def test_has_user_won(input, expected):
    game_doors = Doors()
    game_doors.setup(number_of_doors=3,
                     override_prize_door_index=1,
                     override_user_selection_index=input)
    assert game_doors.has_user_won() == expected



def test_number_of_simulations_to_run():
    monty_hall=Monty_Hall(80)
    monty_hall.run_simulations()
    assert monty_hall._iterations_completed==80


def test_number_of_wins():
    monty_hall = Monty_Hall()
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=1, override_user_selection_index=1)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=2, override_user_selection_index=2)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=3, override_user_selection_index=2)
    assert monty_hall._number_of_wins==2

def test_number_of_losses():
    monty_hall = Monty_Hall()
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=1, override_user_selection_index=1)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=2, override_user_selection_index=2)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=3, override_user_selection_index=2)
    assert monty_hall._number_of_losses==1

def test_iterations_completed():
    monty_hall = Monty_Hall()
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=1, override_user_selection_index=1)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=2, override_user_selection_index=2)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=3, override_user_selection_index=2)
    assert monty_hall._iterations_completed==3

def test_percentage_win():
    monty_hall = Monty_Hall()
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=1, override_user_selection_index=1)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=2, override_user_selection_index=2)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=3, override_user_selection_index=2)
    monty_hall.update_stats()
    assert monty_hall._percentage_win==66.67

def test_percentage_loss():
    monty_hall = Monty_Hall()
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=1, override_user_selection_index=1)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=2, override_user_selection_index=2)
    monty_hall.simulate_game(Doors(), number_of_locations=3, override_prize_index=3, override_user_selection_index=2)
    monty_hall.update_stats()
    assert monty_hall._percentage_loss==33.33