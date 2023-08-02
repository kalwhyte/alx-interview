#!/usr/bin/python3
'''Lockboxes
'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened
    '''
    if not boxes:
        return False
    if not isinstance(boxes, list):
        return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for key in boxes[key]:
            if key not in keys:
                if key < len(boxes):
                    keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False