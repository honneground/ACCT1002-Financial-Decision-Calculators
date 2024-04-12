from m0_discount_table import find_dsfc, generate_fixed_cashflows

def load(present_value, interest_rate, num_periods):
    discount_rate = find_dsfc(2, interest_rate, num_periods)
    future_value = present_value / discount_rate
    return future_value 

def deposite(present_value, interest_rate, num_periods):
    discount_rate = find_dsfc(1, interest_rate, num_periods)
    future_value = present_value / discount_rate
    return future_value 




# Notice: annually_interest_rate is in % format, therefore 8%'s annually_interest_rate is sinmply 8, not 0.08!
annually_interest_rate = 15
# For non-irreggular Aunity Questions ONLY!!!!
present_value = 5000
num_year = 5

payment_per_year = 1 # Default as 1




# Working 

print("Period Interest rate: ", annually_interest_rate/payment_per_year, "%\nNumber of periods: ", num_year*payment_per_year,"\n")

print("# Deposite Question:\nFuture value",deposite(present_value, annually_interest_rate/payment_per_year, num_year*payment_per_year))

period_payback = load(present_value, annually_interest_rate/payment_per_year, num_year*payment_per_year)
print("\n# Load Question:")
# print("Period repayment:", period_payback)
print("Period repayment:", round(period_payback))
# print("Total repayment:", period_payback * num_year*payment_per_year)
print("Total repayment:", round(period_payback)*num_year*payment_per_year)
print("Total interest:", (round(period_payback)*num_year*payment_per_year)-present_value)

print("\n$ Loan schedule $")
curr_period = 0
cit = 0
balance = present_value
while(True):
    curr_period += 1
    open_balance = balance
    curr_interest = round(balance*(annually_interest_rate/payment_per_year)*0.01)
    cit += curr_interest
    reduction = round(period_payback) - curr_interest
    balance = balance - reduction
    if curr_period <= (num_year*payment_per_year):
        print(curr_period, open_balance, curr_interest, round(period_payback), reduction, balance)
    else:
        break

print("Period|OpenBalance|Interst|Repayment|Reduction|ClosingBalance")

