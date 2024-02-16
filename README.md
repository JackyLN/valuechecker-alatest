# valuechecker-alatest

# Telephone Call Routing System

## Overview

This project implements a telephone call routing system designed to find the cheapest cost for a call based on operator price lists. Each operator provides prices for various phone number prefixes. Given a phone number, the system determines which operator offers the cheapest rate for that call.

## Why Trie?

[A trie (prefix tree)](https://www.geeksforgeeks.org/trie-insert-and-search/) is chosen as the core data structure for this project due to its efficient prefix matching capabilities. Tries allow for quick lookups of variable-length keys (in this case, phone number prefixes), making them ideal for matching phone numbers to their corresponding rates among potentially thousands of prefixes.

### Advantages of Using Trie:

- **Efficient Prefix Matching**: Directly supports finding the longest matching prefix for a given phone number.
- **Fast Lookups**: Time complexity for searches is O(n), where n is the length of the phone number, independent of the number of prefixes stored.
- **Space-Efficient**: Common prefixes are shared among entries, reducing space usage compared to storing prefixes in a hash map or list.

## Implementation

The system is implemented in Python, structured into a main application script (`app.py`) and a module (`my_package/routing.py`) containing the trie data structure and routing logic.

### Key Components:

- **TrieNode**: Represents a single node in the trie, containing children nodes and flags to indicate if a node corresponds to the end of a prefix.
- **OperatorTrie**: Encapsulates a trie for a specific operator, including methods to insert prefixes with their prices and to find the cheapest price for a given number.
- **find_cheapest_operator**: A function to compare prices across multiple operators and determine the cheapest one for a specific phone number.

## Setup Operators with Realistic Prefixes

The `setup_operators_mass_generate` function generates operators with a predefined set of real-world country prefixes. It can optionally save this data to a JSON file for later use. If a JSON file with operator data already exists, the system loads this data instead of regenerating it.

For future implementation, we can use `setup_operators` function to set up the input for operator list.

### JSON File Usage

The system can optionally save generated operator data to a JSON file (`operators.json`) and load from it in subsequent runs. This feature speeds up the system's startup time by reusing previously generated data and allows for easy inspection and modification of operator data.

> **Side note**: currently, `setup_operators_mass_generate` function only generates a small set of operators. If you generate a large list, it will take time during list loading / list generation. Hence, there may be a delay after running the main app.

### Generating and Saving Operator Data

Run `app.py` with the `--save` option to generate new operator data and save it to `operators.json`:

```bash
python app.py --save
```

If `operators.json` already exists, it will be overwritten with new data.

### Loading Operator Data from JSON

If `operators.json` exists, simply run `app.py` without the `--save` option. The system will load operator data from the JSON file:

```bash
python app.py
```

## Running the Application

1. **Without Saving to JSON**: Run the application normally to input a phone number and find the cheapest operator.

   ```bash
   python app.py
   ```

   Follow the prompt to enter a phone number.

2. **With JSON Data Saving**: To save the generated operator data to a JSON file (or load from it if available), use the `--save` flag.

   ```bash
   python app.py --save
   ```

## How to Use

After starting the application, you will be prompted to enter a phone number. The system will then display the cheapest operator for that number based on the available data.

## Testing

### Overview

The project includes a suite of unit tests designed to verify the functionality of the telephone call routing system. These tests cover various scenarios, including matching phone numbers to operators, handling edge cases, and ensuring the system behaves as expected under different conditions.

### Running the Tests

To run the unit tests, navigate to your project directory in the terminal and execute the following command:

```bash
python -m unittest tests/test_routing.py
```

This command runs all tests defined in `test_routing.py`, providing output on test successes and failures.

### Covered Scenarios

The current test suite includes scenarios such as:

- **Exact Match**: Testing that the system correctly identifies the cheapest operator when there is an exact match for the phone number prefix.
- **Partial Match**: Verifying that the system can find the cheapest rate when only a partial match for the phone number prefix exists.
- **No Match**: Ensuring the system properly handles cases where no operator has a matching prefix for the given phone number.
- **Longest Prefix Match**: Testing that the system prioritizes the longest matching prefix when multiple operators match the phone number to varying extents.

### Future Testing Considerations

To further enhance the reliability and robustness of the telephone call routing system, future tests could include:

- **Performance Testing**: Evaluating the system's performance, particularly the speed of finding the cheapest operator, as the number of operators and prefixes increases.
- **Concurrency Testing**: Ensuring the system behaves correctly under concurrent access, simulating real-world usage scenarios where multiple users might query the system simultaneously.
- **Integration Testing**: Testing the integration with external systems or databases, particularly if the system is expanded to include dynamic data sources for operator pricing.
- **Error Handling**: Verifying the system's response to invalid input, such as non-numeric phone numbers or improperly formatted JSON files, to ensure robust error handling and user feedback.

## Conclusion

This project demonstrates an efficient approach to solve the telephone call routing problem using a trie data structure. The implementation offers fast and reliable prefix matching, making it well-suited for applications requiring quick lookups of hierarchical or prefixed data.

## Sample running
Below is my output sample for a data set of 10000 operators, each opeartor consists of 999 prefixes 

```bash
$ python3 app.py --save
Enter a phone number to find the cheapest operator: 946961191
The cheapest operator for 946961191 is Operator 20 with a price of $0.1/min.
Search took 0.059937 seconds.

$ python3 app.py --save
Enter a phone number to find the cheapest operator: 68123456789
The cheapest operator for 68123456789 is Operator 1611 with a price of $0.1/min.
Search took 0.077846 seconds.

$ python3 app.py --save
Enter a phone number to find the cheapest operator: 4673212345
The cheapest operator for 4673212345 is Operator 75 with a price of $0.1/min.
Search took 0.075005 seconds.
```
