# python3

import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_rk(pattern, text):
    big_prime = 100000007
    x = random.randint(1, big_prime - 1)
    positions = []
    p_hash = poly_hash(pattern, big_prime, x)
    H = pre_compute_hashes(text, pattern, big_prime, x)
    for i in range (len(text) - len(pattern) + 1):

        if p_hash != H[i]:
            continue

        if (text[i:i + len(pattern)]) == pattern:
            positions.append(i)        
    return positions

def poly_hash(S, p, x):
    po_hash = 0
    for i in range(len(S) - 1, -1, -1):
        po_hash = (((po_hash * x + ord(S[i])) % p) + p) % p
    return po_hash

def pre_compute_hashes(text, pattern, p, x):
    H = [0] * (len(text) - len(pattern) + 1)
    S = text[len(text) - len(pattern): len(text)  ]
    H[len(text) - len(pattern)] = poly_hash(S, p, x)
    y = 1
    for i in range(0, len(pattern)):
        y = (y * x) % p
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        H[i] = (x*H[i+1] + ord(text[i]) - y*ord(text[i + len(pattern)])) % p
    return H

if __name__ == '__main__':
    print_occurrences(get_occurrences_rk(*read_input()))

