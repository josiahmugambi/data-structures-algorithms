# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char in "([{":
            # Process opening bracket
            Bracket = (char, i+1) 
            opening_brackets_stack.append(Bracket)

        if char in ")]}":
            # Process closing bracket
            if opening_brackets_stack == []:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top[0], char):                
                return i + 1
    if opening_brackets_stack == []:
        return "Success"
    else:
        return opening_brackets_stack[0][1]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
