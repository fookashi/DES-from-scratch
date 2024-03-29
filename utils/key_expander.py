from interfaces.key_expander import IKeyExpander
from utils.permutator import Permutator
from tables import PC1, PC2, SHIFT_SCHEDULE
from utils.shifter import CircularShifter
import asyncio


class KeyExpander(IKeyExpander):

    async def expand_key(self, original_key: bytes | bytearray) -> tuple[bytes]:
        round_keys = list()

        permuted_key = await Permutator.permutate(original_key, PC1)

        # key_bits = int.from_bytes(permuted_key, 'big')
        # left_len = len(permuted_key) * 8 // 2
        # right_len = len(permuted_key) * 8 - left_len
        # right_part = (key_bits & ((1 << right_len) - 1))
        # left_part = (key_bits >> right_len)
        left_part = permuted_key[:len(permuted_key) // 2]
        right_part = permuted_key[len(permuted_key) // 2:]
        for shift in SHIFT_SCHEDULE:
            # shifted_left = CircularShifter.left_shift(left_part, left_len, shift)
            # shifted_right = CircularShifter.left_shift(right_part, right_len, shift)
            # combined_round_key = (shifted_left << right_len | shifted_right).to_bytes(len(permuted_key), 'big')
            shifted_left = CircularShifter.left_shift_bytes(left_part, shift)
            shifted_right = CircularShifter.left_shift_bytes(right_part, shift)
            combined_round_key = shifted_right + shifted_right
            round_keys.append(
                asyncio.create_task(Permutator.permutate(combined_round_key, PC2)))
            left_part = shifted_left
            right_part = shifted_right

        return await asyncio.gather(*round_keys)
