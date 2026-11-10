"""Statement/line coverage tests for phone_repair_quote.py.

Run: coverage run --source=phone_repair_quote -m pytest CodeCoverageTest_phone_repair_quote_application.py
"""
import pytest

from phone_repair_quote import repair_quote, repair_days, trade_in_value


@pytest.mark.parametrize(
    "part,tier,warranty,express,expected",
    [
        ("screen", "budget", False, False, 4600),
        ("battery", "budget", False, False, 1800),
        ("screen", "flagship", False, False, 8600),
        ("camera", "flagship", False, True, 5800),
        ("battery", "budget", True, False, 300),
        ("charging_port", "flagship", True, True, 800),
    ],
)
def test_repair_quote_valid_cases(part, tier, warranty, express, expected):
    assert repair_quote(part, tier, warranty, express) == expected


@pytest.mark.parametrize(
    "part,tier",
    [
        ("speaker", "budget"),
        ("screen", "premium"),
    ],
)
def test_repair_quote_rejects_unknown_values(part, tier):
    with pytest.raises(ValueError):
        repair_quote(part, tier, False, False)


@pytest.mark.parametrize(
    "part,in_stock,technicians,expected",
    [
        ("battery", True, 2, 1),
        ("screen", False, 1, 6),
        ("camera", False, 0, 8),
        ("charging_port", False, 3, 3),
        ("battery", False, 0, 5),
    ],
)
def test_repair_days_cases(part, in_stock, technicians, expected):
    assert repair_days(part, in_stock, technicians) == expected


@pytest.mark.parametrize(
    "price,age,cracked,expected",
    [
        (10000, 6, False, 6000),
        (10000, 18, False, 4000),
        (10000, 36, False, 2000),
        (10000, 60, False, 0),
        (10000, 6, True, 3000),
        (10000, 18, True, 2000),
        (10000, 36, True, 1000),
    ],
)
def test_trade_in_value_cases(price, age, cracked, expected):
    assert trade_in_value(price, age, cracked) == expected


@pytest.mark.parametrize("price,age", [(0, 5), (-1, 5), (1000, -1)])
def test_trade_in_value_rejects_invalid_input(price, age):
    with pytest.raises(ValueError):
        trade_in_value(price, age, False)
