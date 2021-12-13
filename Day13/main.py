from FoldablePaper import FoldablePaper

def main():
    paper = FoldablePaper("Day13\DayThirteenInput")
    for fold in paper.folds:
        paper.execute_next_fold()
        print(f'{len(paper.points)} points remain')
    paper.print_points()
    print('END')



if __name__ == '__main__':
    main()