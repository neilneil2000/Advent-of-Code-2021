from typing import Tuple, List
from dataclasses import dataclass


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
        x = block.x_dimension[1] - block.x_dimension[0] + 1
        y = block.y_dimension[1] - block.y_dimension[0] + 1
        z = block.z_dimension[1] - block.z_dimension[0] + 1

        return x * y * z

    def execute_boot_sequence(self, instructions: List[Instruction]) -> None:
        """Run through all boot sequence instructions"""
        for instruction in instructions:
            self.process_instruction(instruction)

    def process_instruction(self, instruction: Tuple[str, Block]):
        """Process single block"""
        state, block = instruction
        if state == "on":
            self.process_on_block([block])
        elif state == "off":
            self.process_off_block([block])
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
            if splinters == []:
                return  # Block is entirely covered by existing blocks
            unprocessed_blocks = splinters
        if unprocessed_blocks != []:
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
        """Removes small_block from large_block where small_block is completely enveloped by large_block. Returns a list of blocks which cover the remaining area"""
        x_chunks = self.chunk_1d(small_block.x_dimension, large_block.x_dimension)
        y_chunks = self.chunk_1d(small_block.y_dimension, large_block.y_dimension)
        z_chunks = self.chunk_1d(small_block.z_dimension, large_block.z_dimension)

        result = []
        for x in x_chunks:
            for y in y_chunks:
                for z in z_chunks:
                    result.append(Block(x, y, z))

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
    my_reactor = Reactor()
    block_a = Block((0, 9), (0, 9), (0, 9))
    block_b = Block((6, 15), (6, 15), (6, 15))

    my_reactor.process_on_block([block_a])
    my_reactor.process_on_block([block_b])
    my_reactor.process_off_block(block_a)
    my_reactor.process_off_block(block_b)

    print(f"Block A: {my_reactor.count_cubes_in_block(block_a)} Cubes\n{block_a}\n")
    print(f"Block B: {my_reactor.count_cubes_in_block(block_b)} Cubes\n{block_b}\n")

    overlapping_block = my_reactor.overlap(block_a, block_b)
    print(
        f"Overlapping Block: {my_reactor.count_cubes_in_block(overlapping_block)} Cubes\n{overlapping_block}\n"
    )
    new_blocks = my_reactor.subtract_blocks(block_b, overlapping_block)

    overlap_cubes = 0
    for block in new_blocks:
        overlap_cubes += my_reactor.count_cubes_in_block(block)
    print(f"Additional Blocks: {overlap_cubes} Cubes")
    for block in new_blocks:
        print(block)


def process_input_file(input: list) -> list:
    output = []
    for line in input:
        on_off, co_ords = line.split(" ")
        co_ords = co_ords.split(",")
        x, y, z = co_ords
        x = x.split("=")[1].split("..")
        x[0] = int(x[0])
        x[1] = int(x[1])
        y = y.split("=")[1].split("..")
        y[0] = int(y[0])
        y[1] = int(y[1])
        z = z.split("=")[1].split("..")
        z[0] = int(z[0])
        z[1] = int(z[1])
        cuboid = (on_off, (x, y, z))
        output.append(cuboid)
    return output


def read_input_file(filename) -> list:
    input = []
    with open(filename, "r") as f:
        for line in f:
            input.append(line.strip())
    return input


if __name__ == "__main__":
    main()
