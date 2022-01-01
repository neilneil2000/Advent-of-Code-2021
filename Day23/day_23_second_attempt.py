from amphipod_cave import AmphipodCave


def main():
    cave = AmphipodCave()
    populate_cave(cave)
    print(cave.pod_locations())
    solve(cave)
    pass


def solve(cave: AmphipodCave):
    moves = cave.next_moves()
    for move in moves:
        pod, location = move
        cave.do_move(pod, location)


def populate_cave(cave: AmphipodCave):
    colour_list = [
        "C",
        "D",
        "D",
        "B",
        "B",
        "C",
        "B",
        "C",
        "D",
        "B",
        "A",
        "A",
        "D",
        "A",
        "C",
        "A",
    ]
    pod_pointer = 0
    while pod_pointer < 4:
        cave.place_new_amphipod(colour_list[pod_pointer], (3, pod_pointer + 2))
        pod_pointer += 1

    while pod_pointer < 8:
        cave.place_new_amphipod(colour_list[pod_pointer], (5, pod_pointer - 2))
        pod_pointer += 1

    while pod_pointer < 12:
        cave.place_new_amphipod(colour_list[pod_pointer], (7, pod_pointer - 6))
        pod_pointer += 1

    while pod_pointer < 16:
        cave.place_new_amphipod(colour_list[pod_pointer], (9, pod_pointer - 10))
        pod_pointer += 1


if __name__ == "__main__":
    main()
