#!/usr/bin/python3
"""UTF-8 Validation Algorithm"""


def validUTF8(data):
    """Check whether data is valid UTF-8."""
    bytes_to_follow = 0

    for n in data:
        binary_str = format(n % 256, "08b")

        if bytes_to_follow > 0:
            index = 0

            while index < 2:
                if index == 0 and binary_str[index] != "1":
                    return False

                if index == 1 and binary_str[index] != "0":
                    return False

                index += 1

            bytes_to_follow -= 1

        elif binary_str[0] == "0":
            continue

        elif binary_str[:3] == "110":
            bytes_to_follow = 1

        elif binary_str[:4] == "1110":
            bytes_to_follow = 2

        elif binary_str[:5] == "11110":
            bytes_to_follow = 3

        else:
            return False

    return bytes_to_follow == 0
