class Die:

    def __init__(self) -> None:
        self.sides = 100
        self.rolls = 0
        self.last_value = 0

    def roll(self) -> int:
        self.rolls += 1
        next_value = self.last_value + 1
        if next_value > self.sides:
            next_value -= self.sides
        self.last_value = next_value
        return next_value

    def multi_roll(self,number_of_rolls) -> int:
        total = 0
        for _ in range(0,number_of_rolls):
            total += self.roll()
        return total
