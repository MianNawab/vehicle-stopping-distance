import pytest
import main

def test_kmh_to_ms():
    assert main.kmh_to_ms(36) == 10.0
    assert main.kmh_to_ms(72) == 20.0

   

def test_calculate_reaction_distance():
    assert main.calculate_reaction_distance(1.5, 36) == 15

    assert main.calculate_reaction_distance(2, 72) == 40.0

def test_calculate_braking_distance():
    assert main.calculate_braking_distance(36, 5) == 10.0
    assert main.calculate_braking_distance(72, 5) == 40.0


def test_calculate_braking_distance_invalid_deceleration():
    with pytest.raises(ValueError) :
        main.calculate_braking_distance( 36, 0)
    with pytest.raises(ValueError) :
        main.calculate_braking_distance(36, -5)



def test_calculate_effective_deceleration():
    assert main.calculate_effective_deceleration(9.81, 0.8, 10) == pytest.approx(8.785, rel=1e-3)
    assert main.calculate_effective_deceleration(9.81, 0.5, 0) == pytest.approx(4.905, rel=1e-3)


def test_calculate_stopping_distance():
    reaction_distance, braking_distance, stopping_distance = main.calculate_stopping_distance(36, 1.5, 0, "dry")
    assert reaction_distance == pytest.approx(15)
    assert braking_distance == pytest.approx(6.371, rel=1e-3)
    assert stopping_distance == pytest.approx(21.371, rel=1e-3)

    reaction_distance, braking_distance, stopping_distance = main.calculate_stopping_distance(72, 2, 0, "wet")
    assert reaction_distance == pytest.approx(40)
    assert braking_distance == pytest.approx(40.775, rel=1e-3)
    assert stopping_distance == pytest.approx(80.775, rel=1e-3)

def test_calculate_stopping_distance_invalid():
    with pytest.raises(ValueError):
       main.calculate_stopping_distance(-20, 1.5,0, "dry")
    with pytest.raises(ValueError):
        main.calculate_stopping_distance(36, -1.5, 0, "dry")
    with pytest.raises(ValueError):
        main.calculate_stopping_distance(36, 1.5, -5, "out")
