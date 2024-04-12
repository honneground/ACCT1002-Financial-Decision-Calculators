variable_cost = 75+100+35
fixed_cost = 2600000



if __name__ == '__main__':
# optional parameters based on the question
    selling_price = 650
    excepted_profit = 0
    num_units = 6500

    if selling_price != 0:
        contribution_margin = selling_price - variable_cost
        breakeven_units = round(fixed_cost/contribution_margin)
        breakeven_dollars = breakeven_units * selling_price
        print("## Breakeven: \n  ", breakeven_units, "unit(s)\n   $", breakeven_dollars)
        if num_units != 0:
            profit = (selling_price - variable_cost) * num_units - fixed_cost
            print("# Total Profit: $", profit)
        else:
            excepted_units = (excepted_profit + fixed_cost)/contribution_margin
            print("# Expected Sales:", round(excepted_units), "unit(s)", "\n  (where a profit of $", excepted_profit ,"can be achieved)")
    else:
        excepted_selling_price = round(variable_cost + (fixed_cost + excepted_profit) / num_units)
        breakeven_selling_price = round(variable_cost + fixed_cost / num_units)
        print("\n## Breakeven Selling Price: $", breakeven_selling_price, "\n   Expected Selling Price:  $", excepted_selling_price, "\n   (where a profit of $", excepted_profit ,"can be achieved)")