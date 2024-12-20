def parse_input(input): 
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))
    arr = arr[0].split(", ")
    return arr

def part_one(input):
    x_moves = input[::2]
    y_moves = input[1::2]
    # return x_moves, y_moves
    coords = (int(input[0][-1]), 0)
    return coords

def part_two(input):
    pass

def main():
    f = "inputs/day1.txt"
    data = parse_input(f)
    # print(data)
    print(part_one(data))
    print(part_two(data))

if __name__ == "__main__":
    main() 