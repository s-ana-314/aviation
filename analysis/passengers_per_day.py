"""Analysis to determine the number of passengers per day."""

import camia_engine as engine

import aviation

days_per_year = 365.25
passengers_per_year = 2000000.0

inputs = {
    "days_per_year": days_per_year,
    "passengers_per_year": passengers_per_year,
}
output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)


print(f"{passengers_per_day=:.2f}")  # f string good for formating
