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
    for i in range (len(text) - len(pattern) + 1):
        t_hash = poly_hash(text[i:i + len(pattern)], big_prime, x)
        if p_hash != t_hash:
            continue

        if (text[i:i + len(pattern)]) == pattern:
            positions.append(i)        
    return positions

def poly_hash(S, p, x):
    po_hash = 0
    for i in range(len(S) - 1, -1, -1):
        po_hash = (((po_hash * x + ord(S[i])) % p) + p)%p
    return po_hash
    
def are_equal(S1, S2):
    if len(S1) == len(S2):
        return False
    for i in range(len(S1)-1):
        if S1[i] != S2[i]:
            return False
    return True

if __name__ == '__main__':
    print_occurrences(get_occurrences_rk(*read_input()))

