from typing import Literal
import logging

import pandas as pd


logger = logging.getLogger(__name__)


def calculate_revenue(
        pdf: pd.DataFrame,
        scenario_factors: dict,
        scenario: Literal["low", "med", "high"]
) -> pd.DataFrame:
    """
    Calculate revenue by combining NG and CO2 prices and multiplying by the scenario
    factor.

    Parameters
    ----------
    pdf: DataFrame holding the NG and CO2 prices for each day
    scenario_factors: multiplication factor based on economic scenario
    scenario: economic scenario

    Returns
    -------
    DataFrame with calculated revenue.
    """
    factor = scenario_factors.get(scenario, "low")
    logger.info(f"Using the `{scenario}` scenario -> factor={factor}")
    pdf["revenue"] = pdf["price_ng"] * pdf["price_co2"] * factor

    return pdf
