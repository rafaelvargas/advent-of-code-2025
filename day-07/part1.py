
from functools import reduce


def count_number_of_beam_splits(lines, i, j):
    if len(lines) == i or lines[i][j] == "|":
        return 0
    if lines[i][j] == "^":
        return 1 + count_number_of_beam_splits(lines, i, j-1) + count_number_of_beam_splits(lines, i, j+1)

    lines[i][j] = "|"
    return count_number_of_beam_splits(lines, i+1, j)


def main():
    with open("input.txt", "r") as file:
        lines = list(map(lambda s: list(s.strip()), file.readlines()))

    beam_enter = 0
    for j in range(len(lines[0])):
        if lines[0][j] == "S":
            beam_enter = j
            break

    number_of_splits = count_number_of_beam_splits(lines, 0, beam_enter)
    print(f"Number of beam splits: {number_of_splits}")

if __name__ == "__main__":
    main()