days_per_year = 365.0

passengers_per_year= 6_000_000_000.0 #note use float 
seats_per_aircraft= 180.0
flight_per_aircraft_per_day= 2.0

passengers_per_day= passengers_per_year/days_per_year
required_global_fleet= passengers_per_day/ (seats_per_aircraft*flight_per_aircraft_per_day)

print(f"{required_global_fleet=:.2f}") #f string good for formating