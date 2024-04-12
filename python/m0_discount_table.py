def read_csv_file(file_path):
    """
    Reads a CSV file and returns its contents as a list of lists.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        list: A list of lists representing the CSV file contents.
    """
    with open(file_path, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
        data = [[float(element) for element in row] for row in data]
    return data

table_one = read_csv_file('table1.csv')
table_two = read_csv_file('table2.csv')
tables_dict = {1: table_one, 2: table_two}

def find_column_index(csv_data, target_value):
    # Iterate through the first row of the CSV data (assuming the first row contains column names)
    for index, value in enumerate(csv_data[0]):
        # Check if the target value is found
        if abs(value - target_value) <= 0.01:
            return index
    # Return -1 if the target value is not found
    return -1

def find_row_index(csv_data, target_value):
    # Iterate through the first row of the CSV data (assuming the first row contains column names)
    for index, row in enumerate(csv_data):
        # Check if the target value is found
        if row[0] == target_value:
            return index
    # Return -1 if the target value is not found
    return -1

def find_dsfc(table_index, interest_rate, period):
    """
    find the discount factor from the discount table
    interest_rate in percentage manner. eg. if interest_rate is 5%, interest_rate should be 5.
    """
    if period != 0:
        return tables_dict[table_index][find_row_index(tables_dict[table_index], period)][find_column_index(tables_dict[table_index], interest_rate)]
    else:
        return 1

def generate_fixed_cashflows(annual_cashflow, num_periods, residual_value=0):
    cashflows = [0]
    for _ in range(num_periods):
        cashflows.append(annual_cashflow)
    cashflows[-1] += residual_value
    return cashflows

if __name__ == '__main__':
    interest_input = float(input("Aannual Interest rate? (%): "))
    num_years_input = int(input("Numbers of years: "))
    remap_dict = {
        "": 1,
        "y": 1,
        "s": 2,
        "h": 2,
        "q": 4,
        "m": 12
    }
    num_payments = input("Number of payments annually: ")
    if num_payments.lower() in remap_dict:
        num_payments = remap_dict[num_payments.lower()]
    num_payments = int(num_payments)
    print()
    print(find_dsfc(1, interest_input/num_payments, num_years_input*num_payments), ("(Table 1)"))
    print(find_dsfc(2, interest_input/num_payments, num_years_input*num_payments), ("(Table 2)"))