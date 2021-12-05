from array import *

class BingoCard:

    def __init__(self):
        self.values = []
        self.drawn = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.won = False


    def sum_remaining_values(self):
        sum = 0
        for x in range(0,5):
            for y in range(0,5):
                if self.drawn[x][y] == 0:
                    sum += self.values[x][y]
        return sum
        


    def check_row(self,row):
        if sum(self.drawn[row]) == 5:
            self.won = True

    def check_column(self,column):
        sum = 0
        for x in range(0,5):
            sum += self.drawn[x][column]
        if sum == 5:
            self.won = True

    def check_new_number(self,new_number):
        for x in range(0,5):
            for y in range(0,5):
                if self.values[x][y] == new_number:
                    self.drawn[x][y] = 1
                    self.check_row(x)
                    self.check_column(y)

    def add_row(self,row):
        if len(row) != 5:
            print("Row list must contain 5 items")
            return False
        if len(self.values) < 5:
            self.values.append(row)
            for x in range(0,5):
                self.values[len(self.values)-1][x] = int(self.values[len(self.values)-1][x])
            return True
        else:
            print("Cannot Add Row")
            return False