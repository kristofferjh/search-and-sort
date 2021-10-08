import csv
from merge_sort import merge_sort
import random


def optCost(freq, i, j):
    # Base cases
    if j < i:  # no elements in this subarray
        return 0
    if j == i:  # one element in this subarray
        return freq[i]

    # Get sum of freq[i], freq[i+1], ... freq[j]
    fsum = Sum(freq, i, j)

    # Initialize minimum value
    Min = 999999999999

    # One by one consider all elements as
    # root and recursively find cost of
    # the BST, compare the cost with min
    # and update min if needed
    for r in range(i, j + 1):
        cost = (optCost(freq, i, r - 1) +
                optCost(freq, r + 1, j))
        if cost < Min:
            Min = cost

    # Return minimum value
    return Min + fsum


# The main function that calculates minimum
# cost of a Binary Search Tree. It mainly
# uses optCost() to find the optimal cost.
def optimalSearchTree(keys, freq, n):
    # Here array keys[] is assumed to be
    # sorted in increasing order. If keys[]
    # is not sorted, then add code to sort
    # keys, and rearrange freq[] accordingly.
    return optCost(freq, 0, n - 1)


# A utility function to get sum of
# array elements freq[i] to freq[j]
def Sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


def read_csv():
    A = {}
    with open('worldcities.csv', encoding="utf8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['country'] == 'Norway':
                A[row['lat']] = row['city']
    return A


if __name__ == '__main__':
    A = read_csv()
    lat = []
    freqencies = [10, 20, 30, 40]
    freq = []

    for key in A:
        lat.append(key)

    merge_sort(lat, 0, len(lat))

    for i in lat:
        freq.append(random.choice(freqencies))

    print('Cost of optimal BST is:', optimalSearchTree(lat[1:10], freq, 10))