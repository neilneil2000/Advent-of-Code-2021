from Game import Game

def main():
    practice_game = Game([10,3])
    score, rolls = practice_game.play_game(1000)
    print(f'Winning Score: {score} after {rolls} rolls. Answer = {score*rolls}')

if __name__ == "__main__":
    main()