
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
    ranges = sorted(ranges, key=lambda x: x[0])
    
    last_fresh_ingredient_id = ranges[0][1]
    number_of_fresh_ingredients = ranges[0][1] - ranges[0][0] + 1

    for i in range(1, len(ranges)):
        if ranges[i][1] <= last_fresh_ingredient_id:
            continue
        if ranges[i][0] <= last_fresh_ingredient_id:
            number_of_fresh_ingredients += ranges[i][1] - last_fresh_ingredient_id
        else:
            number_of_fresh_ingredients += ranges[i][1] - ranges[i][0] + 1
        
        last_fresh_ingredient_id = max(ranges[i][1], last_fresh_ingredient_id)
    
    print(f"Number of fresh ingredients from ranges: {number_of_fresh_ingredients}")

if __name__ == "__main__":
    main()