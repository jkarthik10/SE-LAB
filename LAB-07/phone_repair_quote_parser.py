"""Robust input parsers for the phone repair quote application."""


def mask_imei(imei):
    """Mask an IMEI-like value, retaining only its final four characters.

    Non-string and empty values return an empty string. Hyphens and spaces are
    removed before masking. Short values are fully masked rather than leaking
    the complete identifier.
    """
    if not isinstance(imei, str):
        return ""
    normalized = imei.replace("-", "").replace(" ", "").strip()
    if not normalized:
        return ""
    if len(normalized) <= 4:
        return "*" * len(normalized)
    return "*" * (len(normalized) - 4) + normalized[-4:]


def parse_parts_order(text):
    """Parse semicolon-separated ``part x quantity`` entries safely.

    Invalid entries, blank part names, non-positive quantities and malformed
    quantities are ignored. Duplicate part names are accumulated.
    """
    if not isinstance(text, str) or not text.strip():
        return {}

    order = {}
    for item in text.split(";"):
        item = item.strip()
        if not item or "x" not in item.lower():
            continue
        part, qty_text = item.rsplit("x", 1) if "x" in item else item.rsplit("X", 1)
        part = part.strip()
        qty_text = qty_text.strip()
        if not part or not qty_text:
            continue
        try:
            qty = int(qty_text)
        except (TypeError, ValueError):
            continue
        if qty <= 0:
            continue
        order[part] = order.get(part, 0) + qty
    return order


def parse_model(text):
    """Return a normalized (brand, model) tuple, or empty fields if invalid."""
    if not isinstance(text, str):
        return "", ""
    parts = text.strip().split(None, 1)
    if len(parts) < 2 or not parts[0] or not parts[1].strip():
        return "", ""
    return parts[0].title(), parts[1].strip()


def main():
    print("==== Running mask_imei ====")
    value = input("Enter an IMEI number (e.g. 35-209900-176148-1): ")
    print("Masked IMEI:", mask_imei(value))

    print("\n==== Running parse_parts_order ====")
    value = input("Enter parts and quantities as PART xQTY separated by ; (e.g. screen x1; battery x2): ")
    print("Parts order:", parse_parts_order(value))

    print("\n==== Running parse_model ====")
    value = input("Enter the phone brand and model (e.g. Samsung Galaxy S23): ")
    print("Brand and model:", parse_model(value))


if __name__ == "__main__":
    main()
