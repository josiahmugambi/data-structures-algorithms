# Algorithmic Toolbox 
# Week 1 
# Programming Assignment #1
# Sum of Digits

def sum_of_two_digits(first_digit, second_digit):
    '''
    return the sum of the two digits provided
    '''
    return first_digit + second_digit

if __name__ == '__main__':
    a, b = map(int, input().split())
    print (sum_of_two_digits(a,b))