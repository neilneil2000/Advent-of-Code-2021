from amphipod_cave import AmphipodCave


def main():
    cave = AmphipodCave()
    test_map = {
        (1, 1): None,
        (2, 1): None,
        (3, 1): None,
        (4, 1): None,
        (5, 1): None,
        (6, 1): None,
        (7, 1): None,
        (8, 1): None,
        (9, 1): None,
        (10, 1): None,
        (11, 1): None,
        (3, 2): "B",
        (3, 3): "D",
        (3, 4): "D",
        (3, 5): "A",
        (5, 2): "C",
        (5, 3): "C",
        (5, 4): "B",
        (5, 5): "D",
        (7, 2): "B",
        (7, 3): "B",
        (7, 4): "A",
        (7, 5): "C",
        (9, 2): "D",
        (9, 3): "A",
        (9, 4): "C",
        (9, 5): "A",
    }
    my_map = {
        (1, 1): None,
        (2, 1): None,
        (3, 1): None,
        (4, 1): None,
        (5, 1): None,
        (6, 1): None,
        (7, 1): None,
        (8, 1): None,
        (9, 1): None,
        (10, 1): None,
        (11, 1): None,
        (3, 2): "C",
        (3, 3): "D",
        (3, 4): "D",
        (3, 5): "B",
        (5, 2): "B",
        (5, 3): "C",
        (5, 4): "B",
        (5, 5): "C",
        (7, 2): "D",
        (7, 3): "B",
        (7, 4): "A",
        (7, 5): "A",
        (9, 2): "D",
        (9, 3): "A",
        (9, 4): "C",
        (9, 5): "A",
    }
    print()
    print("=================")
    print(" PROGRAM STARTED")
    print("=================")
    cave.print_cave(my_map)
    print(f"Initial Target: {cave.best_score}. Now Solving...")
    cave.take_turn(my_map, 0)
    print(cave.best_score)


if __name__ == "__main__":
    main()
