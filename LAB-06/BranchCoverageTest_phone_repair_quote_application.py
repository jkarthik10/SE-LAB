"""Decision/branch coverage tests for phone_repair_quote.py.

Run: coverage run --branch --source=phone_repair_quote -m pytest BranchCoverageTest_phone_repair_quote_application.py
"""
import pytest

from phone_repair_quote import repair_quote, repair_days, trade_in_value


# repair_quote: valid and invalid part/tier; both pricing, labour,
# warranty and express decision outcomes.
@pytest.mark.parametrize(
    "part,tier,warranty,express,expected",
    [
        ("screen", "budget", False, False, 4600),
        ("screen", "flagship", False, True, 9100),
        ("battery", "budget", False, True, 2300),
        ("battery", "flagship", True, False, 300),
        ("camera", "budget", True, True, 800),
        ("charging_port", "flagship", False, False, 1900),
    ],
)
def test_repair_quote_all_decisions(part, tier, warranty, express, expected):
    assert repair_quote(part, tier, warranty, express) == expected


@pytest.mark.parametrize(
    "part,tier",
    [("unknown", "budget"), ("screen", "standard")],
)
def test_repair_quote_validation_branches(part, tier):
    with pytest.raises(ValueError):
        repair_quote(part, tier, False, False)


# repair_days: technician-free and available; stock and no-stock;
# screen/camera and other-part paths when out of stock.
@pytest.mark.parametrize(
    "part,in_stock,technicians,expected",
    [
        ("screen", True, 0, 3),
        ("camera", False, 0, 8),
        ("screen", False, 2, 6),
        ("camera", True, 1, 1),
        ("battery", False, 0, 5),
        ("charging_port", False, 4, 3),
        ("battery", True, 3, 1),
    ],
)
def test_repair_days_all_decisions(part, in_stock, technicians, expected):
    assert repair_days(part, in_stock, technicians) == expected


# trade_in_value: invalid-input OR outcomes, >48, <=12, <=24,
# remaining age band, and both cracked-screen outcomes.
@pytest.mark.parametrize(
    "price,age,cracked,expected",
    [
        (10000, 49, False, 0),
        (10000, 12, False, 6000),
        (10000, 24, False, 4000),
        (10000, 25, False, 2000),
        (10000, 12, True, 3000),
        (10000, 24, True, 2000),
        (10000, 25, True, 1000),
    ],
)
def test_trade_in_age_and_cracked_branches(price, age, cracked, expected):
    assert trade_in_value(price, age, cracked) == expected


@pytest.mark.parametrize("price,age", [(0, 0), (-100, 10), (1000, -1)])
def test_trade_in_invalid_input_branches(price, age):
    with pytest.raises(ValueError):
        trade_in_value(price, age, False)
