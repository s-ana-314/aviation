"""Analysis to determine the required global fleet."""

import camia_engine as engine
from camia_model.units import day, year

import aviation
from aviation.units import aircraft, journey, passenger

days_per_year = 366.0 * day / year
passengers_per_year = 5_000_000_000.0 * passenger / year
seats_per_aircraft = 180.0 * passenger / aircraft
flight_per_aircraft_per_day = 2.0 * journey / (aircraft * day)

inputs = {
    "passengers_per_year": passengers_per_year,
    "days_per_year": days_per_year,
    "seats_per_aircraft": seats_per_aircraft,
    "flight_per_aircraft_per_day": flight_per_aircraft_per_day,
}
output = "required_global_fleet"

systems_model = engine.SystemsModel(aviation.transforms)
required_global_fleet = systems_model.evaluate(inputs, output)

passengers_per_day = aviation.passengers_per_day(passengers_per_year, days_per_year)
required_global_fleet = aviation.required_global_fleet(
    passengers_per_day, seats_per_aircraft, flight_per_aircraft_per_day
)

print(f"{required_global_fleet=!s}")  # f string good for formating
