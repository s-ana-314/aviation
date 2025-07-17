import aviation

days_per_year = 366.0  # leap year

passengers_per_year = 5_000_000_000.0  # note use float
seats_per_aircraft = 180.0  # estimated from observation as 30 rows x 6 seats per row
flight_per_aircraft_per_day = 2.0

passengers_per_day = aviation.passengers_per_day(passengers_per_year, days_per_year)

print(f"{passengers_per_day=:.2f}")  # f string good for formating
