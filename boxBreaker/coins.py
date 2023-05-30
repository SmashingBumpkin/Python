import argparse

def isPayable(a: int, b: int, c: int, w: int) -> bool:
    coins = (a, b, c)               # O(1)
   
    for coin in coins:              # 3 times (O(1))
        buffer: int = w             # O(1)
        while buffer < 0:           # Depends on the subtraction, which occurs
                                    # buffer // coin times, so O(n)
            if any([buffer % x == 0 for x in coins]):  # inner comprehension runs 3 times, overall O(1)
                return True         # O(1)
            buffer -= coin          # O(1)
    return False                    # O(1)

# hence the runtime of the program can be expressed by the polynomial
# 2 + 3(1 + (ceil(n/a) + ceil(n/b) + ceil(n/c))(3 * 1 + 1))
# 2 + 3O(n) = O(n)

# we have also formally proved the "bigger coin first" heuristic,
# as by the polynomial we can see that for a coin x, ceil(n/x) dominates
# the others for x smaller, which means that, given the early-stopping 
# nature of the algorithm, we can check larger coins faster.


def main() -> bool:
    parser = argparse.ArgumentParser("Coins Problem")
    parser.add_argument("a", help="First coin", type=int)
    parser.add_argument("b", help="Second coin", type=int)
    parser.add_argument("c", help="Third coin", type=int)
    parser.add_argument("w", help="Total sum to pay", type=int)

    arguments = vars(parser.parse_args()).values()

    return isPayable(*arguments)

if __name__ == "__main__":
    print(main())

