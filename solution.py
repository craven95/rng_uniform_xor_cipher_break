import random


def get_cipher():
    challenge = ""
    with open('solution.txt','r') as solved:
        solution = ""
        for line in solved:
            for letter in line.strip():
                as_binary = bin(ord(letter))[2:].zfill(8)  # ASCII TO BINARY
                solution += as_binary
    new_b = ""
    for b in solution:
        new_b += str(int(b) ^ (random.uniform(0,1) < 0.75))
    return new_b


def solution():
    new_b=[]
    decrypt=''
    for i in range(0,100):
        new_b.append(get_cipher())
    print(new_b)
    for j in range(0,len(new_b[0])):
        one = 0
        zero = 0
        for i in range(0,100):
            if int(new_b[i][j]) == 1:
                one = one + 1
            else:
                zero = zero + 1
        if one > zero:
            decrypt += str(0)
        else:
            decrypt+= str(1)
    return decrypt


decrypt = solution()
print (decrypt)