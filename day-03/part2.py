
NUMBER_OF_DIGITS = 12

def main():
    with open("input_part2.txt", "r") as file:
        banks = list(map(lambda x: x.strip(), file.readlines()))

    total_joltage = 0

    for bank in banks:
        final_digits = []
        last_largest_digit = (int(bank[0]), 0)

        for d in range(NUMBER_OF_DIGITS, 0, -1):
            for i in range(last_largest_digit[1], len(bank) - d + 1):
                if int(bank[i]) > last_largest_digit[0]:
                    last_largest_digit = (int(bank[i]), i)
            
            final_digits.append(str(last_largest_digit[0]))
            if len(final_digits) != NUMBER_OF_DIGITS:
                last_largest_digit = (int(bank[last_largest_digit[1] + 1]), last_largest_digit[1] + 1)
        
        total_joltage += int("".join(final_digits))
    
    print("Sum: " + str(total_joltage))

if __name__ == "__main__":
    main()