"""A simple model for global aviation.

Modules:
    aviation: Modelling global fleet using average number of passengers and aircraft data.
"""

__all__ = ("passengers_per_day", "required_global_fleet", "transforms")

from aviation.aviation import passengers_per_day, required_global_fleet

transforms = (passengers_per_day, required_global_fleet)
