from Amphipod import AmphipodGrid

def main():
    large_warren = AmphipodGrid("Day23\DayTwentyThreePart2Input")
    #large_warren.force_game()
    large_warren.compute_best_score()
    print(f'END')



if __name__ == '__main__':
    main()