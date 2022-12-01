def part_1():
    max_calories = -1
    current_calories = 0
    with open('../inputs/1-calories-counting-input.txt') as file:
        for line in file:
            if line == '\n':
                if current_calories > max_calories:
                    max_calories = current_calories
                current_calories = 0
            else:
                calories = int(line)
                current_calories += calories
    return max_calories


def part_2():
    calories = []
    current_calories = 0
    with open('../inputs/1-calories-counting-input.txt') as file:
        for line in file:
            if line == '\n':
                calories.append(current_calories)
                current_calories = 0
            else:
                current_calories += int(line)
    calories.sort()
    return sum(calories[-3:])


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
