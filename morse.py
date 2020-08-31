#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = """ manuel velasco  John(SE Coach) Howard Post (SE Tutor)"""

from morse_dict import MORSE_2_ASCII


def decode_morse(morse):
    MORSE_2_ASCII[''] = ' '
    empty_string = ""
    list_morse_space = morse.split(' ')
    print(list_morse_space)
    for words in list_morse_space:
        empty_string += MORSE_2_ASCII[words]
    print(' '.join(empty_string.split()))
    return ' '.join(empty_string.split())


def decode_bits(bits):
    bits = bits.strip('0')

    two_bits = min([len(bit)
                    for bit in bits.split("1") + bits.split("0") if bit])

    return bits.replace(
        '111' * two_bits, '-'
    ).replace(
        '1' * two_bits, '.'
    ).replace(
        "0000000" * two_bits, '   '
    ).replace(
        '000' * two_bits, ' '
    ).replace(
        '0' * two_bits, ''
    )


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
