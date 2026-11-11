# L6_L7_59 — Phone Repair Quote

## Lab 7: Fuzzing for Input Validation Bugs

This lab uses Hypothesis and pytest to fuzz three parsers and harden them against malformed input.

### Files

| File | Purpose |
|---|---|
| `phone_repair_quote_parser.py` | Fixed implementation of the three parser functions and interactive application |
| `test_phone_repair_quote_parser.py` | Hypothesis property-based tests (canonical lab test file) |
| `processor.py` | Compatibility entry point requested by the handout |
| `test_processor.py` | Copy of the Hypothesis tests using the requested generic handout filename |
| `requirements.txt` | Test dependencies |

### Setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Run the application

```powershell
python phone_repair_quote_parser.py
```

Or use the compatibility entry point:

```powershell
python processor.py
```

### Run fuzz tests

```powershell
python -m pytest -v test_phone_repair_quote_parser.py
```

The requested generic test filename is also supported:

```powershell
python -m pytest -v test_processor.py
```

### Example inputs

- IMEI: `35-209900-176148-1`
- Parts: `screen x1; battery x2`
- Model: `Samsung Galaxy S23`

### Fixes

- `mask_imei`: checks input type, handles empty values, removes separators, and masks short values without exposing them.
- `parse_parts_order`: validates the input and each entry; ignores malformed entries and invalid/non-positive quantities; combines duplicate part names.
- `parse_model`: validates type and word count and safely handles whitespace-only or one-word input.

Invalid inputs return safe empty values (`""`, `{}`, or `("", "")`) rather than raising exceptions.

### Screenshot/report note

The submitted PDF contains captured command-output evidence and clearly labels any environment limitation. Run the commands above on your Windows machine to capture the final Hypothesis/pytest output if Hypothesis cannot be installed in the report-generation environment.

### Reproduce the failing Hypothesis screenshot (SS2)

After installing the requirements, temporarily switch to the supplied original buggy implementation:

```powershell
Copy-Item phone_repair_quote_parser.py phone_repair_quote_parser_fixed_backup.py
Copy-Item phone_repair_quote_parser_buggy.py phone_repair_quote_parser.py -Force
python -m pytest -v test_phone_repair_quote_parser.py
```

The tests are expected to fail against the original implementation. Capture the terminal output. Restore the fixed implementation immediately afterward:

```powershell
Copy-Item phone_repair_quote_parser_fixed.py phone_repair_quote_parser.py -Force
python -m pytest -v test_phone_repair_quote_parser.py
```

Capture the passing output for SS4. Do not commit the temporary backup file `phone_repair_quote_parser_fixed_backup.py`.
