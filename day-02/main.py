
import math

def main():
    with open("input.txt", "r") as file:
        ranges_as_str = file.readline()
        ranges = list(map(lambda r: r.split("-"), ranges_as_str.strip().split(",")))

    current_sum = 0
    for r in ranges:
        range_start = int(r[0])
        range_end = int(r[1])

        for n in range(range_start, range_end + 1):
            n_as_str = str(n)
            middle_index = math.floor(len(n_as_str) / 2)
            if n_as_str[:middle_index] == n_as_str[middle_index:]:
                current_sum += n
    
    print("Sum: " + str(current_sum))

if __name__ == "__main__":
    main()