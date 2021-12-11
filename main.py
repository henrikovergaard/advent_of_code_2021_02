DEPTH = 'depth'
HORIZONTAL = 'horizontal'


def getdirection(line: str):
    if line.startswith('forward'):
        return HORIZONTAL, int(line.split(' ')[1])
    if line.startswith('up'):
        return DEPTH, - int(line.split(' ')[1])
    if line.startswith('down'):
        return DEPTH, int(line.split(' ')[1])


def part_one():
    depth = 0
    horizontal = 0
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        direction = getdirection(line)
        if direction[0] == DEPTH:
            depth += direction[1]
        else:
            horizontal += direction[1]
    return depth * horizontal


def part_two():
    aim = 0
    depth = 0
    horizontal = 0
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        direction = getdirection(line)
        if direction[0] == DEPTH:
            aim += direction[1]
        else:
            forward = direction[1]
            horizontal += forward
            depth += (aim * forward)
    return horizontal * depth


if __name__ == '__main__':
    print('result part one', part_one())
    print('result part two', part_two())
