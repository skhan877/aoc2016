def parse_input(input): 
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))
    arr = arr[0].split(", ")
    return arr

def part_one(input):
    n = len(input)
    x_moves = input[::2]
    y_moves = input[1::2]
    # return x_moves, y_moves

    if input[0][0] == "R": x = int(input[0][1])
    else: x = int(input[0][1]) * -1
    y = 0

    # coords = [int(input[0][-1]), 0]

    for i in range(1,10):
        print(x, y)
        if i % 2 != 0: 
        # y axis
            if input[i-1][0] == "L":
                if input[i][0] == "L": y -= int(input[i][1])
                else: y += int(input[i][1])
            else:
                if input[i][0] == "L": y -= int(input[i][1])
                else: y += int(input[i][1])
        else:
        # x axis
            if input[i-1][0] == "L":
                if input[i][0] == "L": x += int(input[i][1])
                else: x -= int(input[i][1])
            else:
                if input[i][0] == "L": y += int(input[i][1])
                else: x -= int(input[i][1])

    return ('final', x, y)

def part_two(input):
    pass

def main():
    f = "inputs/day1.txt"
    data = parse_input(f)
    print(data)
    print(part_one(data))
    print(part_two(data))

if __name__ == "__main__":
    main() 