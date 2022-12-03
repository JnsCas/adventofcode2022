# A rock
# B paper
# C scissors
expected_result_by_letter = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

equals_shapes = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

losser_shape_by_shape = {
    "A": "C",
    "B": "A",
    "C": "B"
}

shape_values = {
    "A": 1,
    "B": 2,
    "C": 3
}


def part_1():
    match_score = 0
    shape_score = 0
    with open('../inputs/2-rock-paper-scissors.txt') as file:
        for line in file:
            shapes = line.rstrip().split(' ')
            [opponent_shape, my_shape] = [shapes[0], equals_shapes[shapes[1]]]
            losser_shape = losser_shape_by_shape[opponent_shape]

            shape_score += shape_values[my_shape]
            if my_shape != losser_shape:
                if my_shape == opponent_shape:
                    match_score += 3
                else:
                    match_score += 6
        return match_score + shape_score


def part_2():

    def get_winner_shape_by_shape(shape):
        for winner_shape, losser_shape in losser_shape_by_shape.items():
            if shape == losser_shape:
                return winner_shape

    match_score = 0
    shape_score = 0
    with open('../inputs/2-rock-paper-scissors.txt') as file:
        for line in file:
            letters = line.rstrip().split(' ')
            [opponent_shape, expected_result] = [letters[0], expected_result_by_letter[letters[1]]]

            if expected_result == "lose":
                my_shape = losser_shape_by_shape[opponent_shape]
            elif expected_result == "draw":
                my_shape = opponent_shape
                match_score += 3
            else:
                my_shape = get_winner_shape_by_shape(opponent_shape)
                match_score += 6

            shape_score += shape_values[my_shape]

        return match_score + shape_score


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
