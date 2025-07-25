import typing

import pytest
import pytest_camia
from camia_model.units import Quantity, percent, year

from aviation.demand import (
    DemandGrowthModel,
    demand_growth_rate,
    passengers_per_year,
)
from aviation.units import passenger


def test_demand_growth_rate() -> None:
    assert demand_growth_rate() == 4.0 * percent / year


@pytest.mark.parametrize(
    ("demand_growth_model", "modeling_year", "demand_growth_rate", "expected_passengers_per_year"),
    (
        (DemandGrowthModel.EXPONENTIAL, 2025, 4.0 * percent / year, 5_000_000.0 * passenger / year),
        (
            DemandGrowthModel.EXPONENTIAL,
            2025,
            10.0 * percent / year,
            5_000_000.0 * passenger / year,
        ),
        (DemandGrowthModel.LINEAR, 2025, 10.0 * percent / year, 5_000_000.0 * passenger / year),
        # (DemandGrowthModel.EXPONENTIAL, 2026, 4.0 * percent / year, 5_000_000.0 * passenger / year),
    ),
)
def test_passengers_per_year(
    demand_growth_model: DemandGrowthModel,
    modeling_year: int,
    demand_growth_rate: typing.Annotated[Quantity, percent / year],
    expected_passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> None:
    with passengers_per_year.context(demand_growth_model=demand_growth_model):
        assert passengers_per_year(modeling_year, demand_growth_rate) == pytest_camia.approx(
            expected_passengers_per_year, atol=1.0
        )
