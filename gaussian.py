# AI Attribution: This content was generated in part with the assistance of an AI model.
# Author: Tim Cotten <tim@cotten.io> @cottenio
# 2024-07-18

import argparse
from Crypto.Hash import keccak
from collections import Counter

MAX_SEED_VALUE = 2**256 - 1  # Maximum allowed seed value

def keccak256(data):
    """
    Compute Keccak-256 hash, compatible with Ethereum's implementation.

    Args:
        data (bytes): The input data to be hashed.

    Returns:
        bytes: The 32-byte Keccak-256 hash of the input data.
    """
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.digest()

def count_bits(n):
    """
    Count set bits using Brian Kernighan's algorithm.

    Args:
        n (int): The number whose set bits are to be counted.

    Returns:
        int: The count of set bits in the input number.
    """
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

def generate_bitfield(seed, size):
    """
    Generate bitfield of given size from seed using sequential Keccak-256 hashes.

    Args:
        seed (int): The seed value to start hash generation.
        size (int): The size of the bitfield to generate.

    Returns:
        int: The generated bitfield as an integer.
    """
    data = seed.to_bytes(32, 'big')
    bitfield = 0
    last_hash = 0
    while size > 0:
        hash_value = int.from_bytes(keccak256(data), 'big')
        last_hash = hash_value
        if size >= 256:
            bitfield = (bitfield << 256) | hash_value
            size -= 256
        else:
            bitfield = (bitfield << size) | (hash_value >> (256 - size))
            size = 0
        data = hash_value.to_bytes(32, 'big')
    return bitfield, last_hash

def main():
    parser = argparse.ArgumentParser(description="Analyze bit counts in Ethereum-style hashes")
    parser.add_argument("-b", "--bitfield-size", type=int, default=32, help="Size of bitfield (default: 32)")
    parser.add_argument("-n", "--num-trials", type=int, default=1000, help="Number of trials (default: 1000)")
    parser.add_argument("-s", "--seed", type=int, default=42, help="Seed value (default: 42)")
    args = parser.parse_args()

    if args.bitfield_size < 1 or args.num_trials < 1 or args.seed < 0 or args.seed > MAX_SEED_VALUE:
        parser.error("Invalid argument values")

    count_map = Counter()
    
    for _ in range(args.num_trials):
        bitfield, last_hash = generate_bitfield(args.seed, args.bitfield_size)
        count = count_bits(bitfield)
        count_map[count] += 1
        args.seed = last_hash

    print("Bit count distribution:")
    for count, frequency in sorted(count_map.items()):
        print(f"{count}: {frequency}")

if __name__ == "__main__":
    main()