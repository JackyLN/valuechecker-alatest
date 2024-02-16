import time
import argparse
from my_package import OperatorTrie, find_cheapest_operator, setup_operators_mass_generate


def main():
    parser = argparse.ArgumentParser(
        description="Run the Telephone Call Routing System.")
    parser.add_argument('--save', action='store_true',
                        help='Optionally save generated operators to a JSON file.')
    args = parser.parse_args()

    # The JSON filename to save to or load from, if --save is specified
    json_filename = "operators.json" if args.save else None

    # Setup operators, either by loading from a JSON file or generating new data
    # If --save is used, and data is generated, it will also save to the specified JSON file
    operators = setup_operators_mass_generate(
        filename=json_filename, num_operators=1000, num_prefixes=999)

    # Input phone number
    number = input("Enter a phone number to find the cheapest operator: ")

    start_time = time.time()  # Start timing
    cheapest_operator, cheapest_price = find_cheapest_operator(
        number, operators)
    end_time = time.time()  # End timing

    if cheapest_operator:
        print(
            f"The cheapest operator for {number} is {cheapest_operator} with a price of ${cheapest_price}/min."
        )
    else:
        print("No operator found for the given number.")

    print(f"Search took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    main()
