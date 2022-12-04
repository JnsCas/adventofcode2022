def get_section_limits(section):
    [init, end] = section.split('-')
    return [int(init), int(end)]


def part_1():

    def is_fully_contained(first_section, second_section):
        [first_section_init, first_section_end] = get_section_limits(first_section)
        [second_section_init, second_section_end] = get_section_limits(second_section)
        return first_section_init >= second_section_init and first_section_end <= second_section_end

    result = 0
    with open('../inputs/4-camp-cleanup.txt') as file:
        for line in file:
            [first_section_range, second_section_range] = line.rstrip().split(',')

            if is_fully_contained(first_section_range, second_section_range) \
                    or is_fully_contained(second_section_range, first_section_range):
                result += 1
    return result


def part_2():

    def is_overlapped(first_section, second_section):
        [first_section_init, first_section_end] = get_section_limits(first_section)
        [second_section_init, second_section_end] = get_section_limits(second_section)
        first_sections = set(range(first_section_init, first_section_end + 1))

        for section in range(second_section_init, second_section_end + 1):
            if section in first_sections:
                return True
        return False

    result = 0
    with open('../inputs/4-camp-cleanup.txt') as file:
        for line in file:
            [first_section_range, second_section_range] = line.rstrip().split(',')

            if is_overlapped(first_section_range, second_section_range):
                result += 1
    return result


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
