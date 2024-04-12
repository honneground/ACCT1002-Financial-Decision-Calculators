from m0_discount_table import find_dsfc, generate_fixed_cashflows

def further_to_current(cashflows, discount_rate):
    discounted_cumulative_cashflow = 0
    for period, cashflow in enumerate(cashflows):
        discounted_cashflow = cashflow * find_dsfc(1, discount_rate, period)
        discounted_cumulative_cashflow += discounted_cashflow
    return discounted_cumulative_cashflow 

def further_to_current_fixed_payment(annual_cashflow, discount_rate, residual_value, num_period):
    return annual_cashflow * find_dsfc(2, discount_rate, num_period) + residual_value * find_dsfc(1, discount_rate, num_period) 

# For non-irreggular Aunity Questions ONLY!!!!
annual_cashflow = 10000
num_years = 4
residual_value = 9500

# Notice: annually_interest_rate is in % format, therefore 8%'s annually_interest_rate is sinmply 8, not 0.08!
annually_interest_rate = 14


payment_per_year = 1 # Default as 1

# For irreggular Aunity Questions, uncomment and ajust the following
cashflows = []

if cashflows != []:
    cashflows.insert(0, 0)  # Add 0 to the front of the list
    print("Cashflows: ", cashflows, "\n")
    print(further_to_current(cashflows, annually_interest_rate/payment_per_year))
else:
   cashflows = generate_fixed_cashflows(annual_cashflow/payment_per_year, payment_per_year*num_years, residual_value)
   print("Cashflows: ", cashflows, "\n")
   print("Table one suggests:", further_to_current(cashflows, annually_interest_rate/payment_per_year))
   print("Table two suggests:", further_to_current_fixed_payment(annual_cashflow/payment_per_year, annually_interest_rate/payment_per_year, residual_value, num_years * payment_per_year))
   print("\nNote: WileyPlus expects what table two suggests.")
