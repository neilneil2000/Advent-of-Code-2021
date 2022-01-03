"""Solution to Advent of Code 2021 Day 22"""
from typing import Tuple, List
from dataclasses import dataclass
from time import perf_counter


@dataclass
class Block:
    """Dataclass representing a cuboid of space in the Reactor"""

    x_dimension: Tuple[int, int]
    y_dimension: Tuple[int, int]
    z_dimension: Tuple[int, int]


@dataclass
class Instruction:
    """Represents a single instruction to turn a block on or off"""

    state: str
    block: Block


class Reactor:
    """Representation of a Reactor"""

    def __init__(self):
        self.on_blocks = []

    def count_lit_cubes(self) -> int:
        """Counts number of lit cubes in self.on_blocks"""
        lit_cubes = 0
        for block in self.on_blocks:
            lit_cubes += self.count_cubes_in_block(block)

        return lit_cubes

    def count_cubes_in_block(self, block: Block) -> int:
        """Counts number of cubes in block"""
        _x = block.x_dimension[1] - block.x_dimension[0] + 1
        _y = block.y_dimension[1] - block.y_dimension[0] + 1
        _z = block.z_dimension[1] - block.z_dimension[0] + 1

        return _x * _y * _z

    def process_instruction(self, instruction: Tuple[str, Block]):
        """Process single block"""
        state, block = instruction
        if state == "on":
            self.process_on_block(block)
        elif state == "off":
            self.process_off_block(block)
        else:
            print("Invalid Block State")
            print(block)

    def process_on_block(self, on_block: Block) -> None:
        """Update Reactor to turn ON this block"""
        unprocessed_blocks = [on_block]
        for existing_block in self.on_blocks:
            splinters = []
            for new_block in unprocessed_blocks:
                overlap = self.overlap(existing_block, new_block)
                if overlap is None:
                    splinters.append(new_block)
                else:
                    splinters.extend(self.subtract_blocks(new_block, overlap))
            if not splinters:
                return  # Block is entirely covered by existing blocks
            unprocessed_blocks = splinters
        if unprocessed_blocks:
            for new_block in unprocessed_blocks:
                self.on_blocks.append(new_block)

    def process_off_block(self, off_block: Block) -> None:
        """Update Reactor to turn OFF this block"""
        current_blocks = self.on_blocks.copy()
        for on_block in current_blocks:
            overlap = self.overlap(on_block, off_block)
            if overlap is not None:
                self.on_blocks.extend(self.subtract_blocks(on_block, overlap))
                self.on_blocks.remove(on_block)

    def chunk_1d(
        self, small: Tuple[int, int], large: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Chunks up a single dimension into 1,2 or 3 parts where small line fits inside large line
        +------------small-------------+
        +------------large-------------+
        Return [small]

        +-------small------+
        +----------large------------+
        Return [small,right_segment]

                 +-------small------+
        +----------large------------+
        Return [small,left_segment]

             +-------small------+
        +----------large------------+
        Return [small,left_segment, right_segment]
        """
        chunks = [small]
        if small[0] > large[0]:
            chunks.append((large[0], small[0] - 1))
        if small[1] < large[1]:
            chunks.append((small[1] + 1, large[1]))
        return chunks

    def subtract_blocks(self, large_block: Block, small_block: Block) -> List[Block]:
        """
        Removes small_block from large_block
        where small_block is completely enveloped by large_block.
        Returns a list of blocks which cover the remaining area
        """
        x_chunks = self.chunk_1d(small_block.x_dimension, large_block.x_dimension)
        y_chunks = self.chunk_1d(small_block.y_dimension, large_block.y_dimension)
        z_chunks = self.chunk_1d(small_block.z_dimension, large_block.z_dimension)

        result = []
        for _x in x_chunks:
            for _y in y_chunks:
                for _z in z_chunks:
                    result.append(Block(_x, _y, _z))

        result.remove(small_block)
        return result

    def overlap(self, block_a: Block, block_b: Block) -> Block | None:
        """Returns overlapping Block of two blocks"""
        overlap_x = self.overlap_1d(block_a.x_dimension, block_b.x_dimension)
        if overlap_x is None:
            return None
        overlap_y = self.overlap_1d(block_a.y_dimension, block_b.y_dimension)
        if overlap_y is None:
            return None
        overlap_z = self.overlap_1d(block_a.z_dimension, block_b.z_dimension)
        if overlap_z is None:
            return None

        return Block(overlap_x, overlap_y, overlap_z)

    def overlap_1d(
        self, line_a: Tuple[int, int], line_b: Tuple[int, int]
    ) -> Tuple[int, int] | None:
        """Returns overlapping section between two lines"""
        a_low, a_high = line_a
        b_low, b_high = line_b

        overlap_low = max(a_low, b_low)
        overlap_high = min(a_high, b_high)

        if overlap_low > overlap_high:
            return None
        return overlap_low, overlap_high


def main():
    """Read file and compute number of cubes lit following Reactor boot sequence"""
    print("Program Started")
    my_reactor = Reactor()
    print("Reading Input File")
    input_file = read_input_file("Day22\\DayTwentyTwoInput")
    instructions = process_input_file(input_file)
    print(f"Input File Processed: {len(instructions)} Instructions Found\n")
    count = 1
    for instruction in instructions:
        start = perf_counter()
        my_reactor.process_instruction(instruction)
        end = perf_counter()
        print(
            f"Instruction {count} Processed in {int(end-start)} \
                Seconds: {instruction[0], instruction[1]}"
        )
        count += 1
    print("\nFinished Processing All Instructions\nCounting Cubes...\n")
    print(f"{my_reactor.count_lit_cubes()}: Cubes Lit at end of sequence")


def process_input_file(input_file: List[str]) -> List[Tuple[str, Block]]:
    """Process Input file from list of strings to executable instructions"""
    instructions = []
    for line in input_file:
        on_off, co_ords = line.split(" ")
        co_ords = co_ords.split(",")
        _x, _y, _z = co_ords
        _x = _x.split("=")[1].split("..")
        _x[0] = int(_x[0])
        _x[1] = int(_x[1])
        _y = _y.split("=")[1].split("..")
        _y[0] = int(_y[0])
        _y[1] = int(_y[1])
        _z = _z.split("=")[1].split("..")
        _z[0] = int(_z[0])
        _z[1] = int(_z[1])
        instruction = (on_off, Block(_x, _y, _z))
        instructions.append(instruction)
    return instructions


def read_input_file(filename: str) -> List[str]:
    """Read file from disk and convert to list of strings"""
    input_file = []
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            input_file.append(line.strip())
    return input_file


if __name__ == "__main__":
    main()
