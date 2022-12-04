import string

alphabet = list(string.ascii_lowercase + string.ascii_uppercase)


def get_priority(letter):
    return alphabet.index(letter) + 1


def part_1():
    with open('../inputs/3-rucksack-reorganization.txt') as file:
        priority_result = 0
        for line in file:
            rucksack = line.rstrip()
            half_number = int(len(rucksack) / 2)
            first_compartment = rucksack[0:half_number]
            second_compartment = rucksack[half_number:len(rucksack)]

            first_compartment_items = set(first_compartment)

            for item in second_compartment:
                if item in first_compartment_items:
                    priority_result += get_priority(item)
                    break

        return priority_result


def part_2():
    with open('../inputs/3-rucksack-reorganization.txt') as file:
        priority_result = 0
        line_number = 0
        rucksack_group = []
        for line in file:
            line_number += 1
            rucksack = line.rstrip()
            rucksack_group.append(rucksack)
            if line_number % 3 == 0:
                first_compartment_items = set(rucksack_group[0])
                second_compartment_items = set(rucksack_group[1])

                third_compartment = rucksack_group[2]
                for item in third_compartment:
                    if item in first_compartment_items and item in second_compartment_items:
                        priority_result += get_priority(item)
                        break

                rucksack_group.clear()

        return priority_result


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
