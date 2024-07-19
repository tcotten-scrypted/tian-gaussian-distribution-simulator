# Tian-Gaussian Distribution Simulator

This project implements a novel approach to generating Gaussian-like random numbers using Ethereum-style Keccak-256 hashing. It's designed to explore the distribution of bit counts in hash-generated bitfields for analysis of their properties in relation to Gaussian distributions.

The original idea is Simon Tian's[1] and his Solidity implementation can be found here: https://github.com/simontianx/OnChainRNG/tree/main/GaussianRNG [2]

## Key Concepts

1. **Bitfields**: Generated from Keccak-256 hashes of seeds.
2. **Bit Counting**: Using Brian Kernighan's algorithm to count set bits in bitfields.

## Installation

### Prerequisites

- Python 3.x
- pycryptodome library

### Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/tcotten-scrypted/tian-gaussian-distribution-simulator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd tian-gaussian-distribution-simulator
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Simulation

To run the simulation, use the following command:

```bash
python gaussian.py [-b BITFIELD_SIZE] [-n NUM_TRIALS] [-s SEED]
```

### Command-Line Arguments

- `-b`, `--bitfield-size`: Size of bitfield (default: 32)
- `-n`, `--num-trials`: Number of trials (default: 1000)
- `-s`, `--seed`: Seed value (default: 42)

### Example Usage

```bash
python gaussian.py -b 16 -n 10000 -s 42
```

Expected output:
```
Bit count distribution:
1: 4
2: 15
3: 85
4: 314
5: 649
6: 1214
7: 1744
8: 2015
9: 1738
10: 1174
11: 653
12: 296
13: 83
14: 15
15: 1
```

## Interpretation of Results

The output shows the distribution of bit counts across the trials. In a Gaussian-like distribution:

- The counts should be roughly symmetrical around the mean.
- The mean should be close to half the bitfield size.
- The distribution should resemble a bell curve.

## Key Features

1. **Ethereum-Compatible Hashing**: Uses Keccak-256, the same hash function as Ethereum.
2. **Configurable Bitfield Size**: Allows exploration of different-sized bitfields.
3. **Multiple Trials**: Supports running multiple trials for statistical analysis.
4. **Efficient Bit Counting**: Utilizes Kernighan's algorithm for fast bit counting.

## Limitations and Considerations

- The generated distribution is discrete, unlike a true Gaussian distribution.
- The statistical properties may vary based on bitfield size and number of trials.
- This method is experimental and may not perfectly mimic a true Gaussian distribution.

## Citations

1. S. Tian, "On-chain Gaussian Randomness is Now Made Available," Medium, Aug. 12, 2021. [Online]. Available: https://medium.com/@maxareo/on-chain-gaussianity-is-available-now-1409c7f14cbe. [Accessed: Jul. 18, 2024].

2. S. Tian, "OnChainRNG," GitHub repository, 2021. [Online]. Available: https://github.com/simontianx/OnChainRNG/tree/main/GaussianRNG. [Accessed: Jul. 18, 2024].

## AI Attribution

This content was generated in whole or part with the assistance of an AI model - see the [AI.md](AI.md) file for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
