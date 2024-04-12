from m0_discount_table import find_dsfc, generate_fixed_cashflows
from m3_time_value_interactive import further_to_current

def discounted_payback_period(initial_investment, cashflows, discount_rate):
    discounted_cumulative_cashflow = 0
    discounted_payback_period = None
    print("\n# Discounted Payback Period:")
    for period, cashflow in enumerate(cashflows):
        discounted_cashflow = cashflow * find_dsfc(1, discount_rate, period)
        discounted_cumulative_cashflow += discounted_cashflow
        print("    " ,period, cashflow, discounted_cashflow, initial_investment-discounted_cumulative_cashflow)
        if discounted_cumulative_cashflow >= initial_investment:
            if discounted_cumulative_cashflow - initial_investment != 0:
                fraction_of_last_period = (initial_investment - (discounted_cumulative_cashflow - discounted_cashflow)) / discounted_cashflow
                discounted_payback_period = period-1 + fraction_of_last_period
            else:
                discounted_payback_period = period
            break
    return discounted_payback_period

def payback_period(initial_investment, cashflows):
    cumulative_cashflow = 0
    payback_period = None
    print("\n# Payback Period:")
    for period, cashflow in enumerate(cashflows):
        cumulative_cashflow += cashflow
        print("    " ,period, cashflow, cashflow, initial_investment-cumulative_cashflow)
        if cumulative_cashflow >= initial_investment:
            if cumulative_cashflow - initial_investment != 0:
                fraction_of_last_period = (initial_investment - (cumulative_cashflow - cashflow)) / cashflow
                payback_period = period-1 + fraction_of_last_period
            else:
                payback_period = period
            break
    print("\n","Payback Period")
    print("=",initial_investment,"/",annual_cashflow)
    print("=",initial_investment/annual_cashflow, "years")

    return

def npv_working(annual_cashflow, discount_rate, residual_value, num_period, initial_investment):
    print("NPV (Net Present Value)")
    print("=",annual_cashflow,"*", find_dsfc(2, discount_rate, num_period),"+",residual_value,"*",find_dsfc(1, discount_rate, num_period),"-",initial_investment)
    print("=",round(annual_cashflow * find_dsfc(2, discount_rate, num_period) + residual_value * find_dsfc(1, discount_rate, num_period) - initial_investment,2),"\n")

def npvi_working(annual_cashflow, discount_rate, residual_value, num_period,initial_investment):
    print("NPV Index")
    print("=",annual_cashflow,"*", find_dsfc(2, discount_rate, num_period),"+",residual_value,"*",find_dsfc(1, discount_rate, num_period),"/",initial_investment)
    print("=",round((annual_cashflow * find_dsfc(2, discount_rate, num_period) + residual_value * find_dsfc(1, discount_rate, num_period))/initial_investment,5),"\n")


# Example usage:
initial_investment = 372000
annual_cashflow = 80000
num_periods = 10
residual_value = 75000
# Notice: discount_rate is in % format, therefore 8%'s discount_rate is sinmply 8, not 0.08!
interest_rate = 10

irregular_cashflow = []

cashflows = generate_fixed_cashflows(annual_cashflow, num_periods, residual_value)

if irregular_cashflow != []:
    cashflows = irregular_cashflow
    cashflows.insert(0, 0)
    cashflows[-1] += residual_value 
print("# Cash Flows:", cashflows,"\n")
if irregular_cashflow == []:
    npv_working(annual_cashflow, interest_rate, residual_value, num_periods, initial_investment)
    npvi_working(annual_cashflow, interest_rate, residual_value, num_periods, initial_investment)
else:
    print("# Net Present Value: ", further_to_current(cashflows, interest_rate)-initial_investment)
    print("# Net Present Value Index: ", further_to_current(cashflows, interest_rate)/initial_investment)

payback_period(initial_investment, cashflows)
print(discounted_payback_period(initial_investment, cashflows, interest_rate), "year(s)")