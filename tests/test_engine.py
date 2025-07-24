import camia_engine as engine
import pytest
import pytest_camia
from camia_model.units import day, year

import aviation
from aviation.units import aircraft, journey, passenger


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        (
            {"passengers_per_year": 5_000_000_000.0 * passenger / year},
            "passengers_per_year",
            5_000_000_000.0 * passenger / year,
        ),
        ({"required_global_fleet": 25_000.0}, "required_global_fleet", 25_000.0),
        (
            {
                "passengers_per_year": 5_000_000_000.0 * passenger / year,
            },
            "passengers_per_day",
            13689253.94 * passenger / day,
        ),
        (
            {
                "passengers_per_day": 13661202.19 * passenger / day,
                "seats_per_aircraft": 180.0 * passenger / aircraft,
                "flight_per_aircraft_per_day": 2.0 * journey / (aircraft * day),
            },
            "required_global_fleet",
            37947.0 * aircraft,
        ),
        (
            {
                "passengers_per_year": 5_000_000_000.0 * passenger / year,
                "seats_per_aircraft": 180.0 * passenger / aircraft,
                "flight_per_aircraft_per_day": 2.0 * journey / (aircraft * day),
            },
            "required_global_fleet",
            38025.0 * aircraft,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel, inputs: dict[str, float], output: str, expected: str
) -> None:
    systems_model = engine.SystemsModel(aviation.transforms)
    assert systems_model.evaluate(inputs, output) == pytest_camia.approx(expected, atol=1.0)
