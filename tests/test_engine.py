import pytest

import aviation
from aviation import _engine as engine


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        ({"passengers_per_year": 5_000_000_000.0}, "passengers_per_year", 5_000_000_000.0),
        ({"required_global_fleet": 25_000.0}, "required_global_fleet", 25_000.0),
        (
            {
                "passengers_per_year": 5_000_000_000.0,
                "days_per_year": 365.25,
            },
            "passengers_per_day",
            13689253.94,
        ),
        (
            {
                "passengers_per_day": 13661202.19,
                "seats_per_aircraft": 180.0,
                "flight_per_aircraft_per_day": 2.0,
            },
            "required_global_fleet",
            37947.78,
        ),
        (
            {
                "days_per_year": 366.0,
                "passengers_per_year": 5_000_000_000.0,
                "seats_per_aircraft": 180.0,
                "flight_per_aircraft_per_day": 2.0,
            },
            "required_global_fleet",
            37947.78,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel, inputs: dict[str, float], output: str, expected: str
) -> None:
    systems_model = engine.SystemsModel(aviation.transforms)
    assert systems_model.evaluate(inputs, output) == pytest.approx(expected)
