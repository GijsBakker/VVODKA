#!/usr/bin/python3

"""
Rabin_karp.py is a script used by by VVODKA to find substrings within a larger string
"""

bin_dict = {0b00: 1, 0b01: 2, 0b10: 3, 0b11: 4}
#bin_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}


def custom_hash(text):
    """
    This function takes text and converts it to a number
    :param text: the text that needs to be hashed
    :return: A number resulting from the hash of the given text
    """
    number = 0
    length = len(text)
    for index, letter in enumerate(text):
        # 10 should be fine being a 4 considering there are only 4 possible letters
        number += bin_dict[letter] * (10 ** (length - index - 1))

    return number


def rabin_karp(sub_str, text):
    """
    This function returns the first index of each match where the substring occurs in the text.
    :param sub_str: A substring
    :param text: The text in which the substring has to be found
    :return: A list of integers
    """
    # Zet de substr van lengte K om naar een getal X afhankelijk aan de hashfunction
    sub_hashed = custom_hash(sub_str)
    sub_len = len(sub_str)

    overlaps = []   # the first indexes of the overlapping strings
    text_hashed = custom_hash(text[0:sub_len])

    # loop over the text - sub_len
    for index in range(len(text)-sub_len+1):

        # update number without looping over each individual letter, looking only at the dropping and new letter
        if index != 0:
            # subtract waarde van de eerste letter van de hashfunction
            # doe overige getal x10
            # Add waarde nieuwe getal
            print(text, index)
            text_hashed = (text_hashed - bin_dict[text[index - 1]] * 10 ** (sub_len - 1)) * 10 + \
                          custom_hash(text[index+sub_len-1])

        if text_hashed == sub_hashed:
            if sub_str == text[index: index+sub_len]:
                overlaps.append(index)

    return overlaps


def main():
    sub_str = "ACACAGT"
    text_str = "ACACACAGTACACAGT"
    finds = rabin_karp(sub_str, text_str)
    print(finds)


if __name__ == "__main__":
    main()
