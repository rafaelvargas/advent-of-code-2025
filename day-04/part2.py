
import copy

def main():
    with open("input.txt", "r") as file:
        matrix = list(map(lambda x: list(x.strip()), file.readlines()))
        new_matrix = copy.deepcopy(matrix)

    number_of_rolls_removed = 0

    while True:
        forklifts = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                adjacent_rolls = 0

                if matrix[i][j] == "@":
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if k == 0 and l == 0:
                                continue
                            if (i + k < 0) or (j + l < 0) or (i + k >= len(matrix)) or (j + l >= len(matrix[0])):
                                continue
                            if matrix[i + k][j + l] == "@":
                                adjacent_rolls += 1
                
                    if adjacent_rolls < 4:
                        forklifts += 1
                        new_matrix[i][j] = "x"

        matrix = copy.deepcopy(new_matrix)
        number_of_rolls_removed += forklifts

        if forklifts == 0:
            break
                        
    print(f"Number of Rolls Removed: {number_of_rolls_removed}")

if __name__ == "__main__":
    main()