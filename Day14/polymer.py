from typing import List


class Polymer:
    def __init__(self,filename):
        self.monomer_count = {}
        self.pair_count = {}
        self.end_monomer = set()
        self.rules = {}
        self.read_input_file(filename)

    def calculate_min_max(self):
        """Find highest and lowest occurences of monomers in chain"""
        self.highest = max(self.monomer_count,key=self.monomer_count.get)
        self.lowest = min(self.monomer_count,key=self.monomer_count.get)

    def count_monomers(self):
        monomers = {}
        for pair in self.rules.keys():
            monomers.update({pair[0]:0})
            monomers.update({pair[1]:0})
        for pair in self.pair_count:
            for monomer in pair:
                count = monomers[monomer] + self.pair_count[pair]
                monomers.update({monomer:count})
        for monomer in monomers:
            if monomer in self.end_monomer:
                monomers[monomer] +=1
            monomers[monomer] = int(monomers[monomer]/2)
        self.monomer_count = monomers

    def run_insertion_steps(self,number_of_steps):
        for _ in range(number_of_steps):
            self.run_insertion_step()

    def run_insertion_step(self):
        new_pair_count = self.blank_pair_count.copy()
        for pair in self.pair_count:
            rules = self.rules[pair]
            for rule in rules:
                count = new_pair_count[rule]
                existing_count = self.pair_count[pair]
                new_pair_count.update({rule:count+existing_count})
        self.pair_count = new_pair_count


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
                input = list(line[0].strip())
                input.insert(1,line[1].strip())
                new_rule = {
                    (input[0],input[2]):[(input[0],input[1]),(input[1],input[2])]
                    }
                self.rules.update(new_rule)
            elif line == '':
                pass
            else:
                polymer_chain = line
        #Set Starting Position
        self.end_monomer.add(polymer_chain[0])
        self.end_monomer.add(polymer_chain[-1])
        for key in self.rules.keys():
            self.pair_count.update({key:0})
        self.blank_pair_count = self.pair_count.copy()
        for x in range(1,len(polymer_chain)):
            pair = (polymer_chain[x-1],polymer_chain[x])
            count = self.pair_count[pair]
            self.pair_count.update({pair:count+1})