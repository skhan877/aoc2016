def parse_input(input): 
    arr = []
    with open(input, "r") as f: 
        for line in f:
            arr.append(line.replace("\n",""))
    arr = arr[0].split(", ")
    return arr

def part_one(cmds):
    dir = 0
    pos, found = [0, 0, 0, 0], []
    v = set()
    for i in range(len(cmds)):
        if cmds[i][0] == 'R':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        for j in range(int(cmds[i][1:])):
            if (pos[0] - pos[2], pos[1] - pos[3]) not in v:
                v.add((pos[0] - pos[2], pos[1] - pos[3]))
            elif not found:
                found = pos.copy()
            pos[dir] += 1
        print(pos)
    return abs(pos[0] - pos[2]) + abs(pos[1] - pos[3])

def part_two(input):
    pass

def main():
    f = "inputs/day1.txt"
    data = parse_input(f)
    # print(data)

    # data = ['R2', 'L3']
    # data = ['R2', 'R2', 'R2']
    # data = ['R5', 'L5', 'R5', 'R3']
    
    print(part_one(data))
    # print(part_two(data))

if __name__ == "__main__":
    main() 