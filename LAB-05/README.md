# INSURANCE PREMIUM CALCULATOR
## Lab 5 - Static Code Analysis

**Student Name:** J KARTHIK  
**SRN:** PES1UG25AM804

### 1. Project Overview
The Insurance Premium Calculator is a Python-based application that calculates insurance premiums based on policy type, age, sum insured, smoking status, and previous claims.

### 2. Objectives
- Improve Python code quality.
- Identify and fix programming errors.
- Detect security vulnerabilities.
- Follow Python coding standards.
- Perform static code analysis using Pylint, Bandit, and Flake8.

### 3. Technologies Used
- Python
- Pylint
- Bandit
- Flake8
- Git and GitHub

### 4. Static Analysis Tools

**Pylint:** Checks code quality, programming mistakes, naming conventions, and unused variables.

**Bandit:** Identifies common security vulnerabilities in Python applications.

**Flake8:** Checks Python coding style, indentation, whitespace, and PEP 8 compliance.

### 5. Issues Identified and Fixed
1. Mutable default argument.
2. Incorrect age calculation.
3. Disabled SSL certificate verification.
4. Unsafe XML parsing.
5. Unsafe archive extraction.
6. Hardcoded authentication token.
7. Broad exception handling.
8. Improper file handling.
9. Weak random policy number generation.
10. Missing input validation.

### 6. Improvements
- Replaced mutable default arguments with None.
- Improved age calculation.
- Enabled HTTPS certificate verification.
- Used secure XML parsing.
- Added archive path validation.
- Moved authentication tokens to environment variables.
- Improved exception handling.
- Added input validation.
- Improved file handling and code readability.

### 7. How to Run the Project

Install the required packages:

```bash
pip install defusedxml pylint bandit flake8
```

Run the Python program:

```bash
python premium_calculator.py
```

### 8. Static Code Analysis Commands

Run Pylint:

```bash
pylint premium_calculator.py
```

Run Bandit:

```bash
bandit -r premium_calculator.py
```

Run Flake8:

```bash
flake8 premium_calculator.py
```

### 9. Conclusion
Static code analysis helped identify and correct security vulnerabilities, programming errors, and coding-style issues in the Insurance Premium Calculator. Using Pylint, Bandit, and Flake8 improves code quality, security, readability, and maintainability.

The corrected program should be tested and all static analysis reports should be verified before final submission.
