"""Modelling global fleet using average number of passengers and aircraft data."""

import camia_model as model


@model.transform
def passengers_per_day(passengers_per_year: float, days_per_year: float) -> float:
    """The number of passengers per day globally.

    Args:
        passengers_per_year: Number of passengers flying in aircraft globally per year.
        days_per_year: Number of days in that specific year.

    """
    return passengers_per_year / days_per_year


@model.transform
def required_global_fleet(
    passengers_per_day: float,
    seats_per_aircraft: float,
    flight_per_aircraft_per_day: float,
) -> float:
    """The required global fleet per year.

    Args:
        passengers_per_day: Number of passengers per day in modelled year.
        seats_per_aircraft: Number of available seats in one aircraft on average.
        flight_per_aircraft_per_day: Number of flights that one aircraft makes per day
            on average.

    """
    return passengers_per_day / (seats_per_aircraft * flight_per_aircraft_per_day)
