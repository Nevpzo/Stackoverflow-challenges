# ------------------
# Imports
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# ------------------
# Function
def decode_lsb(path):
    # Extract last bit of every pixel channel
    img = np.asarray(Image.open(path))
    bits = ''.join(str(v & 1) for v in img.flatten())

    header = bits[:2]

    if header == '00': # Hidden text
        msg_length = int(bits[2:18], 2)

        # First 2+16 bits are for header and message length
        msg_bits = bits[18:18 + msg_length]
        message = ''.join(
            chr(int(msg_bits[i:i+8], 2))
            for i in range(0, msg_length, 8)
        )

        print("Hidden message:")
        print(message)

    elif header == '10': # Hidden binary image
        width = int(bits[2:18], 2)
        height = int(bits[18:34], 2)

        print(f"Hidden image size: {width} x {height}")

        # First 2+16+16 bits are for header, width and height
        pixel_bits = bits[34:34 + width * height]
        image = np.array(
            [int(b) for b in pixel_bits],
            dtype=np.uint8
        ).reshape(height, width) * 255

        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.show()

    else:
        print(f"Unknown header: {header}")


# ------------------
# Run decoding
decode_lsb('./CodingChallenge/black.png')
decode_lsb('./CodingChallenge/butterfly.png')

