# Financial Decision Calculators

* **Unit**: Financial Decision Making (`ACCT1002`)
* **Study Period**: 2024 Trimester 1A
* **Degree Programme**: Bachelor of Information Technology — Awarded with Distinction by Curtin University
* **Overall Unit Mark**: 93 (High Distinction)

Python calculators and spreadsheet tools I developed to support financial decision-making coursework and exam preparation. They cover time value of money, loan schedules, capital budgeting, cost–volume–profit analysis, short-term decisions, cash budgets and financial statement analysis.

## Coursework context

The unit involved applying financial calculations to business scenarios, showing calculation steps and interpreting results. Relevant tasks included discounting single sums and cash flows, comparing investments using NPV and payback, evaluating contribution margins and target profit, deciding whether to accept a special order or make a component, preparing cash budgets, and analysing financial statements and ratios across reporting periods.

The Python scripts were personal study and calculation helpers, with editable examples and interactive entry points. I subsequently used Google Sheets for the M6 decision tools and M7 cash budget, including input cells, results and generated workings. The Assignment 3 spreadsheet supports financial statement checking, ratio calculations and comparisons.

## Contents

| Location | Content |
|---|---|
| [`python/`](python/) | Nine Python scripts and their two discount-factor CSV inputs |
| [`sheets/M6_Decision_Calculators.xlsx`](sheets/M6_Decision_Calculators.xlsx) | Multiple-product breakeven, special-order analysis with workings, and make-or-buy analysis |
| [`sheets/M7_Cash_Budget.xlsx`](sheets/M7_Cash_Budget.xlsx) | Cash receipts/payments, surplus or deficit, and monthly opening/closing balances |
| [`sheets/Assignment3_Financial_Analysis.xlsx`](sheets/Assignment3_Financial_Analysis.xlsx) | Statement checks, financial ratios and comparisons |
| [`sheets/README.md`](sheets/README.md) | Spreadsheet inputs, calculations and worksheet guide |

## Python usage

Python 3 and its standard library are sufficient. Run from `python/` because the scripts load `table1.csv` and `table2.csv` using relative paths.

```bash
cd python
python m3_time_value_interactive.py
```

Other entry points include:

```bash
python m0_discount_table.py
python m3_time_value_interactive_lite.py
python m3_loan.py
python m4_payback.py
python m5_breakeven_interactive.py
```

| File | Purpose |
|---|---|
| `m0_discount_table.py` | Read single-sum and annuity discount factors and generate fixed cash-flow sequences |
| `m3_time_value.py` | Time-value and cash-flow helper calculations |
| `m3_time_value_interactive.py` | Interactive present-value and cash-flow calculations |
| `m3_time_value_interactive_lite.py` | Smaller interactive time-value workflow |
| `m3_loan.py` | Loan payment and amortization schedule example |
| `m3_future_value_inverse.py` | Discount a future amount to its present value |
| `m4_payback.py` | NPV, NPV index, conventional/discounted payback and printed workings |
| `m5_breakeven.py` | Editable cost–volume–profit and target-profit example |
| `m5_breakeven_interactive.py` | Interactive contribution-margin, breakeven and target-profit calculations |

The scripts use table-based factors and the rounding conventions in the original examples. Interest rates are entered in percentage points where prompted: enter `5` for 5 percent. Noninteractive examples are configured by editing their input assignments.

## Spreadsheets

For the original calculators, **use the Google Sheets versions below and choose File → Make a copy** to create an editable copy in your own Google Drive.

| Tool | Google Sheets | converted Excel |
|---|---|---|
| M6 decision calculators | [Open Google Sheets](https://docs.google.com/spreadsheets/d/1Y9nMH6bmG5BGWtqtUkQjnl05tsrkPAWM6aiaLclLBfk/edit) | [converted Excel](sheets/M6_Decision_Calculators.xlsx) |
| M7 cash budget | [Open Google Sheets](https://docs.google.com/spreadsheets/d/1zGr3icQHU2QsFO2qCnQKNDQuDqOtGPM7WUv6UMqjchY/edit) | [converted Excel](sheets/M7_Cash_Budget.xlsx) |
| Assignment 3 financial analysis | [Open Google Sheets](https://docs.google.com/spreadsheets/d/15p4dUpBgeMJQyjXLMAqCA98oivgotNzWGC321dRknco/edit) | [converted Excel](sheets/Assignment3_Financial_Analysis.xlsx) |

The Excel editions were **converted from my Google Sheets by Codex**. They run locally without a Google account, macros or external data refresh. The M6 multiple-product sheet supports 299 product positions using ordinary Excel formulas. See the [spreadsheet guide](sheets/README.md) for inputs and results.

Enter your own scenario amounts in the blank input cells. Cost multipliers and cash-collection rates have editable defaults; calculated cells update from your inputs.
