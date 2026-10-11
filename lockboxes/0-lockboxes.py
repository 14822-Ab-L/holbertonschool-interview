#!/usr/bin/python3
"""Determine if all boxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    if not boxes:
        return True

    opened = {0}
    to_visit = [0]

    while to_visit:
        box = to_visit.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                to_visit.append(key)

    return len(opened) == len(boxes)
