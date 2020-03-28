if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    array = list(map(int,arr))
    array = list(dict.fromkeys(array))
    
    array.sort()
    
    print(array[-2])

