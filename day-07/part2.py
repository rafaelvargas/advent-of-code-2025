
def main():
    with open("input.txt", "r") as file:
        lines = list(map(lambda s: list(s.strip()), file.readlines()))

    beam_start = 0
    for j in range(len(lines[0])):
        if lines[0][j] == "S":
            beam_start = j
            break

    timeline_counters = [0 for _ in range(len(lines[0]))]
    timeline_counters[beam_start] = 1

    for i in range(1, len(lines)):
        new_timeline_counters = [0 for _ in range(len(lines[0]))]
        for j in range(0, len(lines[0])):
            if timeline_counters[j] > 0:
                if lines[i][j] == "^":
                    new_timeline_counters[j-1] += timeline_counters[j]
                    new_timeline_counters[j+1] += timeline_counters[j]
                else:
                    new_timeline_counters[j] += timeline_counters[j]

        timeline_counters = new_timeline_counters

    print(f"Number of timelines: {sum(timeline_counters)}")

if __name__ == "__main__":
    main()