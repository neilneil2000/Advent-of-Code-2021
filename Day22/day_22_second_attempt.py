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

    def process_on_block(self, unprocessed_blocks: List[Block]) -> None:
        """Update Reactor to turn ON this block"""
        for existing_block in self.on_blocks:
            result_blocks = []
            for block in unprocessed_blocks:
                result_blocks.append(self.underlap(block, existing_block))
            if result_blocks == []:
                return  # Block is entirely covered by existing blocks
            unprocessed_blocks = result_blocks
        if unprocessed_blocks != []:
            for block in unprocessed_blocks:
                self.on_blocks.append(block)

        """WRITING OUT LONG HAND TO HELP MY BRAIN"""
        # 1. Compare new block to first existing block. Possible Outcomes:
        #   - No overlap: return entire new_block
        #   - Total overlap: return [] / None
        #   - Partial overlap: retun underlapping areas as a list of blocks
        # 2. If Total overlap - return -> We are Done
        #   If No overlap - try next existing block
        #   If Partial overlap: try next existing block against each of the remaining on blocks
        # 3. If no more existing blocks to try: Add list of remaining blocks to on_list

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

    def underlap_1d(
        self, new_line: Tuple[int, int], existing_line: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Calculates underlap between two 1 dimensional lines
        Returns List of sections

        """
        new_low, new_high = new_line
        existing_low, existing_high = existing_line
        underlaps = []

        if new_low > existing_high:
            # +--existing--+
            #                   +--new--+
            return [new_line]
        if new_high < existing_low:
            #                   +--existing--+
            # +--new--+
            return [new_line]
        if new_low >= existing_low and new_high <= existing_high:
            # +--existing--+
            #    +--new--+
            return []
        if new_low < existing_low:
            #      +--existing-------------
            # +--new-----------------------
            underlaps.append((new_low, existing_low - 1))
        if new_high > existing_high:
            # ---existing--+
            # ------------------------new--+
            underlaps.append(existing_high + 1, new_high)
        return underlaps

    def underlap(self, new_block: Block, existing_block: Block) -> List[Block]:
        """Calculates area of overlap or underlap and returns underlap"""
        x_underlaps = self.underlap_1d(
            new_block.x_dimension, existing_block.x_dimension
        )
        y_underlaps = self.underlap_1d(
            new_block.y_dimension, existing_block.y_dimension
        )
        z_underlaps = self.underlap_1d(
            new_block.z_dimension, existing_block.z_dimension
        )
        # How do I compile these, especially if one has zero underlap
        underlaps = []

    def process_off_block(self, block: Block):
        """Update Reactor to turn OFF this block"""


def main():
    big_block = Block((0, 100), (0, 100), (0, 100))
    small_block = Block((0, 90), (0, 90), (0, 90))
    my_reactor = Reactor()
    overlapping_block = my_reactor.overlap(big_block, small_block)
    if overlapping_block == small_block:
        print("Overlap Correct")
    remaining_blocks = my_reactor.subtract_blocks(big_block, small_block)
    for block in remaining_blocks:
        print(block)


if __name__ == "__main__":
    main()
