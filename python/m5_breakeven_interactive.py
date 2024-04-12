def require_parameter(string, compulsory = False):
    string = string + ": "
    while True:
        try:
            value = input(string)
            if compulsory == False:
                value = 0 if value == "" else float(value)
            else:
                value = float(value)
            return value
        except:
            print("Please enter a valid value.")

variable_cost = require_parameter("Variable Cost", True)
fixed_cost = require_parameter("Fixed Cost", True)

# optional parameters based on the question
selling_price = require_parameter("Selling Price")
num_units = require_parameter("Number of Units")
excepted_profit = require_parameter("Excepted Profit")

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