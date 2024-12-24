def parse_input(input): 
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))
    arr = arr[0].split(", ")
    return arr

def part_one(input):
    # print(input)
    n = len(input)
    if input[0][0] == "R": x = int(input[0][1])
    else: x = int(input[0][1]) * -1
    y = 0
    for i in range(1, n):
        # print(input[i-1], x, y)
        prev_dir = input[i-1][0]
        cur_dir = input[i][0]
        cur_move = int(input[i][1])

        if i % 2 != 0: 
        # y axis
            if prev_dir == "L":
                if cur_dir == "L": y -= cur_move
                else: y += cur_move
            else:
                if cur_dir == "L": y += cur_move
                else: y -= cur_move
        else:
        # x axis
            if prev_dir == "L":
                if cur_dir == "L": x -= cur_move
                else: x += cur_move
            else:
                if cur_dir == "L": x += cur_move
                else: x -= cur_move

    return (x, y), abs(x) + abs(y)

def part_two(input):
    pass

def main():
    f = "inputs/day1.txt"
    data = parse_input(f)
    # print(data)

    # data = ['R2', 'L3']
    # data = ['R2', 'R2', 'R2']
    data = ['R5', 'L5', 'R5', 'R3']
    
    print(part_one(data))
    print(part_two(data))

if __name__ == "__main__":
    main() 