import os
from PIL import Image
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt

plt.rcdefaults()
DIR_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(DIR_PATH)


def percentize(data):
    return [(x / sum(data)) * 100 for x in data]


def benford_image():
    # Make a list of zeroes
    tally = [0] * 10
    # Load your image and convert to numpy
    IMAGE_PATH = os.path.join(BASE_DIR, "beck.jpeg")
    image = Image.open(IMAGE_PATH)
    data = asarray(image)
    # Iterate through each pixel and tally the first digit
    for i, row in enumerate(data):
        for j, pixel in enumerate(row):
            for num in pixel:
                start = int(str(num)[0])
                tally[start] = tally[start] + 1
    # Truncate zero as a first digit, make percentage, and return
    tally = tally[1:]
    return percentize(tally)


def plot_benford(data):
    y_pos = np.arange(len(data))
    plt.bar(y_pos, data, align='center', alpha=0.5)
    plt.xticks(y_pos, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    plt.title('Benford Test')
    plt.ylabel('Frequency')
    plt.xlabel('First Digit of Pixels')

    plt.show()


def main():
    data = benford_image()
    plot_benford(data)


if __name__ == '__main__':
    main()
