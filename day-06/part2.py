
from functools import reduce

def main():
    with open("input.txt", "r") as file:
        lines = list(map(lambda s: s.replace("\n", ""), file.readlines()))

    operands = []
    current_operands = []
    operators = list(filter(lambda s: s != "", lines[-1].strip().split(" ")))
    total = 0

    for i in range(len(lines[0])):
        joined_digits = "".join(map(lambda l: l[i], lines[:-1]))

        if joined_digits.replace(" ", "") == "":
            operands.append(current_operands)
            current_operands = []
            continue
        
        current_operands.append(int(joined_digits))
    operands.append(current_operands)

    for operands, operator in zip(operands, operators):
        if operator == "*":
            total += reduce(lambda x, y: x * y, operands)
        elif operator == "+":
            total += reduce(lambda x, y: x + y, operands)

    print(f"Total sum: {total}")

if __name__ == "__main__":
    main()