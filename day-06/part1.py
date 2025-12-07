
from functools import reduce

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    operands = list(map(lambda s: list(filter(lambda s: s != "", s.split(" "))), list(map(lambda s: s.strip(), lines[:-1]))))
    operators = list(filter(lambda s: s != "", lines[-1].strip().split(" ")))

    transposed_operands = [[int(operands[i][j]) for i in range(len(operands))] for j in range(len(operands[0]))]
    total = 0

    for operands, operator in zip(transposed_operands, operators):
        if operator == "*":
            total += reduce(lambda x, y: x * y, operands)
        elif operator == "+":
            total += reduce(lambda x, y: x + y, operands)

    print(f"Total sum: {total}")

if __name__ == "__main__":
    main()