"""Compatibility entry point; the canonical implementation is the parser module."""
from phone_repair_quote_parser import main, mask_imei, parse_model, parse_parts_order

__all__ = ["mask_imei", "parse_parts_order", "parse_model", "main"]

if __name__ == "__main__":
    main()
