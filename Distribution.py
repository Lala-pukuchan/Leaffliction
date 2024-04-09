import sys
import os
import matplotlib.pyplot as plt


def countPics(dir):
    """
    count pictures in subdirectories
    """
    storage = {}
    for root, dirs, files in os.walk(dir):
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            count = 0
            for file in os.listdir(subdir_path):
                if file.lower().endswith((".png", ".jpg", ".jpeg")):
                    count += 1
            storage[subdir] = count
    return storage


def createChart(storage):
    """
    create bar/pie chart
    """
    labels = list(storage.keys())
    values = list(storage.values())
    colors = ["red", "blue", "green", "yellow"]
    plt.bar(labels, values, color=colors)
    plt.show()
    plt.pie(values, labels=labels, colors=colors, autopct="%.1f%%")
    plt.show()


def distribution(dir):
    """
    load images from subdirectories
    create chart to see the distribution
    """
    storage = countPics(dir)
    print("storage", storage)
    createChart(storage)


def main():
    if len(sys.argv) != 2:
        print("./Distribution.py ./Apple")
        exit(1)
    distribution(sys.argv[1])


if __name__ == "__main__":
    main()
