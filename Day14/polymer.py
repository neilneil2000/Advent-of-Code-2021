from typing import List


class Polymer:

    def __init__(self,filename):
        self.polymer_chain = []
        self.monomer_count = {}
        self.rules = {}
        self.read_input_file(filename)

    def calculate_min_max(self):
        """Find highest and lowest occurences of monomers in chain"""
        self.highest = max(self.monomer_count,key=self.monomer_count.get)
        self.lowest = min(self.monomer_count,key=self.monomer_count.get)

    def count_monomers(self):
        unique_monomers = set(self.polymer_chain)
        for monomer in unique_monomers:
            count = self.polymer_chain.count(monomer)
            self.monomer_count.update({monomer:count})

    def run_insertion_steps(self,number_of_steps):
        for _ in range(number_of_steps):
            self.run_insertion_step()

    def run_insertion_step(self):
        new_monomers = []
        for index in range(1,len(self.polymer_chain)):
            pair = self.polymer_chain[index-1],self.polymer_chain[index]
            new_monomers.append(self.rules[pair])
        for index,monomer in enumerate(new_monomers):
            self.polymer_chain.insert(2*index+1,monomer)


    def read_input_file(self,filename):
        input = []
        with open(filename,'r') as f:
            for line in f:
                input.append(line.strip())
        self.process_input_file(input)

    def process_input_file(self,input: List):
        for line in input:
            if line.find('->') >= 0:
                line = line.split('->')
                self.rules.update({(line[0][0].strip(),line[0][1].strip()):line[1].strip()})
            elif line == '':
                pass
            else:
                self.polymer_chain.extend(list(line))

