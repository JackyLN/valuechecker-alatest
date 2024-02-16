class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.price = float('inf')


class OperatorTrie:
    def __init__(self, name):
        self.name = name
        self.root = TrieNode()

    def insert(self, prefix, price):
        node = self.root
        for char in prefix:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
        node.price = price

    def find_cheapest_price(self, number):
        node = self.root
        cheapest_price = None
        for char in number:
            if char in node.children:
                node = node.children[char]
                if node.isEndOfWord:
                    cheapest_price = node.price
            else:
                break
        return cheapest_price


def find_cheapest_operator(number, operators):
    cheapest_price = float('inf')
    cheapest_operator = None

    for operator in operators:
        price = operator.find_cheapest_price(number)
        if price is not None and price < cheapest_price:
            cheapest_price = price
            cheapest_operator = operator.name

    # Check if a cheapest price was found; if not, return None for both values
    if cheapest_price == float('inf'):
        return None, None
    else:
        return cheapest_operator, cheapest_price
