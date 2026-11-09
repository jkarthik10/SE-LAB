"""Insurance premium calculator with safer input handling and file operations."""

import csv
import math
import os
import secrets
import tarfile
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

from defusedxml import ElementTree

QUOTES = {}
LOG_FILE = Path("premium_quotes.log")
BASE_RATES = {"health": 5000, "motor": 3000, "life": 8000}
UNDERWRITER_TOKEN = os.getenv("UNDERWRITER_TOKEN")


def calculate_premium(policy_type, age, sum_insured, smoker, claims, discounts=None):
    """Calculate a premium without modifying the caller's discount collection."""
    if policy_type not in BASE_RATES:
        raise ValueError("Unsupported policy type.")
    if age < 0 or sum_insured < 0 or claims < 0:
        raise ValueError("Age, sum insured, and claims must be non-negative.")

    premium = BASE_RATES[policy_type] + sum_insured * 0.002
    if age > 45:
        premium *= 1.5
    if smoker:
        premium *= 1.3
    premium += claims * 1000

    for discount in discounts or ():
        if discount < 0:
            raise ValueError("Discounts must be non-negative.")
        premium -= discount

    return max(0.0, premium)


def age_from_dob(dob):
    """Return completed years of age for a date in DD-MM-YYYY format."""
    birth_date = datetime.strptime(dob, "%d-%m-%Y").date()
    today = date.today()
    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


def policy_number():
    """Generate a hard-to-guess policy reference."""
    return f"POL-{secrets.randbelow(900000) + 100000}"


def save_quote(name, premium):
    """Store a quote in memory and append it safely to the CSV log."""
    if not name.strip():
        raise ValueError("Customer name cannot be empty.")
    number = policy_number()
    QUOTES[number] = {"name": name, "premium": premium}

    with LOG_FILE.open("a", newline="", encoding="utf-8") as quote_file:
        writer = csv.writer(quote_file)
        writer.writerow([number, name, f"{premium:.2f}"])

    return number


def import_policies(xml_text):
    """Parse partner policy XML safely and skip malformed policy records."""
    root = ElementTree.fromstring(xml_text)
    result = []
    for policy in root.findall("policy"):
        try:
            policy_type = policy.get("type")
            age = int(policy.get("age", ""))
            sum_insured = int(policy.get("sum", ""))
            if policy_type not in BASE_RATES or age < 0 or sum_insured < 0:
                continue
            result.append((policy_type, age, sum_insured))
        except (TypeError, ValueError):
            continue
    return result


def fetch_rates(url):
    """Download a rate table over HTTPS with normal certificate validation."""
    parsed_url = urlparse(url)
    if parsed_url.scheme != "https" or not parsed_url.netloc:
        raise ValueError("Rate table URL must be a valid HTTPS URL.")
    with urlopen(url, timeout=10) as response:
        return response.read()


def import_claim_documents(archive_path):
    """Extract regular files from an archive without path traversal."""
    destination = Path("claims_docs").resolve()
    destination.mkdir(parents=True, exist_ok=True)

    with tarfile.open(archive_path, "r:*") as archive:
        for member in archive.getmembers():
            target = (destination / member.name).resolve()
            if not target.is_relative_to(destination):
                raise ValueError("Archive contains an unsafe file path.")
            if member.issym() or member.islnk() or not (member.isfile() or member.isdir()):
                raise ValueError("Archive contains an unsupported entry.")
        archive.extractall(destination, filter="data")


def monthly_instalment(premium, months=12):
    """Calculate a whole-unit monthly instalment."""
    if months <= 0:
        raise ValueError("Number of months must be greater than zero.")
    if premium < 0:
        raise ValueError("Premium cannot be negative.")
    return math.floor(premium / months)


def is_authorised(token):
    """Check a token supplied through the runtime environment."""
    return bool(UNDERWRITER_TOKEN) and secrets.compare_digest(
        token, UNDERWRITER_TOKEN
    )


def renewal_due(start, years=1):
    """Return the renewal date, handling leap-day dates safely."""
    if years < 0:
        raise ValueError("Years cannot be negative.")
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    try:
        renewal_date = start_date.replace(year=start_date.year + years)
    except ValueError:
        renewal_date = start_date.replace(
            year=start_date.year + years, day=28
        )
    return renewal_date.strftime("%Y-%m-%d")


def print_quotes():
    """Print all quotes currently stored in memory."""
    print("===== Quote Book =====")
    for index, (number, quote) in enumerate(QUOTES.items(), start=1):
        print(
            index,
            number,
            quote["name"],
            "Rs.",
            f'{quote["premium"]:.2f}',
        )


def main():
    """Run sample calculations demonstrating the calculator features."""
    premium_one = calculate_premium("health", 30, 500000, False, 0)
    premium_two = calculate_premium("health", 30, 500000, False, 0)
    motor_premium = calculate_premium("motor", 50, 800000, False, 0)
    discounts = [3000, 3000, 3000]
    life_premium = calculate_premium(
        "life", 25, 100000, False, 0, discounts
    )

    print("Quote 1:", premium_one)
    print("Quote 2 (same customer details):", premium_two)
    print("Non-smoker aged 50:", motor_premium)
    print("Life with stacked discounts:", life_premium)
    print("Discount list remains unchanged:", discounts)
    print("Age from DOB 31-12-1990:", age_from_dob("31-12-1990"))
    print("Monthly instalment:", monthly_instalment(motor_premium))
    print("Renewal due:", renewal_due("2025-03-15"))
    sample_xml = (
        "<policies><policy type='health' age='40' sum='300000'/>"
        "<policy type='motor' age='abc' sum='1'/></policies>"
    )
    print("Imported:", import_policies(sample_xml))
    print("Saved as:", save_quote("Kiran", premium_one))
    print("Authorised:", is_authorised(os.getenv("UNDERWRITER_TOKEN", "")))
    print("Server would listen on a configured host.")
    print_quotes()


if __name__ == "__main__":
    main()
