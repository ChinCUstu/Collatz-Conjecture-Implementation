# Collatz Conjecture Implementation

This repository contains a Python program that implements the Collatz Conjecture, a mathematical hypothesis proposed by Lothar Collatz in 1937. The conjecture is simple yet unsolved, and it has intrigued mathematicians for decades.

## The Conjecture

The Collatz Conjecture applies to any positive integer. Here's how it works:

1. Start with any positive integer `n`.
2. If `n` is even, the next term is `n / 2`.
3. If `n` is odd, the next term is `3n + 1`.
4. Repeat the process indefinitely for every term to get a sequence of numbers.
5. The conjecture states that no matter what number you start with, eventually, you will reach `1`.

Despite its simplicity, the conjecture has not been proven or disproven for all positive integers.

## The Program

The Python program in this repository takes a non-negative and non-zero integer as input from the user and performs operations based on whether the number is even or odd until the number becomes `1`. The program also counts and prints the number of steps it takes to reach `1` from the initial number.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory containing the program.
3. Run the program using Python 3.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
