from m0_discount_table import find_dsfc, generate_fixed_cashflows

def further_to_current(cashflows, discount_rate):
    discounted_cumulative_cashflow = 0
    for period, cashflow in enumerate(cashflows):
        discounted_cashflow = cashflow * find_dsfc(1, discount_rate, period)
        discounted_cumulative_cashflow += discounted_cashflow
    return discounted_cumulative_cashflow 

def further_to_current_fixed_payment(annual_cashflow, discount_rate, residual_value, num_period):
    return annual_cashflow * find_dsfc(2, discount_rate, num_period) + residual_value * find_dsfc(1, discount_rate, num_period) 

if __name__ == '__main__':
    try:
        non_irregular = input("Is this a regular annuity Question? (Y/n): ").lower()

        annually_interest_rate = float(input("Annually interest rate (%): "))
        
        payment_per_year_input = input("Payment per year (Defualt as 1): ")
        payment_per_year = int(payment_per_year_input) if payment_per_year_input else 1

        if non_irregular.upper() != "N":
            annual_cashflow_input = input("Annual cash flow: ")
            annual_cashflow = float(annual_cashflow_input) if annual_cashflow_input else 0
            
            num_years = int(input("Number of years: "))
            
            residual_value_input = input("Residual value (Defualt as 0): ")
            residual_value = float(residual_value_input) if residual_value_input else 0

            cashflows = generate_fixed_cashflows(annual_cashflow/payment_per_year, payment_per_year*num_years, residual_value)
            print("Cashflows: ", cashflows, "\n")
            print("Table one suggests:", further_to_current(cashflows, annually_interest_rate/payment_per_year))
            print("Table two suggests:", further_to_current_fixed_payment(annual_cashflow/payment_per_year, annually_interest_rate/payment_per_year, residual_value, num_years * payment_per_year))
            print("\nNote: WileyPlus expects what table two suggests.")

        else:
            cashflows = [0.0]
            num_cashflows = int(input("Number of cash flows: "))
            for i in range(num_cashflows):
                cashflow_input = input(f"Cash flow for year {i+1}: ")
                cashflow = float(cashflow_input) if cashflow_input else 0
                cashflows.append(cashflow)
            residual_value_input = input("Residual value (Defualt as 0): ")
            cashflows[-1] += float(residual_value_input) if residual_value_input else 0
            print("Cashflows: ", cashflows, "\n")
            print(further_to_current(cashflows, annually_interest_rate/payment_per_year))

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")



