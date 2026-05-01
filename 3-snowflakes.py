import random

def insertPattern(snowflake, pattern, x1, x2, y1, y2):
    for i, row in enumerate(pattern):
        snowflake[y1 + i][x1:x2] = row

    return snowflake

def basePattern(seed):
    random.seed(seed)
    choices = [0, 1, 2, 3]
    weights = [1, 3, 3, 3]

    return [
        [random.choices(choices, weights=weights)[0] for _ in range(4)],
        [0] + [random.choices(choices, weights=weights)[0] for _ in range(3)]
    ]

def mirrorPattern(pattern, axis):
    if axis == 0:
        mirrorMap = {0:0, 1:2, 2:1, 3:3, 4:4, 5:6, 6:5, 7:7, 8:8}
        rows, cols = 2, 4
        sym = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sym[i][cols - 1 - j] = mirrorMap[pattern[i][j]]

    elif axis==1:
        mirrorMap = {0:0, 1:2, 2:1, 3:4, 4:3, 5:7, 6:8, 7:5, 8:6}
        rows, cols = 3, 10
        sym = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sym[rows - 1 - i][j] = mirrorMap[pattern[i][j]]
    else:
        raise ValueError('Unknown axis')

    return sym

def createCore(seed):
    tops = [
       [[5, 5, 1, 2, 6, 6],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 1, 2, 0, 0]],

       [[0, 0, 1, 2, 0, 0],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 1, 2, 0, 0]],

       [[0, 0, 2, 1, 0, 0],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 2, 1, 0, 0]],

       [[0, 3, 1, 2, 3, 0],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 1, 2, 0, 0]],
    ]

    return tops[seed % len(tops)]


def makeFlake(seed):
    print(f"Snowflake {seed}:")
    snowflake = [[0]*10 for _ in range(6)]
    
    #Create core of snowflake
    core = createCore(seed)
    snowflake = insertPattern(snowflake, core, 2, 7, 0, 3)

    # Create top of snowflake
    pattern = basePattern(seed)
    horSym = mirrorPattern(pattern, 0)
    snowflake = insertPattern(snowflake, pattern, 0, 4, 1, 3)
    snowflake = insertPattern(snowflake, horSym,  6, 10, 1, 3)
 
    # Mirror on bottom
    verSym = mirrorPattern(snowflake[0:3], 1)
    snowflake = insertPattern(snowflake, verSym, 0, 10, 3, 6)

    return snowflake

# -------------------------------
# PRINTING

def printFlake(snowflake):
    mapping = {
        0: " ",
        1: "/",
        2: "\\",
        3: "_",
        4: "‾",
        5: "⠠",
        6: "⠄",
        7: "⠈",
        8: "⠁"
    }

    for i in range(len(snowflake)):
        row = ""
        for elem in snowflake[i]:
            try:
                row += mapping[elem]
            except:
                row += elem
        print(row)

printFlake(makeFlake(random.randint(0, 999)))
