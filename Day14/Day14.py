from polymer import Polymer

def main():
    my_polymer = Polymer("Day14\DayFourteenInput")
    print(my_polymer.polymer_chain)
    my_polymer.run_insertion_steps(10)
    my_polymer.count_monomers()
    my_polymer.calculate_min_max()
    print(f'Highest = {my_polymer.highest}')
    print(f'Lowest = {my_polymer.lowest}')
    print(f'Answer is: {my_polymer.monomer_count[my_polymer.highest] - my_polymer.monomer_count[my_polymer.lowest]}')
    print("END")

if __name__ == '__main__':
    main()