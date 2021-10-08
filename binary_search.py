import csv
from merge_sort import merge_sort


def binary_search(A, target):
    pivot = len(A) // 2
    if len(A) == 1 and A[pivot] != target:
        return False
    if A[pivot] == target:
        find_city(target)
        return True
    elif A[pivot] < target:
        return binary_search(A[pivot:], target)
    else:
        return binary_search(A[:pivot], target)


def find_city(lat):
    with open('worldcities.csv', encoding="utf8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if lat == float(row['lat']):
                print(row['city_ascii'])


def read_csv():
    A = []
    with open('worldcities.csv', encoding="utf8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            A.append(float(row['lat']))
    return A


if __name__ == '__main__':
    lat = read_csv()
    merge_sort(lat, 0, len(lat))
    value = 35.6897
    print(binary_search(lat, value))






