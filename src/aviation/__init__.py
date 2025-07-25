"""A simple model for global aviation.

Modules:
    aviation: Modelling global fleet using average number of passengers and aircraft data.
    demand: Modelling growth for global demand for aviation.
"""

__all__ = (
    "DemandGrowthModel",
    "passengers_per_day",
    "required_global_fleet",
    "transforms",
)

from aviation.aviation import passengers_per_day, required_global_fleet
from aviation.demand import (
    DemandGrowthModel,
    demand_growth_model,
    demand_growth_rate,
    passengers_per_year,
)

transforms = (
    demand_growth_model,
    passengers_per_day,
    required_global_fleet,
    demand_growth_rate,
    passengers_per_year,
)
