from FoldablePaper import FoldablePaper

def main():
    paper = FoldablePaper("Day13\DayThirteenInput")
    paper.execute_next_fold()
    print(f'{len(paper.points)} points remain')
    print('END')



if __name__ == '__main__':
    main()