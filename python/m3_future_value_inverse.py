from m0_discount_table import find_dsfc, generate_fixed_cashflows

def deposite(future_value, interest_rate, num_periods):
    discount_rate = find_dsfc(1, interest_rate, num_periods)
    return future_value * discount_rate

# Notice: annually_interest_rate is in % format, therefore 8%'s annually_interest_rate is sinmply 8, not 0.08!
annually_interest_rate = 1
# For non-irreggular Aunity Questions ONLY!!!!
future_value = 10000
num_year = 3

payment_per_year = 12 # Default as 1


# Working 

print("Period Interest rate:", annually_interest_rate/payment_per_year, "%\nNumber of periods:", num_year*payment_per_year,"\n")
print("Present value:",deposite(future_value, annually_interest_rate/payment_per_year, num_year*payment_per_year))