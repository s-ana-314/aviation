"""Growth in global aviation."""

__all__ = (
    "DemandGrowthModel",
    "demand_growth_model",
    "passengers_per_year",
)

import enum
import typing

import camia_model as model
from camia_model.units import DIMENSIONLESS, Quantity, percent, year

from aviation.units import passenger

PASSENGER_PER_YEAR_2025 = 5_000_000.0 * passenger / year


@enum.unique
class DemandGrowthModel(enum.Enum):
    """Different models used for demand growth."""

    EXPONENTIAL = enum.auto()
    LINEAR = enum.auto()
    CONSTANT = enum.auto()


@model.transform
def demand_growth_model() -> DemandGrowthModel:
    """The default demand growth model is exponenital."""
    return DemandGrowthModel.EXPONENTIAL


@model.transform
def demand_growth_rate() -> typing.Annotated[Quantity, percent / year]:
    """Expected growth rate for number of passengers starting from 2025."""
    return 4.0 * percent / year


@model.transform.switch(demand_growth_model=DemandGrowthModel.LINEAR)
def passengers_per_year(
    modeling_year: int, demand_growth_rate: typing.Annotated[Quantity, percent / year]
) -> typing.Annotated[Quantity, passenger / year]:
    """The number of passengers per year globally assuming linear growth rate."""
    growth_factor = (100.0 * percent + demand_growth_rate * 1.0 * year).convert_to(DIMENSIONLESS)
    return PASSENGER_PER_YEAR_2025 + PASSENGER_PER_YEAR_2025 * (
        float(modeling_year - 2025) * growth_factor
    )


@model.transform.switch(demand_growth_model=DemandGrowthModel.EXPONENTIAL)  # type: ignore[no-redef]
def passengers_per_year(  # noqa: F811
    modeling_year: int, demand_growth_rate: typing.Annotated[Quantity, percent / year]
) -> typing.Annotated[Quantity, passenger / year]:
    """The number of passengers per year globally estimated assuming exponential growth rate."""
    growth_factor = (100.0 * percent + demand_growth_rate * 1.0 * year).convert_to(DIMENSIONLESS)
    return (PASSENGER_PER_YEAR_2025 * growth_factor ** (modeling_year - 2025)).cast_to(
        passenger / year
    )


@model.transform.switch(demand_growth_model=DemandGrowthModel.CONSTANT)  # type: ignore[no-redef]
def passengers_per_year() -> typing.Annotated[Quantity, passenger / year]:  # noqa: F811
    """The number of passengers per year globally estimated assuming constant growth rate."""
    return PASSENGER_PER_YEAR_2025.cast_to(passenger / year)
