from navSubsytem import Subsystem

def main():
    nav = Subsystem("Day10\DayTenInput")
    print(f'File Read')
    nav.check_data()
    nav.calc_corruption_value()
    print(f'Corruption value is: {nav.corrupt_value}')
    incompletion_value = nav.calc_incompletion_value()
    print(f'Incompletion value is: {incompletion_value}')
    print(f'End')



if __name__ == "__main__":
    main()