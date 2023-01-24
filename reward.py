from collections import defaultdict, Counter
from datetime import datetime

transactions = [
    {'customer': 'John Doe', 'amount': 120, 'date': '2022-01-01'},
    {'customer': 'John Doe', 'amount': 50, 'date': '2022-01-05'},
    {'customer': 'Jane Smith', 'amount': 75, 'date': '2022-01-10'},
    {'customer': 'Jane Smith', 'amount': 200, 'date': '2022-02-15'},
    {'customer': 'John Doe', 'amount': 150, 'date': '2022-02-20'},
    {'customer': 'Jane Smith', 'amount': 90, 'date': '2022-03-05'},
    # ... more transactions
]

# Function to calculate rewards points for a transaction
def calculate_points(amount):
    points = 0
    if amount > 50:
        points += (amount - 50)
    if amount > 100:
        points += (amount - 100)
    return points

# Initialize dictionaries to store customer rewards points by month and total
customer_points_by_month = defaultdict(lambda: defaultdict(int))
customer_points_total = defaultdict(int)

# Iterate through transactions and add rewards points to dictionaries
for transaction in transactions:
    customer = transaction['customer']
    amount = transaction['amount']
    date = datetime.strptime(transaction['date'], '%Y-%m-%d')
    points = calculate_points(amount)
    month = date.strftime('%B %Y')
    customer_points_by_month[customer][month] += points
    customer_points_total[customer] += points

# Print rewards points for each customer by month and total
for customer in customer_points_by_month:
    print(f'{customer} rewards points by month:')
    for month, points in customer_points_by_month[customer].items():
        print(f'    {month}: {points}')
    print(f'    Total: {customer_points_total[customer]}')