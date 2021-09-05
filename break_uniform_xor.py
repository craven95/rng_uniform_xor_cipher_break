import random
from tqdm import tqdm
from termcolor import colored


def score(input_string_1, input_string_2):
    somme = 0
    for c1, c2 in zip(input_string_1, input_string_2):
        if c1 == c2:
            somme += 1
    return somme / len(input_string_1) * 100


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


# My solution
print(colored("[+] Acquisition ciphertext data ...", 'green'))
challenges = []
try_number = 1000
for t in tqdm(range(try_number)):
    # print('*'*(int(t/try_number*100)))
    challenge, solution = get_cipher()
    challenges.append(challenge)
    # print(challenge)
# print(challenges)

somme = 0
res = ''
print(colored("[+] Data processed successfully !", "green"))
print(colored("[+] Processing data ...", "green"))
for i in range(len(challenges[0])):
    for j in range(len(challenges)):
        somme += int(challenges[j][i])
    if somme >= try_number / 2:
        res += '0'
    else:
        res += '1'
    somme = 0
word = (binascii.unhexlify('%x' % int(solution, 2))).decode()
if solution == res:
    print(colored("[+] Decryption successfull !", "green"))
    print(word)
else:
    print(colored(f"[-] Decryption failed : score is {score(solution, res)} %.", "red"))
