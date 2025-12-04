
def main():
    with open("input_part1.txt", "r") as file:
        banks = list(map(lambda x: x.strip(), file.readlines()))

    total_joltage = 0

    for bank in banks:
        largest_digit = (int(bank[0]), 0)

        for i in range(1, len(bank) - 1):
            if int(bank[i]) > largest_digit[0]:
                largest_digit = (int(bank[i]), i)
        
        next_largest_digit = (int(bank[largest_digit[1] + 1]), largest_digit[1] + 1)

        for j in range(largest_digit[1] + 1, len(bank)):
            if int(bank[j]) > next_largest_digit[0]:
                next_largest_digit = (int(bank[j]), j)
        
        total_joltage += int(str(largest_digit[0]) + str(next_largest_digit[0]))
    
    print("Sum: " + str(total_joltage))

if __name__ == "__main__":
    main()