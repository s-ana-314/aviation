import typing

import pytest
import pytest_camia
from camia_model.units import Quantity, day, year

from aviation.aviation import passengers_per_day, required_global_fleet
from aviation.units import aircraft, journey, passenger


@pytest.mark.parametrize(
    ("passengers_per_year", "expected_passengers_per_day"),
    (
        (365_000_000.0 * passenger / year, 999_315.0 * passenger / day),
        (732_000_000.0 * passenger / year, 2_004_106.0 * passenger / day),
    ),
)
def test_passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
    expected_passengers_per_day: typing.Annotated[Quantity, passenger / day],
) -> None:
    assert passengers_per_day(passengers_per_year) == pytest_camia.approx(
        expected_passengers_per_day, atol=1.0
    )


def test_required_global_fleet() -> None:
    passengers_per_year = 5_000_000_000.0 * passenger / year
    seats_per_aircraft = 180.0 * passenger / aircraft
    flight_per_aircraft_per_day = 2.0 * journey / (aircraft * day)

    expected_required_global_fleet = 38_025.0 * aircraft

    result = required_global_fleet(
        passengers_per_day(passengers_per_year),
        seats_per_aircraft,
        flight_per_aircraft_per_day,
    )
    assert result == pytest_camia.approx(expected_required_global_fleet, atol=1.0)
