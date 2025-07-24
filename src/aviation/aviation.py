"""Modelling global fleet using average number of passengers and aircraft data."""

import typing

import camia_model as model
from camia_model.units import Quantity, day, year

from aviation.units import aircraft, journey, passenger


@model.transform
def passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> typing.Annotated[Quantity, passenger / day]:
    """The number of passengers per day globally.

    Args:
        passengers_per_year: Number of passengers flying in aircraft globally per year.
        days_per_year: Number of days in that specific year.

    """
    return passengers_per_year.convert_to(passenger / day)


@model.transform
def required_global_fleet(
    passengers_per_day: typing.Annotated[Quantity, passenger / day],
    seats_per_aircraft: typing.Annotated[Quantity, passenger / aircraft],
    flight_per_aircraft_per_day: typing.Annotated[Quantity, journey / (aircraft * day)],
) -> typing.Annotated[Quantity, aircraft]:
    """The required global fleet per year.

    Args:
        passengers_per_day: Number of passengers per day in modelled year.
        seats_per_aircraft: Number of available seats in one aircraft on average.
        flight_per_aircraft_per_day: Number of flights that one aircraft makes per day
            on average.

    """
    aircraft_per_journey = 1.0 * aircraft / journey
    return passengers_per_day / (
        seats_per_aircraft * flight_per_aircraft_per_day * aircraft_per_journey
    )
