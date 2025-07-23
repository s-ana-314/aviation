"""Analysis to determine the number of passengers per day."""

import camia_engine as engine
from camia_model.units import day, year

import aviation
from aviation.units import passenger

days_per_year = 365.25 * day / year
passengers_per_year = 2000000.0 * passenger / year

inputs = {
    "days_per_year": days_per_year,
    "passengers_per_year": passengers_per_year,
}
output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)


print(f"{passengers_per_day.value=:2f} {passengers_per_day.unit=!s}")  # f string good for formating
