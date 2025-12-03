
def main():
    current_position = 50
    dial_pointing_zero_counter = 0

    with open("input.txt", "r") as file:
        rotations = list(map(lambda x: x.strip(), file.readlines()))

    for r in rotations:
        direction = r[0]
        distance = int(r[1:]) % 100
        if direction == "L":
            new_position = current_position - distance
            if new_position < 0:
                current_position = 100 + new_position
            else:
                current_position = new_position
        elif direction == "R":
            new_position = current_position + distance
            if new_position > 99:
                current_position = new_position - 100
            else:
                current_position = new_position
        
        if current_position == 0:
            dial_pointing_zero_counter += 1
    
    print("Count: " + str(dial_pointing_zero_counter))

if __name__ == "__main__":
    main()