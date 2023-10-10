#!/usr/bin/python3
"""Lockboxes
"""


def canUnlockAll(boxes):
    """
        args(list): box
        return true or false
    """
    if boxes:
        n_boxes = [0]
        n = len(n_boxes)
        for i in boxes:
            for j in i:
                if j < len(boxes) and j not in n_boxes and j != boxes.index(i):
                    n_boxes.append(j)
        if len(n_boxes) == len(boxes):
            return True
    return False
