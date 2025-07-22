def passengers_per_day(passengers_per_year, days_per_year):
    """The number of passengers per day globally."""
    return passengers_per_year / days_per_year


def required_global_fleet(passengers_per_day, seats_per_aircraft, flight_per_aircraft_per_day):
    return passengers_per_day / (seats_per_aircraft * flight_per_aircraft_per_day)
