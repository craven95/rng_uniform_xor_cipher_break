import random

def get_cipher():
    challenge = ""
    with open('solution.txt', 'r') as solved:
        solution = ""
        for line in solved:
            for letter in line.strip():
                as_binary = bin(ord(letter))[2:].zfill(8)  # ASCII TO BINARY
                solution += as_binary
    new_b = ""
    for b in solution:
        new_b += str(int(b) ^ (random.uniform(0, 1) < 0.75))
    return new_b, solution
