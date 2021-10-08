import csv
import random


def QuickSort(A):
    elements = len(A)

    if elements < 2:
        return A

    position = 0  # Current position

    for i in range(1, elements):  # Partitioning loop
        if A[i] <= A[0]:
            position += 1
            temp = A[i]
            A[i] = A[position]
            A[position] = temp

    temp = A[0]
    A[0] = A[position]
    A[position] = temp  # Brings pivot to it's appropriate position

    left = QuickSort(A[0:position])  # Sorts the elements to the left of pivot
    right = QuickSort(A[position + 1:elements])  # sorts the elements to the right of pivot

    A = left + [A[position]] + right  # Merging everything together

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
    B = QuickSort(A)
    for i in B:
        print(i)