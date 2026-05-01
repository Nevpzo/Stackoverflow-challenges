from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# SETUP

message = "La vaca saturno saturnita, bombarbilo crocodilo y gussini"
if len(message) * 5 > 19*19-9:
    raise Exception('Message is too long')

board = np.array([[0 for _ in range(19)] for _ in range(19)])

key = np.array([2, 0, 1, 1, 2, 0, 0, 1, 2])

# ----------------------------------------------------
# FUNCTIONS

def toBase3(s):
    return np.base_repr(s, base=3).zfill(5)

def ternLookup(key, a, b):
    key = np.reshape(key, (3, 3))
    return key[a][b]

def cipher(key, message):
    key_digits = list(key)
    flat_message = ''.join(message)
    return ''.join(
        str(ternLookup(key, key_digits[i % len(key_digits)], int(ch)))
        for i, ch in enumerate(flat_message)
    )

# ----------------------------------------------------
# PREPARE MESSAGE

message += ' ' + ''.join(str(i) for i in range((69 - len(message))))
message = list(message)
for i in range(len(message)):
    message[i] = toBase3(ord(message[i]))

message = cipher(key, message)

# ----------------------------------------------------
# INSERT MESSAGE AND KEY IN BOARD

board[0][:9] = key

index = 9
count = 0
for row in range(19):
    cols = range(19) if row % 2 == 0 else range(18, -1, -1)
    for col in cols:
        if count >= 9:  # first 9 cells are for the key
            board[row][col] = int(message[index - 9]) # -9 to align board and message start
            index += 1
        count += 1

pprint(board)

# ----------------------------------------------------
# SHOW GO BOARD

size = board.shape[0]
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')
ax.set_aspect('equal')

# Draw grid lines
for i in range(size):
    ax.plot([0, size - 1], [i, i], color='black')
    ax.plot([i, i], [0, size - 1], color='black')

# Draw stones
for i in range(size):
    for j in range(size):
        if board[i, j] == 1:
            ax.plot(j, size - 1 - i, 'wo', markersize=18, markeredgecolor='black')
        elif board[i, j] == 2:
            ax.plot(j, size - 1 - i, 'ko', markersize=18)
plt.show()

# ===============================================================

# ===============================================================

# ===============================================================

# ===============================================================

def rLookup(row, value):
    for col, v in enumerate(row):
        if v == value:
            return col

def decrypt_board(board):
    # Step 1: Read the key from the first 9 cells
    key = list(board[0][:9])
    key_matrix = np.reshape(key, (3, 3))

    # Step 2: Extract the encrypted digits from the board (snake pattern)
    digits = []
    flat_index = 0
    for row in range(19):
        cols = range(19) if row % 2 == 0 else range(18, -1, -1)
        for col in cols:
            if flat_index >= 9:  # Skip the key
                digits.append(int(board[row][col]))
            flat_index += 1

    # Step 3: Undo the cipher using the key
    decoded = []
    for i, val in enumerate(digits):
        a = key[i % 9]
        row = key_matrix[a]
        original = rLookup(row, val)
        decoded.append(str(original))

    # Step 4: Convert base-3 chunks to characters
    result = []
    for i in range(0, len(decoded) - 4, 5):
        chunk = ''.join(decoded[i:i+5])
        result.append(chr(int(chunk, 3)))

    return ''.join(result)

message = decrypt_board(board)
print("Decrypted:", message)