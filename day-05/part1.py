
def main():
    with open("input.txt", "r") as file:
        row = 0
        line_separator_row = 0
        lines = []
        for line in file:
            if line == "\n":
                line_separator_row = row
            lines.append(line.strip())
            row += 1
    
    ranges = list(map(lambda s: list(map(int, s.split("-"))), lines[:line_separator_row]))
    ids = list(map(int, lines[line_separator_row + 1:]))

    ranges = sorted(ranges, key=lambda x: x[0])
    ids = sorted(ids)
    
    number_of_fresh_ingredients = 0
    current_range_index = 0

    for i in range(len(ids)):
        while current_range_index < len(ranges):
            if ids[i] < ranges[current_range_index][0]: 
                break
            elif ids[i] <= ranges[current_range_index][1]:
                number_of_fresh_ingredients += 1
                break
            current_range_index += 1
    
    print(f"Number of fresh ingredients: {number_of_fresh_ingredients}")




if __name__ == "__main__":
    main()