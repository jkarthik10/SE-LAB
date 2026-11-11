"""Property-based fuzz tests for all public input parsers."""
from hypothesis import given, strategies as st

from phone_repair_quote_parser import mask_imei, parse_model, parse_parts_order


@given(st.one_of(st.text(), st.none()))
def test_mask_imei_no_crash(value):
    result = mask_imei(value)
    assert isinstance(result, str)
    assert len(result) <= len(value.replace("-", "").replace(" ", "")) if isinstance(value, str) else result == ""


@given(st.one_of(st.text(), st.none()))
def test_parse_parts_order_no_crash(value):
    result = parse_parts_order(value)
    assert isinstance(result, dict)
    assert all(isinstance(part, str) and isinstance(quantity, int) and quantity > 0
               for part, quantity in result.items())


@given(st.one_of(st.text(), st.none()))
def test_parse_model_no_crash(value):
    result = parse_model(value)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(part, str) for part in result)
