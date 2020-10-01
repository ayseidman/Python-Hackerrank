

if __name__ == '__main__':
    arraySize = int(input())
    array = list(map(int, input().split()))

    array.sort()
    print(array[-2])

