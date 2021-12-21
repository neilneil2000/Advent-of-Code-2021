from DiracGame import DiracGame
from Game import Game

def main():
    starting_places = [10,3]

    practice_game = Game(starting_places)
    score, rolls = practice_game.play_game(1000)
    print(f'Winning Score: {score} after {rolls} rolls. Answer = {score*rolls}')

    dirac_game = DiracGame(starting_places)
    winning_score = dirac_game.play_full_game()
    print(f'Winning Player Wins in {winning_score} universes')

if __name__ == "__main__":
    main()