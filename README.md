# Simple Calculator

Course: COU3303 – Software Engineering
Assignment: Simple Calculator Development & Testing

A simple GUI calculator built in Python using Tkinter. Supports addition,
subtraction, multiplication, division, decimals, clear, and backspace.

## Features
- Basic arithmetic: `+  -  *  /  %`
- Decimal number support
- Clear (`C`) and backspace (`⌫`)
- Graceful handling of division by zero (fixed in v1.1)

## How to run
```bash
python calculator.py
```
Requires Python 3 with Tkinter (included by default on most systems; on
Linux you may need `sudo apt install python3-tk`).

## How to run the tests
```bash
python -m unittest test_calculator.py -v
```

## Version History
- **v1.0** – Initial version. Bug found during testing: dividing by zero
  crashed the app with an unhandled `ZeroDivisionError` (see TC05 in
  `test_case_scenarios.xlsx`).
- **v1.1** – Fixed division-by-zero bug: `divide()` now raises a handled
  `ZeroDivisionError` that the UI catches and displays as `Error: Div by 0`.
  All test cases pass.

## Test Case Scenarios
See `test_case_scenarios.xlsx` (also submitted separately to the activity
box) for the full list of test cases, steps, expected vs. actual results,
and pass/fail status for both v1.0 and v1.1.

## Author
<your name> – <your student ID>
