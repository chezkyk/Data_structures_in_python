accounts = {
    "123-456-789": 5000.50,
    "987-654-321": 3200.75,
    "111-222-333": 7600.10,
    "444-555-666": 1500.00
}

def calculate_total_balance(accounts_dict):
    total_balance = 0
    accounts_list =  list(accounts_dict.values())
    return sum(accounts_list)

print(calculate_total_balance(accounts))

print("---" * 100)

expenses = {
    "Groceries": [150.75, 200.30, 125.50],
    "Utilities": [300.00, 250.40],
    "Entertainment": [100.00, 50.50, 75.75],
    "Transportation": [60.00, 45.30]
}
def categorize_expenses(expenses_dict):
    for service, cost in expenses_dict.items():
        expenses_dict[service] = sum(cost)
    return expenses_dict
print(categorize_expenses(expenses))

print("---" * 100)

#def track_loan_repayments(loans_dict):
