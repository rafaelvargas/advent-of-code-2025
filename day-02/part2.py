


import math

def main():
    with open("input_part2.txt", "r") as file:
        ranges_as_str = file.readline()
        ranges = list(map(lambda r: r.split("-"), ranges_as_str.strip().split(",")))

    current_sum = 0
    for r in ranges:
        range_start = int(r[0])
        range_end = int(r[1])

        for n in range(range_start, range_end + 1):
            n_as_str = str(n)

            for substring_length in range(1, math.floor(len(n_as_str) / 2) + 1):
                if (len(n_as_str) % substring_length) == 0:
                    has_common_substring = True
                    first_substring = n_as_str[:substring_length]

                    for i in range(1, int(len(n_as_str) / substring_length)):
                        next_substring = n_as_str[i * substring_length: (i + 1) * substring_length]
                        if next_substring != first_substring:
                            has_common_substring = False
                            break
                    
                    if has_common_substring:
                        current_sum += n
                        break
    
    print("Sum: " + str(current_sum))

if __name__ == "__main__":
    main()