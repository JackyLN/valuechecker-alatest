import random
import json
import os
from .routing import OperatorTrie


def generate_operator_prices(num_prefixes):
    """Generate a dictionary of random prefixes and prices."""
    prices = {}
    for _ in range(num_prefixes):
        # Generate a random prefix (as a string of numbers) and a random price
        prefix = str(random.randint(200, 999))
        price = round(random.uniform(0.1, 5.0), 2)
        prices[prefix] = price
    return prices


def setup_operators_mass_generate(filename="operators.json", num_operators=10, num_prefixes=100):
    if os.path.exists(filename):
        # Load existing operator data from JSON file
        with open(filename, 'r') as f:
            operators_data = json.load(f)
    else:
        # Generate new operator data
        operators_data = {
            f"Operator {i+1}": generate_operator_prices(num_prefixes)
            for i in range(num_operators)
        }
        # Save the newly generated data to JSON
        save_operators_to_json(operators_data, filename)

    # Initialize OperatorTrie instances from the operators data
    operators = []
    for name, prices in operators_data.items():
        operator = OperatorTrie(name)
        for prefix, price in prices.items():
            operator.insert(prefix, price)
        operators.append(operator)

    return operators


def save_operators_to_json(operators_data, filename="operators.json"):
    # Save the operator data directly to a JSON file
    with open(filename, 'w') as f:
        json.dump(operators_data, f, indent=4)


def setup_operators():

    operators_info = [
        {
            "name": "Operator A",
            "prices": {
                '1': 0.9,
                '268': 5.1,
                '46': 0.17,
                '4620': 0.01,
                '468': 0.15,
            }
        },
        {
            "name": "Operator B",
            "prices": {
                '1': 0.92,
                '44': 0.5,
                '46': 0.2,
                '467': 1.0,
                '48': 1.2,
            }
        },
        {
            "name": "Operator C",
            "prices": {
                '1': 0.88,
                '44': 0.45,
                '46': 0.18,
                '467': 0.95,
                '48': 1.15,
            }
        },
        {
            "name": "Operator D",
            "prices": {
                '1': 0.85,
                '44': 0.48,
                '46': 0.19,
                '467': 1.05,
                '48': 1.10,
            }
        },
    ]

    operators = []

    for op_info in operators_info:
        operator = OperatorTrie(op_info["name"])
        for prefix, price in op_info["prices"].items():
            operator.insert(prefix, price)
        operators.append(operator)

    return operators
