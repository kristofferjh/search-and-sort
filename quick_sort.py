import csv
import random


def quick_sort(A):
    A_1 = []
    A_2 = []
    position = 0
    if len(A) > 1:
        pivot = random.choice(A)
        for item in A:
            if item < pivot:
                A_1.append(item)
            else:
                A_2.append(item)
    else:
        return A

    left = quick_sort(A[0:position])
    right = quick_sort(A[position + 1:len(A)])
    A = left + [A[position]] + right

    return A


def read_csv():
    A = []
    with open('worldcities.csv', encoding="utf8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            A.append(float(row['lat']))
    return A


if __name__ == '__main__':
    A = read_csv()

    quick_sort(A)

    for i in A:
        print(i)