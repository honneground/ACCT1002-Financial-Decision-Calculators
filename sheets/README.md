# Spreadsheet Calculators

Three Excel workbooks cover short-term business decisions, cash budgeting and financial statement analysis.

## Google Sheets and Excel editions

**Prefer the original Google Sheets calculators.** Open a link and select **File → Make a copy** to use an editable copy in your own Google Drive.

| Tool | Google Sheets |
|---|---|
| M6 decision calculators | [Open original calculator](https://docs.google.com/spreadsheets/d/1Y9nMH6bmG5BGWtqtUkQjnl05tsrkPAWM6aiaLclLBfk/edit) |
| M7 cash budget | [Open original calculator](https://docs.google.com/spreadsheets/d/1zGr3icQHU2QsFO2qCnQKNDQuDqOtGPM7WUv6UMqjchY/edit) |
| Assignment 3 financial analysis | [Open original calculator](https://docs.google.com/spreadsheets/d/15p4dUpBgeMJQyjXLMAqCA98oivgotNzWGC321dRknco/edit) |

The downloadable **Excel editions were converted from the author's Google Sheets by Codex**. They provide a local alternative without a Google account, macros or external data refresh.

## Starting a scenario

Enter your own amounts in the blank input cells and leave formula cells unchanged. Ratio and breakeven results remain blank when required inputs are missing; other totals may show zero. A numeric zero is a valid input.

The make-or-buy cost multipliers default to `1`. Cash-collection rates in `budgets v2!L35:L36` default to `60%` and `30%`; adjust these assumptions to your scenario.

## M6 Decision Calculators

Open [`M6_Decision_Calculators.xlsx`](M6_Decision_Calculators.xlsx).

| Worksheet | Inputs and results |
|---|---|
| `Special Order v2 (with working)` | Normal/special prices, costs, volume and capacity; calculates contribution margins, opportunity cost, incremental gain/loss and workings |
| `Muti-Products Breakeven` | Sales/quantity in row 2, selling price in row 3, variable cost in row 4, fixed cost in B5 and optional target in B6; calculates weighted contribution and breakeven/product allocations |
| `Make or Buy` | Volume, unit costs, labour and other fixed costs; calculates each alternative's total cost, difference and decision |

The multiple-product sheet supports **299 product positions, B through KN**. Blank product positions remain blank in calculated rows; entering zero remains a numeric input. Fixed cost and optional target are shared inputs in B5 and B6.

## M7 Cash Budget

Open [`M7_Cash_Budget.xlsx`](M7_Cash_Budget.xlsx). The `budgets v2` worksheet contains receipts, payments, surplus/deficit and a closing balance feeding the next opening balance. Enter amounts in the white input cells and preserve formula cells. Month headings can be adjusted to the scenario.

## Assignment 3 Financial Analysis

Open [`Assignment3_Financial_Analysis.xlsx`](Assignment3_Financial_Analysis.xlsx).

| Worksheet | Purpose |
|---|---|
| `2019` | Input statements, check internal totals and calculate financial ratios |
| `Formulas` | Formula illustrations included in the original tool |
| `2020` | Equivalent calculations for the second period |
| `Changes` | Compare amounts/ratios and generate supporting descriptions |

Some `Changes` headings use `2022` while the other worksheet is named `2020`. Set reporting labels and amounts to match the scenario.
