#!/usr/bin/python3

"""
Rabin-karp.py is a script used by by VVODKA to find substrings within a larger string
"""

bin_dict = {0b00: 1, 0b01: 2, 0b10: 3, 0b11: 4}
bin_dict_temp = {'A': 1, 'C': 2, 'G': 3, 'T': 4}


def custom_hash(text):
    """
    This function takes text and converts it to a number
    :param text: the text that needs to be hashed
    :return: A number resulting from the hash of the given text
    """
    number = 0
    length = len(text)
    print(length)
    for index, letter in enumerate(text):
        number += bin_dict_temp[letter] * (10 ** (length - index-1))

    return number


def rabin_karp(sub_str, text):
    """
    """
    # Zet de substr van lengte K om naar een getal X afhankelijk aan de hashfunction
    sub_hashed = custom_hash(sub_str)

    # loop over de text
    #   Als index = 0
    #       Neem het begin van de text met lengte K, zet dit om in een getal Y naar de hand van de hashfunction
    #   Anders
    #       subtract waarde van de eerste letter van de hashfunction
    #       doe overige getal x10
    #       Add waarde nieuwe getal

    #   Als X = Y
    #       pak vergelijk de text met de sub string
    #       Als die hetzelfde is markeer het
    #   Anders
    #       schuif op in de text.


def main():
    sub_str = "ACACAGT"
    number = custom_hash(sub_str)
    print(number)


if __name__ == "__main__":
    main()
