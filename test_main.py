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
    with pytest.raises(ValueError):
        main.calculate_braking_distance(36, 0)
    with pytest.raises(ValueError):
        main.calculate_braking_distance(36, -5)


def test_calculate_effective_deceleration():
    assert main.calculate_effective_deceleration(9.81, 0.8, 10) == pytest.approx(
        8.785, rel=1e-3
    )
    assert main.calculate_effective_deceleration(9.81, 0.5, 0) == pytest.approx(
        4.905, rel=1e-3
    )


def test_calculate_stopping_distance():
    reaction_distance, braking_distance, stopping_distance = (
        main.calculate_stopping_distance(36, 1.5, 0, "dry")
    )
    assert reaction_distance == pytest.approx(15)
    assert braking_distance == pytest.approx(6.371, rel=1e-3)
    assert stopping_distance == pytest.approx(21.371, rel=1e-3)

    reaction_distance, braking_distance, stopping_distance = (
        main.calculate_stopping_distance(72, 2, 0, "wet")
    )
    assert reaction_distance == pytest.approx(40)
    assert braking_distance == pytest.approx(40.775, rel=1e-3)
    assert stopping_distance == pytest.approx(80.775, rel=1e-3)


def test_calculate_stopping_distance_invalid():
    with pytest.raises(ValueError):
        main.calculate_stopping_distance(-20, 1.5, 0, "dry")
    with pytest.raises(ValueError):
        main.calculate_stopping_distance(36, -1.5, 0, "dry")
    with pytest.raises(ValueError):
        main.calculate_stopping_distance(36, 1.5, -5, "out")


def test_calculate_stopping_distances():
    speeds_kmh = [30, 50, 80]
    reaction_time = 1.5
    gradient_percent = 0
    friction_type = "dry"
    stop_distances = main.calculate_stopping_distances(
        speeds_kmh, reaction_time, gradient_percent, friction_type
    )
    assert len(stop_distances) == 3
    for result in stop_distances:
        assert len(result) == 3  # Each tuple should have 3 elements
        #:reaction_distance, braking_distance, stopping_distance

        assert result[2] == result[0] + result[1]  # total stopping distance should be
        # sum of reaction and braking distance


def test_calculate_effective_deceleration_invalid():
    with pytest.raises(ValueError):
        main.calculate_effective_deceleration(9.81, 0.8, -200)


def test_calculate_stopping_distance_invalid_gradient():
    with pytest.raises(ValueError):
        main.calculate_stopping_distance(36, 1.5, -5, "dry")


def test_calculate_stopping_distance_for_multiple_road_conditions():
    speeds = [30, 50]
    conditions = ["dry", "wet"]

    result = main.calculate_stopping_distance_for_multiple_road_conditions(
        speeds, 1.5, 0, conditions
    )

    assert len(result) == 2
    assert result[0][0] == "dry"
    assert result[1][0] == "wet"
    assert len(result[0][1]) == 2
    assert len(result[1][1]) == 2


def test_plotting_stopping_distances():
    data = [
        ("dry", [(1, 2, 3), (4, 5, 9)]),
        ("wet", [(2, 3, 5), (5, 6, 11)]),
    ]

    result = main.plotting_stopping_distances(data)

    assert result == {
        "dry": [3, 9],
        "wet": [5, 11],
    }
